from fastapi import APIRouter, Depends

from .dependencies import get_headers
from .schemas import HelloUserModel, BookModel, BookListModel
from .service import UserService

router = APIRouter()


@router.get("/my-headers")
async def hello(headers: dict = Depends(get_headers)):
    """访问返回自身 headers 接口"""
    data = {"headers": headers}
    return {"message": "hello", "data": data}


@router.post("/users")
async def add_user(user: HelloUserModel):
    UserService.add_user_to_database(user)
    return {"message": "OK"}


@router.get("/books", response_model=BookListModel)
async def get_books():
    books_list = [
        {"name": "《三体》", "author": "刘慈欣"},
        {"name": "《红楼梦》", "author": "曹雪芹"},
        {"name": "《哈利·波特与魔法石》", "author": "J.K.罗琳"}
    ]
    return books_list


@router.post("/books", response_model=BookModel)
async def add_book(book: BookModel):
    return book
