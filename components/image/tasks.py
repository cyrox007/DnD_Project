from run_celery import celery
from components.image.handler import avatar_processing


@celery.task
def user_image_processing(file, new_path):
    avatar_processing(file, new_path)