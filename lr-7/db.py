import psycopg2

# Функція для очікування доступності PostgreSQL
conn = psycopg2.connect(
    dbname="rental_db",
    user="user",
    password="password",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Tenants (
    tenant_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    manager_name VARCHAR(100),
    phone VARCHAR(15) CHECK (phone ~ '^\\+?\\d{1,15}$')
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Premises (
    premise_id SERIAL PRIMARY KEY,
    area DECIMAL(5, 2) NOT NULL CHECK (area > 0),
    rent_cost DECIMAL(10, 2) NOT NULL CHECK (rent_cost > 0),
    floor INTEGER NOT NULL CHECK (floor >= 0),
    phone_in_premise BOOLEAN DEFAULT FALSE,
    decoration_type VARCHAR(20) CHECK (decoration_type IN ('звичайне', 'поліпшене', 'євро'))
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS RentalAgreements (
    agreement_id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    duration_days INTEGER CHECK (duration_days > 0),
    purpose VARCHAR(20) CHECK (purpose IN ('офіс', 'кіоск', 'склад')),
    tenant_id INTEGER REFERENCES Tenants(tenant_id) ON DELETE CASCADE,
    premise_id INTEGER REFERENCES Premises(premise_id) ON DELETE CASCADE
);
""")

conn.commit()
cursor.close()
conn.close()
