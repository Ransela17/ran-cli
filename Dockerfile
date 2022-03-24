FROM python:3.8-slim

RUN apt-get update \
    && apt-get install -y git

ADD . / 

#RUN mkdir  -p /home/ran_cli
#WORKDIR /home/ran_cli

# /home/ran_cli/ran-cli

RUN pip3 install .

CMD ["ran"]