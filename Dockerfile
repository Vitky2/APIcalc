FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir bandit

RUN pip install --no-cache-dir semgrep

CMD ["python3", "app.py"]

EXPOSE 8001

