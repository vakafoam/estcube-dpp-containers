FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev libpq-dev python3-dev libfreetype6-dev libxft-dev

ENV CELERY_BROKER_URL redis://redis_scipy:6379/0
ENV CELERY_RESULT_BACKEND redis://redis_scipy:6379/0
ENV C_FORCE_ROOT true


# copy source code
COPY . /worker_SciPy
WORKDIR /worker_SciPy

# install requirements
RUN sudo pip3 install -r requirements.txt
# RUN pip3 install --user numpy
# RUN pip3 install --user scipy
# RUN pip3 install --user matplotlib
# RUN pip3 install --user psycopg2
# RUN pip3 install numpy scipy matplotlib psycopg2

RUN sudo apt-get install --yes python3-numpy python3-scipy python3-matplotlib
# RUN DEBIAN_FRONTEND="noninteractive" sudo apt-get install python3-numpy
# RUN DEBIAN_FRONTEND="noninteractive" sudo apt-get install python3-scipy
# RUN DEBIAN_FRONTEND="noninteractive" sudo apt-get install python3-matplotlib

# run the worker
#ENTRYPOINT ['celery']
#CMD ['-A','tasks', 'worker','--loglevel=info']
ENTRYPOINT celery -A tasks worker --loglevel=info
