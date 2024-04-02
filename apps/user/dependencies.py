from fastapi import Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose.jwt import JWTError

from utils import jwt
from dependencies import get_db
from apps.user import constants as user_constant
from apps.user import service as user_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """获取当前用户"""
    secret_key = user_constant.SECRET_KEY
    try:
        payload = jwt.decrypt_access_token(token, secret_key)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token 解密失败")

    # 检验是否过期
    if not jwt.is_access_token_valid(expire_time_stamp=payload.get("exp")):
        raise HTTPException(status_code=401, detail="Token 已过期")

    # 检验 Token 用户信息
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="无效 Token")

    user = user_service.UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="未匹配到对应用户")

    return user
