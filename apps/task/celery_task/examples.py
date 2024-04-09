from apps.task.celery_app import celery_app


@celery_app.task(queue="default")
def task_beat_example():
    print("Beat trigger, your celery is running healthily..")
    return True


@celery_app.task(queue="default")
def task_add_two_num(num1: int, num2: int):
    return num1 + num2
