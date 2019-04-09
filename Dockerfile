FROM ubuntu:18.04
RUN apt update
RUN apt upgrade -y
RUN apt install python3 -y
RUN apt install -y python3-pip
#RUN apt install git
RUN mkdir -p /home/root/course
COPY . /home/root/course/
WORKDIR /home/root/course/
RUN pip3 install -r req.txt
#RUN python3 manage.py runserver