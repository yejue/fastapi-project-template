from fastapi import Request


async def get_headers(request: Request):
    """获取请求头信息"""
    return request.headers
