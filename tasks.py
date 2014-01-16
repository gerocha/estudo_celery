from celery import Celery
from celery.utils.log import get_task_logger
import logging

logger = get_task_logger(__name__)
handler = logging.FileHandler('tasks.log')
logger.addHandler(handler)

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    logger.warning('teste')
    return x + y
