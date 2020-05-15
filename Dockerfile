FROM ubuntu:16.04

RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt -y update
RUN apt -y install python3.7
RUN apt -y install python3-pip
COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]