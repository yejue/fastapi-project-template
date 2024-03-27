from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from sqlalchemy import select

from dependencies import get_db

from . import models, schemas, service

router = APIRouter()


@router.get("/notes", summary="笔记列表", response_model=list[schemas.NoteSchema])
async def get_notes(db: Session = Depends(get_db)):
    stmt = select(models.NoteModel).where(models.NoteModel.is_public == True)
    res = [item for item in db.scalars(stmt)]
    return res


# @router.post("/notes", summary="创建笔记")
# async def create_note(note: schemas.NodeCreateSchema, db: Session = Depends(get_db)):
#     return service.NoteService.create_note(db, note)
