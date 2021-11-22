FROM python:3.9-slim

RUN apt-get update

WORKDIR /crypto

COPY . /crypto

RUN pip install poetry

RUN poetry export -f requirements.txt --output requirements.txt

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]