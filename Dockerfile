FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org Flask

EXPOSE 8080

ENV NAME World

CMD ["python", "app.py"]
