import os
import json
from my_functions import check_number, translate_text

def read_or_create_data():
    file_name = "MyData.json"
    if os.path.exists(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                number = data.get("number")
                language = data.get("language", "uk")
                if not isinstance(number, int) or language not in ["uk", "en"]:
                    raise ValueError("Некоректні дані")
                return number, language
        except (json.JSONDecodeError, ValueError):
            print("Помилка читання файлу або некоректні дані.")

    number = int(input("Введіть ціле число n: "))
    language = input("Введіть мову інтерфейсу (uk/en): ").strip().lower()

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump({"number": number, "language": language}, file)
    print(f"Дані збережено в файл {file_name}")
    return None, None

def main():
    # Спроба прочитати дані або створити новий файл
    number, language = read_or_create_data()

    if number is not None:
        # українську за замовчуванням
        if language not in ["uk", "en"]:
            language = "uk"

        # Переклад
        lang_text = {
            "uk": {
                "language": "Мова: Українська",
                "number_message": "Ціле число n:",
                "result": check_number(number, "uk")
            },
            "en": {
                "language": "Language: English",
                "number_message": "The integer n:",
                "result": check_number(number, "en")
            }
        }

        # результат
        print(lang_text[language]["language"])
        print(f"{lang_text[language]['number_message']} {number}")
        print(lang_text[language]["result"])

if __name__ == "__main__":
    main()
