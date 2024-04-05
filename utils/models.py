from sqlalchemy import Column, DateTime, func

from database import BaseModel


class BaseModelWithDatetime(BaseModel):
    """拥有更新时间和创建时间的基本模型"""
    __abstract__ = True

    create_time = Column(DateTime, default=func.now())
    update_time = Column(DateTime, default=func.now(), onupdate=func.now())
