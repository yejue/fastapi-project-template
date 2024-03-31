import uvicorn
from fastapi import FastAPI

# from apps.hello.router import router as hello_router
from apps.user.router import router as user_router
from apps.note.router import router as note_router

from exceptions import global_exception_handler
from database import BaseModel, engine

BaseModel.metadata.create_all(bind=engine)


app = FastAPI()
# app.include_router(hello_router, prefix="/hello")
app.include_router(user_router, prefix="/user")
app.include_router(note_router, prefix="/note")

# 注册错误捕获
app.add_exception_handler(Exception, global_exception_handler)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)