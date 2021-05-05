FROM python:3.7
WORKDIR /generator
COPY . .

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["-d", "0.5", "-s", "iterative", "-env", ".env"]
ENTRYPOINT ["python", "generator.py"]
