FROM python:3.10

WORKDIR /app
COPY app/ /app/

RUN pip install flask ddtrace

ENV DD_ENV=dev
ENV DD_SERVICE=demo-app
ENV DD_VERSION=1.0.0

CMD ["ddtrace-run", "python", "main.py"]
