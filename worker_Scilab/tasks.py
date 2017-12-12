import os
import time
from celery import Celery
import subprocess as sub
from taskModel import Task



env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis_scilab://localhost:6383'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis_scilab://localhost:6383')


celery= Celery('Silab_tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


@celery.task(name='mytasks.add')
def add(x, y):
    time.sleep(1) # lets sleep for a while before doing the gigantic addition task!
    return x + y

# Celery task to run SciPy script
@celery.task(name='Scilab_broker.Scilab_script', trail=True)
def sl_script(task):
    # save output and Error in separate files
    # folder = task.folder
    folder = task.getFolder()
    os.chdir(folder)
    command = ("../../scilab-6.0.0/bin/scilab-cli -f {0} -nb".format(task.name))
    # out = run (command, task.outName, task.logName)      
    out = run (command, task.getOutPath(), task.getLogPath())
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
