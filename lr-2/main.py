from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text, lang):
    try:
        translation = translator.translate(text, dest=CodeLang(lang))
        return translation.text
    except Exception as e:
        return f"Помилка перекладу тексту: {str(e)}"

def LangDetect(text):
    try:
        detection = translator.detect(text)
        return {
            "language": LangName(detection.lang),
            "confidence": detection.confidence
        }
    except Exception as e:
        return f"Помилка знаходження мови: {str(e)}"

def CodeLang(lang):
    lang = lang.lower()
    if lang in LANGUAGES:
        return lang
    else:
        for code, name in LANGUAGES.items():
            if name.lower() == lang:
                return code
        return f"Невідома мова: {lang}"

def LangName(code):
    return LANGUAGES.get(code, f"Невідомий код мови: {code}")

def main():
    text = input("Введіть текст для перекладу: ")
    
    detected_lang = LangDetect(text)
    print(f"Виявлена мова: {detected_lang['language']} (впевненість: {detected_lang['confidence']})")
    
    target_lang = input("Введіть мову, на яку потрібно перекласти текст (назва або код мови): ")
    
    translated_text = TransLate(text, target_lang)
    print(f"Переклад: {translated_text}")
    
    lang_info = LangName(CodeLang(target_lang))
    print(f"Інформація про мову: {lang_info}")

if __name__ == "__main__":
    main()
