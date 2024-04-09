from fastapi import HTTPException
from celery.result import AsyncResult
from celery.exceptions import NotRegistered

from .celery_app import celery_app


class TaskService:
    """Celery Task 服务类"""

    @staticmethod
    def get_task_list():
        tasks = [k for k in celery_app.tasks.keys() if not k.startswith('celery.')]
        return tasks

    @staticmethod
    def get_task_result_by_id(uid: str):
        try:
            result = AsyncResult(id=uid, app=celery_app)  # 这里要注意被序列化引用出现的无限递归情况
            return {"task_id": result.id, "status": result.status, "result": result.result}
        except NotRegistered:
            raise HTTPException(status_code=404, detail='任务不存在')
