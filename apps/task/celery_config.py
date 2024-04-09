from celery.schedules import crontab


class CelerySettings:
    def __init__(self):
        # redis://:password@hostname:port/db_number
        self.broker_url = "redis://:yejue123@192.168.119.128:6379/10"
        self.result_backend = "redis://:yejue123@192.168.119.128:6379/10"
        self.task_serializer = "json"
        self.result_serializer = "json"
        self.accept_content = ["json"]
        self.timezone = "Asia/Shanghai"
        self.enable_utc = True
        self.broker_connection_retry_on_startup = True

        self.beat_schedule = {
            "celery_heartbeat": {
                "task": "task_beat_example",  # 任务函数，由 app.autodiscover 搜索到对应文件
                "schedule": crontab(minute="*/1")  # 每分钟执行一次
            },
        }

        self.task_packages = [
            "apps.task.celery_task",
            "apps.task.celery_task.examples",
        ]


settings = CelerySettings()
