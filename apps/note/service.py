from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import schemas, models


class NoteService:
    """笔记表操作类"""

    @staticmethod
    def create_note(db: Session, note: schemas.NoteCreateSchema, user_id: int):
        """创建笔记"""
        db_note = models.NoteModel(
            title=note.title,
            content=note.content,
            is_public=note.is_public,
            user_id=user_id
        )

        db.add(db_note)
        try:
            db.commit()
            db.refresh(db_note)
        except IntegrityError:
            raise HTTPException(status_code=409, detail="该数据已经存在")
        return db_note

    @staticmethod
    def partial_update_note(db: Session, db_note: models.NoteModel, note: schemas.NoteUpdateSchema):
        """部分更新"""
        if note.title is not None:
            db_note.title = note.title
        if note.content is not None:
            db_note.content = note.content
        if note.is_public is not None:
            db_note.is_public = note.is_public

        try:
            db.commit()
            db.refresh(db_note)
        except IntegrityError as e:
            raise HTTPException(status_code=409, detail=f"更新的字段已经存在 {e}")
        return db_note

    @staticmethod
    def get_note_by_id(db: Session, note_id: int):
        stmt = select(models.NoteModel).where(models.NoteModel.id == note_id)
        note = db.scalars(stmt).one()
        if not note:
            raise HTTPException(status_code=404, detail="笔记不存在")
        return note
