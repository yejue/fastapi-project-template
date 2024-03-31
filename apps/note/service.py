from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import schemas, models


class NoteService:
    """笔记表操作类"""

    @staticmethod
    def create_note(db: Session, note: schemas.NoteCreateSchema, user_id: int):
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
