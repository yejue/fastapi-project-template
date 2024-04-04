from sqlalchemy.orm import Session
from sqlalchemy import select

from apps.permissions import BasePermission
from apps.user.models import UserModel

from . import models


class IsNoteOwner(BasePermission):
    status_code = 403
    detail = "没有该笔记的权限"

    @staticmethod
    def has_object_permission(object_id: int, user: UserModel, db: Session):
        stmt = select(models.NoteModel)\
            .where(models.NoteModel.id == object_id)\
            .where(models.NoteModel.user_id == user.id)
        res = db.scalars(stmt).one_or_none()
        return bool(res)
