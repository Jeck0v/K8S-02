FROM python:3.9-slim

WORKDIR /app

RUN apt update && apt install -y curl

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]