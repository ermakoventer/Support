from celery import shared_task
from support.service import change


@shared_task
def send_status_message(user_email):
    change(user_email)