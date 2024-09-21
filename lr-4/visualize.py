import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

MALE_UA = 'Чоловіча'
FEMALE_UA = 'Жіноча'

def calculate_age(birthdate):
    return datetime.now().year - pd.to_datetime(birthdate).year

try:
    df = pd.read_csv('employees.csv')
    print("Ok, файл CSV успішно відкрито!")
except FileNotFoundError:
    print("Помилка: файл CSV не знайдено.")
    exit()

df['Вік'] = df['Дата народження'].apply(calculate_age)

print(df['Стать'].unique())

gender_counts = df['Стать'].value_counts()
print(f"Кількість чоловіків: {gender_counts.get(MALE_UA, 0)}")
print(f"Кількість жінок: {gender_counts.get(FEMALE_UA, 0)}")

gender_counts.plot(kind='bar', title="Кількість співробітників за статтю", color=['blue', 'pink'])
plt.ylabel("Кількість")
plt.savefig('gender_distribution.png')
plt.close()

age_categories = {
    'younger_18': df[df['Вік'] < 18],
    '18-45': df[(df['Вік'] >= 18) & (df['Вік'] <= 45)],
    '45-70': df[(df['Вік'] > 45) & (df['Вік'] <= 70)],
    'older_70': df[df['Вік'] > 70]
}

age_category_counts = {key: len(value) for key, value in age_categories.items()}
print("Кількість співробітників за віковими категоріями:")
for category, count in age_category_counts.items():
    print(f"{category}: {count}")

plt.bar(age_category_counts.keys(), age_category_counts.values(), color='green')
plt.title("Кількість співробітників за віковими категоріями")
plt.ylabel("Кількість")
plt.savefig('age_distribution.png')
plt.close()

gender_age_category_counts = {
    category: {
        'male': len(data[data['Стать'] == MALE_UA]),
        'female': len(data[data['Стать'] == FEMALE_UA])
    }
    for category, data in age_categories.items()
}

print("Кількість чоловіків і жінок у кожній віковій категорії:")
for category, counts in gender_age_category_counts.items():
    print(f"{category}: чоловіків - {counts['male']}, жінок - {counts['female']}")

for category, counts in gender_age_category_counts.items():
    plt.bar(['male', 'female'], [counts['male'], counts['female']], color=['blue', 'pink'])
    plt.title(f"Статевий розподіл у категорії {category}")
    plt.ylabel("Кількість")
    plt.savefig(f'gender_distribution_{category}.png')
    plt.close()
