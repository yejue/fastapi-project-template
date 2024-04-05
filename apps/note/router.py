from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from sqlalchemy import select

from database import get_db
from apps.user.dependencies import get_current_user
from apps.user.models import UserModel
from apps.permissions.dependencies import PermissionChecker
from apps.permissions import IsActiveUser

from . import models, schemas, service, permissions

router = APIRouter()


@router.get("/notes", summary="笔记列表", response_model=list[schemas.NoteSchema])
async def get_notes(db: Session = Depends(get_db)):
    stmt = select(models.NoteModel).where(models.NoteModel.is_public == True)
    res = [item for item in db.scalars(stmt)]
    return res


@router.post("/notes", summary="创建笔记")
async def create_note(
        note: schemas.NoteCreateSchema,
        db: Session = Depends(get_db),
        current_user: UserModel = Depends(get_current_user)
):
    user_id = current_user.id
    print(user_id)
    return service.NoteService.create_note(db=db, note=note, user_id=user_id)


@router.patch(
    "/notes/{note_id}",
    summary="部分笔记更新",
    dependencies=[Depends(PermissionChecker([IsActiveUser]))]
)
async def partial_update_note(
        note_id: int,
        note: schemas.NoteUpdateSchema,
        db: Session = Depends(get_db),
        user: UserModel = Depends(get_current_user)
):
    db_note = service.NoteService.get_note_by_id(db, note_id)

    # 对象权限校验
    PermissionChecker.check_object_permission(permissions.IsNoteOwner, db_note.id, user, db)
    return service.NoteService.partial_update_note(db, db_note, note)
