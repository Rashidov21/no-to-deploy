from transliterate import get_available_language_codes
from transliterate import translit
# print(get_available_language_codes()) # all support languages akalar

en_text = "Brothers another mothers"
ru_text = translit(en_text, "ru")
print(ru_text)