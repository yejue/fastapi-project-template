from fastapi import Depends, HTTPException

from apps.user.dependencies import get_current_user
from apps.user.models import UserModel


class BasePermission:
    """基础 Permission 类"""

    @staticmethod
    def has_permission(user: UserModel):
        return True

    @staticmethod
    def has_object_permission(object_id: int, user: UserModel):
        pass


class IsAuthenticated(BasePermission):
    """是否已经登录"""

    @staticmethod
    def has_permission(user: UserModel):
        # 认为 token 可以正常解出，并且 expire time 是在有限期内
        return bool(user)


def permission_classes(permissions: list):
    def decorator(func):
        async def wrapper(user: UserModel = Depends(get_current_user), *args, **kwargs):
            if permissions is None:
                raise ValueError("至少需要指定一个 Permission")

            for permission in permissions:
                if not permission.has_permission(user):
                    raise HTTPException(status_code=401, detail="身份验证未通过")
            res = await func(*args, **kwargs)
            return res
        return wrapper
    return decorator
