FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir bandit

RUN pip install --no-cache-dir semgrep

RUN pip install --no-cache-dir safety

COPY . .

CMD ["python3", "app.py"]

EXPOSE 8001

