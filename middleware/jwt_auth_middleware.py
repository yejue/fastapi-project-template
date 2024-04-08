"""
此中间件目的是为了实现 request.user 这个接口
"""
from fastapi import Request
from jose.jwt import JWTError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.authentication import AuthenticationBackend, AuthCredentials

from utils import jwt
from config import settings
from database import get_db
from apps.user import service as user_service


class JWTAUTHBackend(AuthenticationBackend):
    """JWT 验证后端"""

    async def authenticate(self, request: Request):
        auth_data = request.headers.get("authorization", None)
        if auth_data is None:
            return None

        _, token = auth_data.split(" ")

        try:
            # 解密失败，token 信息不正确
            payload = jwt.decrypt_access_token(token, secret_key=settings.SECRET_KEY)
        except JWTError:
            return None

        user_id = payload.get("user_id")
        if not user_id:  # 无效 user
            return None

        db = next(get_db())
        user = user_service.UserService.get_user_by_id(db, user_id)

        if not user:
            return None
        return AuthCredentials(["authenticated"]), user


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        res = await JWTAUTHBackend().authenticate(request)
        if res is not None:
            credentials, user = res
            request.scope["user"] = user
            request.scope["authenticated"] = credentials
        else:
            request.scope["user"] = None

        response = await call_next(request)
        return response
