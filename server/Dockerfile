FROM python:alpine
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]