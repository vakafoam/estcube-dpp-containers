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


@celery.task(name='mytasks.add')
def add(x, y):
    time.sleep(1) # lets sleep for a while before doing the gigantic addition task!
    return x + y

# Celery task to run SciPy script
@celery.task(name='R_broker.R_script', trail=True)
def r_script(task):
    # save output and Error in separate files
    # folder = task.folder
    folder = task.getFolder()
    os.chdir(folder)
    # command = ("python3 {0}".format(task.name))
    command = ("Rscript --no-save --no-restore --verbose {0}.R > {0}.R.out 2> {0}.R.log".format(task.timestamp))
    # out = run (command, task.outName, task.logName)
    out = run (command)
    return out

# Run separate process from cmd
def run(cmd):
    # out = open(outFile, "w+")
    # log = open(logFile, "w+")
    # try:
    #     sub.call(cmd, stdout=out, stderr=log, shell=True)
    #     #return out
    # except sub.CalledProcessError as cpe:
    #     return cpe.output
    # finally:
    #     out.close()
    #     log.close()
    try:
        out = sub.check_output(cmd, stderr=sub.STDOUT)
        return out
    except sub.CalledProcessError as cpe:
        return cpe.output
