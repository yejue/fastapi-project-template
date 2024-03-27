from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import relationship
from models import BaseModelWithDatetime


class UserModel(BaseModelWithDatetime):
    """用户表"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    account = Column(String(50), doc="账户", unique=True, nullable=False)
    username = Column(String(50), doc="用户名", default="未命名")
    phone = Column(String(50), nullable=True, doc="手机号")
    hashed_password = Column(String, doc="用户密码（已加密）")

    is_superuser = Column(Boolean, default=False, doc="是否超级用户")
    is_active = Column(Boolean, default=True, doc="是否可用")

    # 笔记关系
    notes = relationship("NoteModel", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id} account={self.account})"
