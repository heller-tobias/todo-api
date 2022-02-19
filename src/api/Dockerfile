FROM python:3.7-buster

RUN pip install --upgrade pip

RUN apt update \
    && apt install -y apt-utils gcc g++ 

ADD ./requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip install -r requirements.txt

COPY . /api

EXPOSE 5001

CMD python ./server.py