from starlette.requests import Request
from starlette.responses import JSONResponse


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    # 在这里对错误进行捕获，将错误信息发送到某处，如：企业微信机器人
    # ...
    data = {"detail": "服务器内部出错", "error": str(exc)}
    return JSONResponse(status_code=500, content=data)
