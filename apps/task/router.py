from fastapi import APIRouter

from . import service
from apps.task.celery_task.examples import task_add_two_num


router = APIRouter()


@router.get("/tasks", summary="查看 tasks 列表")
async def get_task_list():
    tasks = service.TaskService.get_task_list()
    return tasks


@router.get("/tasks/{task_id}", summary="查看 task 详情")
async def get_task_detail(task_id: str):
    result = service.TaskService.get_task_result_by_id(task_id)
    print(result)
    return result


@router.post("/add-two-num", summary="两数相加")
async def add_two_num(num1: int, num2: int):
    task = task_add_two_num.delay(num1, num2)
    return {"task_id": task.id}
