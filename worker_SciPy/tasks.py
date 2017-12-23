import os
import time
from celery import Celery
import subprocess as sub
from taskModel import Task


env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis_scipy://localhost:6379'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis_scipy://localhost:6379')


celery= Celery('tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

# Celery task to run SciPy script
@celery.task(name='SciPy_broker.py_script', trail=True)
def py_script(task):
    # save output and Error in separate files
    folder = task.getFolder()
    os.chdir(folder)
    command = ("python3 {0}".format(task.name))
    out = run (command, task.outName, task.logName)
    return out

# Run separate process from cmd
def run(cmd, outFile, logFile):
    out = open(outFile, "w+")
    log = open(logFile, "w+")
    try:
        sub.call(cmd, stdout=out, stderr=log, shell=True)
        #return out
    except sub.CalledProcessError as cpe:
        return cpe.output
    finally:
        out.close()
        log.close()
