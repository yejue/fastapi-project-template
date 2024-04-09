import uvicorn
from fastapi import FastAPI

from apps.user.router import router as user_router
from apps.note.router import router as note_router
from apps.task.router import router as task_router

from middleware.globals import global_exception_handler
from middleware.jwt_auth_middleware import AuthMiddleware


app = FastAPI()
app.include_router(user_router, prefix="/user")
app.include_router(note_router, prefix="/note")
app.include_router(task_router, prefix="/task")

# 注册中间件
app.add_middleware(AuthMiddleware)

# 注册错误捕获
app.add_exception_handler(Exception, global_exception_handler)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
