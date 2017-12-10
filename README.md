## estcube-dpp-containers
A first version of Data Processing Platform for ESTCube-2 space satellite. The application consists of the following Docker containers:
- GUI where a user can upload a script in R, NumPy/SciPy or Scilab and get results of its execution;
- 3 Python Flask backend servers, one for each platform (R, NumPy/SciPy, Scilab);
- 3 Celery workers, one for each platform;
- Redis message ques for Celery applications.

Starting the aplication:
```bash

docker-compose build
docker-compose up -d 	# -d means 'detached mode'

```

The GUI is the entry point for the user. It can be accessed by address: `http://your-dockermachine-ip:8262` in browser. After the page loads, you can upload a script for a corresponding processing engine and wait for its execution to see the results.

You can scale up the Celery workers by running `docker-compose scale <worker_[engine]>=5`. After that there will be 5 workers of a corresponding Engine, ready to execute incoming tasks. 