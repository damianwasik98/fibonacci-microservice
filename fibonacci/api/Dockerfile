FROM python:3.7

WORKDIR /api
COPY . .

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["api:app", "--host", "0.0.0.0", "--port", "8000"]
ENTRYPOINT ["uvicorn"]