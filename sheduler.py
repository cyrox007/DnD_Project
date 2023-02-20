from celery import Celery
from settings import config


def make_celery() -> Celery:
    celery = Celery(
        'app',
        broker=config.REDIS_URL,
        backend=config.REDIS_URL,
        include=[
            "components.image.tasks"
        ]
    )

    return celery


celery = make_celery()