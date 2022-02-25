# pip install transliterate
from transliterate import get_available_language_codes


from transliterate import translit

print(get_available_language_codes()) # all support languages akalar
en_text = "Mening yurtim"
ru_text = translit(en_text, "ru")
print(ru_text)