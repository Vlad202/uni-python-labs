def check_number(n, language):
    if n < 0:
        n = abs(n)

    n_half = n // 2
    is_even = n_half % 2 == 0
    ends_with_3 = n_half % 10 == 3

    # Переклади для повідомлень
    messages = {
        "uk": {
            "even": f"{n}/2={n_half}\nЧисло {n_half} є парним.",
            "odd": f"{n}/2={n_half}\nЧисло {n_half} не є парним.",
            "ends_with_3": f"Число {n_half} закінчується цифрою 3."
        },
        "en": {
            "even": f"{n}/2={n_half}\nThe number {n_half} is even.",
            "odd": f"{n}/2={n_half}\nThe number {n_half} is odd.",
            "ends_with_3": f"The number {n_half} ends with 3."
        }
    }

    if is_even:
        result = messages[language]["even"]
    else:
        result = messages[language]["odd"]

    if ends_with_3:
        result += f" {messages[language]['ends_with_3']}"

    return result

def translate_text(text, language):
    translations = {
        "uk": {"save": "Дані збережено", "error": "Помилка читання файлу"},
        "en": {"save": "Data saved", "error": "File reading error"}
    }
    return translations[language].get(text, text)
