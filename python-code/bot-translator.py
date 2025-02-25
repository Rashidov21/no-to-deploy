# pip install pyTelegramBotAPI
import telebot
from googletrans import Translator

bot = telebot.TeleBot("YOUR TOKEN", parse_mode=None)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
        f"<b>{message.from_user.first_name} {message.from_user.last_name} - Salom !</>",
                     parse_mode="html")

@bot.message_handler(content_types=['text'])
def all_message(message):
    translated = translator.translate(message.text, dest='ru', src='uz')
    bot.send_message(message.chat.id, translated.text)
bot.infinity_polling()