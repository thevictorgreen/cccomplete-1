FROM python:3.6.5-slim

WORKDIR /src

ADD ./src /src

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "main.py"]
