FROM python:3.11-slim

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY 11_dumanskyi.py .

CMD ["python", "11_dumanskyi.py"]
