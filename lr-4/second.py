import pandas as pd
from openpyxl import Workbook
from datetime import datetime
from openpyxl.utils.dataframe import dataframe_to_rows

def calculate_age(birthdate):
    return datetime.now().year - pd.to_datetime(birthdate).year

try:
    df = pd.read_csv('employees.csv')
    print("Ok, файл CSV успішно відкрито!")
except FileNotFoundError:
    print("Помилка: файл CSV не знайдено.")
    exit()

df['Вік'] = df['Дата народження'].apply(calculate_age)

wb = Workbook()
ws_all = wb.active
ws_all.title = "all"

ws_all.append(['№', 'Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

for idx, r in enumerate(dataframe_to_rows(df, index=False, header=False), 1):
    ws_all.append([idx] + r)

age_categories = {
    'younger_18': df[df['Вік'] < 18],
    '18-45': df[(df['Вік'] >= 18) & (df['Вік'] <= 45)],
    '45-70': df[(df['Вік'] > 45) & (df['Вік'] <= 70)],
    'older_70': df[df['Вік'] > 70]
}

for category, data in age_categories.items():
    ws = wb.create_sheet(title=category)
    ws.append(['№', 'Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік'])
    for idx, r in enumerate(dataframe_to_rows(data, index=False, header=False), 1):
        ws.append([idx] + r[:6])

try:
    wb.save('employees.xlsx')
    print("Ok, XLSX файл успішно створено!")
except Exception as e:
    print(f"Неможливо створити XLSX файл. Помилка: {e}")
