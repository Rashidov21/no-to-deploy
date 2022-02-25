# -*- coding:utf-8 -*-
# pip install googletrans==3.1.0a0

from googletrans import Translator
import googletrans
translator = Translator()

text = input("Write here to translate .. \n :")
# lang = input("Select language \nRussian - ru\nUzbek - uz\n:")
translated = translator.translate(text,dest="hi", src='en')
print(translated.text)
# print(googletrans.LANGUAGES) #get all support languages
# print(translator.translate("Open", "ru"))