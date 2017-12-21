FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev libpq-dev python3-dev libfreetype6-dev libxft-dev
RUN apt-get install --yes wget libX11-6 default-jdk

ENV CELERY_BROKER_URL redis://redis_scilab:6379/0
ENV CELERY_RESULT_BACKEND redis://redis_scilab:6379/0
ENV C_FORCE_ROOT true


# copy source code
COPY . /worker_Scilab
WORKDIR /worker_Scilab

# install requirements
RUN sudo pip3 install -r requirements.txt
RUN wget http://www.scilab.org/download/6.0.0/scilab-6.0.0.bin.linux-x86_64.tar.gz
RUN tar xzvf scilab-6.0.0.bin.linux-x86_64.tar.gz

# run the worker
ENTRYPOINT celery -A tasks worker --loglevel=info
