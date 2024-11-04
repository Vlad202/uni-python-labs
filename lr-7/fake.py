import psycopg2
from datetime import date, timedelta

conn = psycopg2.connect(
    dbname="rental_db",
    user="user",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

tenants_data = [
    ("Alpha Co", "John Doe", "+123456789"),
    ("Beta LLC", "Jane Smith", "+198765432"),
    ("Gamma Inc", "Alice Brown", "+145678321"),
    ("Delta Ltd", "Bob White", "+123987654"),
    ("Epsilon SA", "Maria Green", "+192837465")
]
cursor.executemany("INSERT INTO Tenants (company_name, manager_name, phone) VALUES (%s, %s, %s);", tenants_data)

premises_data = [
    (50.5, 300.0, 1, False, "звичайне"),
    (60.0, 350.0, 1, True, "поліпшене"),
    (40.2, 250.0, 2, False, "євро"),
    (55.5, 320.0, 3, True, "звичайне"),
    (75.0, 400.0, 3, False, "поліпшене"),
    (80.0, 450.0, 4, True, "євро")
]
cursor.executemany("INSERT INTO Premises (area, rent_cost, floor, phone_in_premise, decoration_type) VALUES (%s, %s, %s, %s, %s);", premises_data)

rental_data = [
    (date.today(), 365, "офіс", 1, 1),
    (date.today() - timedelta(days=30), 180, "кіоск", 2, 2),
    (date.today() - timedelta(days=60), 90, "склад", 3, 3)
]
cursor.executemany("INSERT INTO RentalAgreements (start_date, duration_days, purpose, tenant_id, premise_id) VALUES (%s, %s, %s, %s, %s);", rental_data)

conn.commit()
cursor.close()
conn.close()
