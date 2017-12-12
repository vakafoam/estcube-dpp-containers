import os
from celery import Celery

env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis_scilab://localhost:6383'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis_scilab://localhost:6383')


celery= Celery('Scilab_tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)
