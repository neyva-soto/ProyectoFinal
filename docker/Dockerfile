FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python3 -m playwright install --with-deps

CMD ["python3", "behave_parallel.py", "--features=job", "--generate_reports", "--executors=15"]
