import os
from celery import Celery

env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6380'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6380')


celery= Celery('R_tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)
