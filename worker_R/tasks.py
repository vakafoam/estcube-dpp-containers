import os
import time
from celery import Celery
import subprocess as sub
from taskModel import Task


env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis_r://localhost:6380'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis_r://localhost:6380')


celery= Celery('R_tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

# Celery task to run R script
@celery.task(name='R_broker.R_script', trail=True)
def r_script(task):
    # save output and Error in separate files
    folder = task.getFolder()
    os.chdir(folder)
    command = ("Rscript --no-save --no-restore --verbose {0}.R > {0}.R.out 2> {0}.R.log".format(task.timestamp))
    out = run (command)
    return out

# Run separate process from cmd
def run(cmd):
    try:
        out = sub.check_output(cmd, stderr=sub.STDOUT, shell=True)
        return out
    except sub.CalledProcessError as cpe:
        return cpe.output
