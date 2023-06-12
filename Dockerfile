
FROM python:3.9

WORKDIR /root
ADD bark /root/bark

RUN pip install --no-cache-dir -r /root/bark/requirements.txt

WORKDIR /root/bark

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]

