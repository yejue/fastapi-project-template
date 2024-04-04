from pydantic import Field
from sqlalchemy.orm import Session
from apps.user.models import UserModel


class BasePermission:
    """基础 Permission 类"""

    status_code: int = Field(description="状态码")
    detail: str = Field(description="详细信息")

    @staticmethod
    def has_permission(user: UserModel):
        return True

    @staticmethod
    def has_object_permission(db: Session, user: UserModel, object_id: int):
        pass


class IsActiveUser(BasePermission):
    """是否有效用户"""

    status_code = 401
    detail = "当前用户已被停用"

    @staticmethod
    def has_permission(user: UserModel):
        return bool(user.is_active)


class IsSuperUser(BasePermission):
    """是否超级用户"""

    status_code = 403
    detail = "没有足够的权限"

    @staticmethod
    def has_permission(user: UserModel):
        return user.is_superuser


__all__ = ["BasePermission", "IsSuperUser", "IsActiveUser"]
