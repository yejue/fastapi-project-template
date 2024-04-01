from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from sqlalchemy import select

from dependencies import get_db
from apps.user.dependencies import get_current_user
from apps.user.models import UserModel
from . import models, schemas, service

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


# @router.put("/notes/{note_id}", summary="更新笔记")
# async def update_note(
#         note_id: int,
#         note: schemas.NoteCreateSchema,
#         db: Session = Depends(get_db)
# ):
#     db_note = service.NoteService.get_note_by_id(db, note_id)


@router.patch("/notes/{note_id}", summary="部分笔记更新")
async def partial_update_note(
        note_id: int,
        note: schemas.NoteUpdateSchema,
        db: Session = Depends(get_db)
):
    db_note = service.NoteService.get_note_by_id(db, note_id)
    return service.NoteService.partial_update_note(db, db_note, note)
