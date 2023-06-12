#!/usr/bin/env python

# FROM python:3.8-slim-buster
FROM python:3.9

WORKDIR /root
ADD bark /root/bark
COPY bark/entry_point.sh root/bark/entry_point.sh

RUN pip install -r /root/bark/requirements.txt

WORKDIR /bark

CMD ["bash", "entry_point.sh"]

