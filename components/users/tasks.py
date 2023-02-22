from run_celery import celery
from components.users.email import email_verification


def email_verification_task(target, verification_link):
    email_verification(target, verification_link)