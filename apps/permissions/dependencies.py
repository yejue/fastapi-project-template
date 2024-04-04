from typing import Type
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from apps.user.dependencies import get_current_user
from apps.user.models import UserModel
from apps.permissions import BasePermission


class PermissionChecker:
    """权限检查类"""

    def __init__(self, permissions: list):
        self.permissions = permissions

    def __call__(self, user: UserModel = Depends(get_current_user)):
        for permission in self.permissions:
            if not permission.has_permission(user):
                raise HTTPException(status_code=permission.status_code, detail=permission.detail)

    @staticmethod
    def check_object_permission(permission: Type[BasePermission],
                                object_id: int,
                                user: UserModel,
                                db: Session):
        if not permission.has_object_permission(user=user, object_id=object_id, db=db):
            raise HTTPException(status_code=permission.status_code, detail=permission.detail)
