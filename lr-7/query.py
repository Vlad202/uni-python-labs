import psycopg2
from psycopg2 import sql

def fetch_data(query, params=None):
    cursor.execute(query, params)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    print("\n" + "-" * 60)
    print(f"{' | '.join(columns)}")
    print("-" * 60)
    for row in rows:
        print(" | ".join(str(col).ljust(15) for col in row))
    print("-" * 60)

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="rental_db",
    user="user",
    password="password",
    host="localhost",   # Замість 'localhost' вказано 'db'
    port="5432"
)
cursor = conn.cursor()

# Виведення структури та даних кожної таблиці
tables = ['Tenants', 'Premises', 'RentalAgreements']
for table in tables:
    print(f"\nТаблиця: {table}")
    cursor.execute(sql.SQL(f"SELECT * FROM {table}"))
    fetch_data(f"SELECT * FROM {table};")

# Виконання запитів з пункту 8
queries = [
    ("Орендарі, які орендують приміщення під склад", """
    SELECT t.company_name, t.manager_name, t.phone
    FROM Tenants t
    JOIN RentalAgreements r ON t.tenant_id = r.tenant_id
    WHERE r.purpose = 'склад'
    ORDER BY t.company_name;
    """),
    
    ("Загальна орендна плата за кожне приміщення", """
    SELECT p.premise_id, p.area * p.rent_cost AS total_rent
    FROM Premises p;
    """),
    
    ("Загальна площа приміщень за типом оздоблення", """
    SELECT decoration_type, SUM(area) AS total_area
    FROM Premises
    GROUP BY decoration_type;
    """),
    
    ("Кінцева дата дії кожного договору оренди", """
    SELECT agreement_id, start_date, start_date + INTERVAL '1 day' * duration_days AS end_date
    FROM RentalAgreements;
    """),
    
    ("Кількість приміщень за типом оздоблення та метою оренди", """
    SELECT p.decoration_type, r.purpose, COUNT(*) AS premises_count
    FROM Premises p
    JOIN RentalAgreements r ON p.premise_id = r.premise_id
    GROUP BY p.decoration_type, r.purpose;
    """),
]

# Виконання та форматований вивід запитів
for description, query in queries:
    print(f"\n{description}:")
    fetch_data(query)

cursor.close()
conn.close()
