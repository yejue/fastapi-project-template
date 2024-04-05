from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from . import schemas, service

router = APIRouter()


@router.post("/register", summary="用户注册", response_model=schemas.UserSchema)
async def user_register(user: schemas.UserCreateSchema, db: Session = Depends(get_db)):
    return service.UserService.create_user(db, user)


@router.post("/login", summary="用户登录")
async def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 认证密码 获得 user
    user = service.UserService.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="认证未通过，检查密码或账户")

    # 创建 token
    data = {"user_id": user.id}
    token = service.UserService.create_token(data)
    return schemas.TokenSchema(access_token=token)
