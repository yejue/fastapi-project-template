from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from jose.jwt import JWTError

from utils.encrypt import get_password_hash, verify_password
from utils import jwt

from . import schemas, models, constants

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class UserService:
    """用户模型表操作类"""

    @staticmethod
    def create_user(db: Session, user: schemas.UserCreateSchema):
        # 将原密码加密后存储
        hashed_password = get_password_hash(user.password)

        db_user = models.UserModel(
            hashed_password=hashed_password,
            username=user.username,
            phone=user.phone,
            account=user.account,
        )

        db.add(db_user)
        try:
            db.commit()
            db.refresh(db_user)
        except IntegrityError:
            raise HTTPException(status_code=409, detail="该数据已经存在")
        return db_user

    @staticmethod
    def get_user_by_account(db: Session, account: str):
        """使用 account 获取 user 对象"""
        stmt = select(models.UserModel).where(models.UserModel.account == account)
        user = db.scalars(stmt).one()
        if user:
            return user

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        """使用 ID 获取 user 对象"""
        stmt = select(models.UserModel).where(models.UserModel.id == user_id)
        user = db.scalars(stmt).one()
        if user:
            return user

    @staticmethod
    def authenticate_user(db: Session, account: str, password: str):
        """用户认证"""
        user = UserService.get_user_by_account(db, account)
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user

    @staticmethod
    def create_token(data: dict):
        """创建认证 token"""
        secret_key = constants.SECRET_KEY
        exp_seconds = constants.ACCESS_TOKEN_EXPIRE_SECONDS
        token = jwt.create_access_token(data, secret_key, exp_seconds)
        return token

    @staticmethod
    def get_current_user(db: Session, token: str = Depends(oauth2_scheme)):
        """获取当前用户"""
        secret_key = constants.SECRET_KEY
        try:
            payload = jwt.decrypt_access_token(token, secret_key)
        except JWTError:
            raise HTTPException(status_code=401, detail="Token 解密失败")

        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="无效 Token")

        user = UserService.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=401, detail="未匹配到对应用户")

        return user
