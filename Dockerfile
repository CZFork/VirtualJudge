FROM ubuntu:18.04

MAINTAINER xudian.cn@gmail.com

ENV VJ_ENV production



ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#COPY deploy/sources.list /etc/apt/

RUN mkdir -p /public
RUN chmod a+x /public
VOLUME /public

ADD . /app
WORKDIR /app

RUN apt update
RUN apt install -y python3 python3-dev python3-pip supervisor git
RUN pip3 install -r /app/requirements.txt
CMD bash /app/deploy/entrypoint.sh
