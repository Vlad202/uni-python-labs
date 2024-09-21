import csv
from faker import Faker
import random

fake = Faker(locale='uk_UA')

male_middle_names = [
    'Олександрович', 'Іванович', 'Петрович', 'Сергійович', 'Володимирович',
    'Миколайович', 'Андрійович', 'Дмитрович', 'Юрійович', 'Васильович',
    'Федорович', 'Ярославович', 'Григорович', 'Богданович', 'Євгенович',
    'Віталійович', 'Романович', 'Павлович', 'Леонідович', 'Вікторович'
]

female_middle_names = [
    'Олександрівна', 'Іванівна', 'Петрівна', 'Сергіївна', 'Володимирівна',
    'Миколаївна', 'Андріївна', 'Дмитрівна', 'Юріївна', 'Василівна',
    'Федорівна', 'Ярославівна', 'Григорівна', 'Богданівна', 'Євгенівна',
    'Віталіївна', 'Романівна', 'Павлівна', 'Леонідівна', 'Вікторівна'
]

gender_name = {
    'male': 'Чоловіча',
    'female': 'Жіноча'
}

male_percentage = 0.6
female_percentage = 0.4
total_records = 2000

def generate_employee():
    gender = random.choices(['male', 'female'], [male_percentage, female_percentage])[0]
    
    if gender == 'male':
        first_name = fake.first_name_male()
        middle_name = random.choice(male_middle_names)
    else:
        first_name = fake.first_name_female()
        middle_name = random.choice(female_middle_names)
    
    last_name = fake.last_name()
    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
    job = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [last_name, first_name, middle_name, gender_name[gender], birth_date, job, city, address, phone, email]

with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 
        'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'
    ])

    for _ in range(total_records):
        writer.writerow(generate_employee())

print("CSV файл успішно створено!")
