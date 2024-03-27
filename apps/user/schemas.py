from datetime import datetime
from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
    account: str = Field(description="账户")
    username: str = Field(description="用户名")
    phone: str = Field(description="手机号")


class UserSchema(UserBaseSchema):
    """用户 Schema"""
    id: int = Field(description="用户ID")
    is_superuser: bool = Field(description="是否超级用户")
    is_active: bool = Field(description="是否可用")
    update_time: datetime = Field(description="更新时间")
    create_time: datetime = Field(description="创建时间")

    class Config:
        from_attributes = True


class UserCreateSchema(UserBaseSchema):
    """创建用户 Schema"""
    password: str = Field(description="密码")


class UserLoginSchema(BaseModel):
    """用户登录 Schema"""
    account: str = Field(description="账户")
    password: str = Field(description="密码")


class TokenSchema(BaseModel):
    """用户认证 Token Schema"""
    access_token: str = Field(description="认证 Token")
    token_type: str = Field("bearer", description="Token 类型")
