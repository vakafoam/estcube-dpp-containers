import os
import time
from celery import Celery
import subprocess as sub
from taskModel import Task



env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6379'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')


celery= Celery('tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


@celery.task(name='mytasks.add')
def add(x, y):
    time.sleep(1) # lets sleep for a while before doing the gigantic addition task!
    return x + y

# Celery task to run SciPy script
@celery.task(name='SciPy_broker.py_script', trail=True)
def py_script(task):                                        #TODO: replace task for timestamp
    # save output and Error in separate files
    # folder = task.folder                                    #TODO: getfolder from time
    folder = task.getFolder()
    os.chdir(folder)
    command = ("python3 {0}".format(task.name))              #TODO: get filename
    out = run (command, task.outName, task.logName)         #TODO: get out/log filenames
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
