FROM python:3.12

WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src /src

COPY ./tests /tests

CMD ["python", "main.py"]
