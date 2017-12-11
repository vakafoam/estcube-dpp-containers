FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev libpq-dev python3-dev libfreetype6-dev libxft-dev

ENV CELERY_BROKER_URL redis://redis_r:6379/0
ENV CELERY_RESULT_BACKEND redis://redis_r:6379/0
ENV C_FORCE_ROOT true


# copy source code
COPY . /worker_R
WORKDIR /worker_R

# install requirements
RUN sudo pip3 install -r requirements.txt
RUN apt-get -y install r-base
RUN sudo su - -c "R -e \"install.packages('DBI', repos = 'http://cran.rstudio.com/')\""
RUN sudo su - -c "R -e \"install.packages('RPostgreSQL', repos = 'http://cran.rstudio.com/')\""
# RUN sudo su - -c "R -e \"install.packages('ggplot2', repos = 'http://cran.rstudio.com/')\""
RUN sudo apt-get install --yes r-cran-ggplot2


# RUN sudo apt-get install --yes python3-numpy python3-scipy python3-matplotlib


# run the worker
ENTRYPOINT celery -A tasks worker --loglevel=info
