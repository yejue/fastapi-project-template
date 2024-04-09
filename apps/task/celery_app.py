from celery import Celery
from .celery_config import settings


def get_celery():
    app = Celery("default")
    app.config_from_object(settings)
    app.autodiscover_tasks(settings.task_packages)
    return app


celery_app = get_celery()

