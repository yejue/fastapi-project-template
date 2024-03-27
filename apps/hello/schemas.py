from typing import List
from pydantic import BaseModel, Field


class HelloUserModel(BaseModel):
    """示例用用户信息模型"""
    name: str
    age: int = Field(..., ge=0, lt=200)
    phone: str = Field(..., pattern=r'^1[3456789]\d{9}$')


class BookModel(BaseModel):
    name: str
    author: str


class BookListModel(BookModel):
    books: List[BookModel]
