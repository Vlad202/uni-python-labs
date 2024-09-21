import string

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

            first_sentence = text.split('.')[0]
            print(f"Перше речення: {first_sentence.strip()}")

            translator = str.maketrans('', '', string.punctuation)
            words = text.translate(translator).split()

            ukrainian_words = [word for word in words if all('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in word)]
            english_words = [word for word in words if all('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in word)]

            ukrainian_words_sorted = sorted(ukrainian_words, key=lambda x: x.lower())
            english_words_sorted = sorted(english_words, key=lambda x: x.lower())

            print("\nВідсортовані українські слова:")
            print(ukrainian_words_sorted)
            
            print("\nВідсортовані англійські слова:")
            print(english_words_sorted)

            total_words = len(words)
            print(f"\nКількість слів у тексті: {total_words}")

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка під час читання файлу: {e}")

file_path = 'text.txt'
read_first_sentence(file_path)
