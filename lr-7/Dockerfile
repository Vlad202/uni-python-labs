FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY db.py db.py
COPY fake.py fake.py

CMD ["python", "/app/db.py", "&&", "python", "/app/fake.py"]
