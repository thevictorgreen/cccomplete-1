FROM python:3.6.5-slim

WORKDIR /src

COPY ./src /src

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "main.py"]
