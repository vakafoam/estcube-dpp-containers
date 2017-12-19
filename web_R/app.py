from __future__ import absolute_import, unicode_literals
import os
from flask import Flask, request, redirect, url_for, jsonify, json
from flask import flash, make_response, request, current_app
from flask import url_for
import time
from datetime import timedelta
from taskModel import Task
from functools import update_wrapper

from worker import celery
from celery.result import AsyncResult
import celery.states as states
import time


env=os.environ
app = Flask(__name__)
CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'R'])

# Crossdomain decorator for access - control - allow - origin
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/add/<int:param1>/<int:param2>')
def add(param1,param2):
    # task = celery.send_task('mytasks.add', args=[param1, param2], kwargs={})
    # id = task.id
    # res = celery.AsyncResult(id)
    # while res.state == states.PENDING:
    #     time.sleep(2)
    #     res = celery.AsyncResult(id)
    # return str(res.result)

    result = sendTask(args=[param1,param2])
    return result.get()

def sendTask(param1,param2):
    task = celery.send_task('mytasks.add', args=[param1, param2], kwargs={})
    id = task.id
    res = celery.AsyncResult(id)
    while res.state == states.PENDING:
        time.sleep(2)
        res = celery.AsyncResult(id)
    return str(res.result)

#### Receive script file when uploaded, save with unique name
     ## Route for the back test without GUI
@app.route('/task', methods=['GET', 'POST'])
@crossdomain(origin='*') # this is for access-control-allow-origin
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            task = Task("R", "R")
            file.save(task.getScriptPath())
            #### Sending script to Celery worker
            r = r_process(task)
            return 'File ' + file.filename + ' was processed successfully' + str(task.result)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

    ## Route for the GUI
@app.route('/', methods=['POST'])
@crossdomain(origin='*') # this is for access-control-allow-origin
def frontend_connect():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            task = Task("R", "R")
            file.save(task.getScriptPath())
            #### Sending script to Celery worker
            r = r_process(task)
            return jsonify(task.result)

# Send script for Celery execution
def r_process(t):
    task = celery.send_task('R_broker.R_script', args=[t], kwargs={})
    id = task.id
    t.setTaskID(id)
    handleResults(t)

def handleResults(task):
    res = AsyncResult(task.getTaskID(), app = celery)
    while (1):
        if (res.ready()):
            task.readLog()
            task.readOut()
            task.readImage()
            result = jsonify(task.result)
            # sendResult(result)
            break
        time.sleep(0.3)

if __name__ == '__main__':
    app.run(debug=env.get('DEBUG',True),
            port=int(env.get('PORT',5000)),
            host=env.get('HOST','0.0.0.0'),
            threaded=True
    )
