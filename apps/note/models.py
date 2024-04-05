from sqlalchemy import Column, String, Text, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
from utils.models import BaseModelWithDatetime


class NoteModel(BaseModelWithDatetime):
    """笔记表模型"""
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(50), doc="笔记标题")
    content = Column(Text, doc="笔记内容")
    is_public = Column(Boolean, default=True, doc="是否公开")

    user_id = Column(Integer, ForeignKey('users.id'), doc="用户ID")
    user = relationship("UserModel", back_populates="notes")

    def __repr__(self):
        return f"Note(id={self.id} user_id={self.user_id} title={self.title})"
