FROM python:3.7
WORKDIR /ingest
COPY . .

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

ENTRYPOINT ["python", "ingest.py"]