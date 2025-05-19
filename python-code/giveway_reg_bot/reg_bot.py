import logging
import sqlite3
import csv
from io import StringIO
from flask import Flask, request
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
    InputFile,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

import config

# States
FIO, PHONE = range(2)

# Constants
ADMIN_ID = 668618297
DATABASE_NAME = "event_users.db"
USERS_TABLE = "users"

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask app
app = Flask(__name__)

def create_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {USERS_TABLE} (
                id INTEGER,
                order_number INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                username TEXT,
                phone TEXT,
                reg_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_user.id
    username = update.effective_user.username

    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        if cursor.fetchone():
            await update.message.reply_text("✅ Siz allaqachon ro'yxatdan o'tgansiz!")
            return ConversationHandler.END

    await update.message.reply_text("👋 Salom! Ro'yxatdan o'tish uchun ism-familiyangizni yuboring:")
    return FIO


async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['full_name'] = update.message.text

    reply_keyboard = [[KeyboardButton("📱 Raqamni yuborish", request_contact=True)]]
    await update.message.reply_text(
        "📞 Telefon raqamingizni yuboring:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    return PHONE


async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    user_id = user.id
    username = user.username
    phone = update.message.contact.phone_number if update.message.contact else update.message.text
    full_name = context.user_data['full_name']

    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute(f"""
        INSERT INTO {USERS_TABLE} (id, full_name, username, phone)
        VALUES (?, ?, ?, ?)
        """, (user_id, full_name, username, phone))
        cursor = conn.execute("SELECT order_number FROM users WHERE id = ?", (user_id,))
        order_number = cursor.fetchone()[0]

    await update.message.reply_text(
        f"🎉 Siz muvaffaqiyatli ro'yxatdan o'tdingiz!\nSizning tartib raqamingiz: <b>{order_number}</b>",
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="HTML"
    )
    return ConversationHandler.END


async def export_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Sizda ruxsat yo‘q.")
        return

    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, full_name, username, phone, reg_time FROM {USERS_TABLE}")
        users = cursor.fetchall()

    if not users:
        await update.message.reply_text("🗂 Hali foydalanuvchilar yo‘q.")
        return

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["#️⃣ Telegram ID", "Raqam", "Ism", "Username", "Telefon", "Ro'yxat vaqti"])
    for row in users:
        writer.writerow(row)

    output.seek(0)
    await update.message.reply_document(
        document=InputFile(output, filename="bot_leads.csv"),
        caption="📋 Ro'yxat eksport qilindi."
    )


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("❌ Bekor qilindi.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = Update.de_json(json_str, app.bot)
    app.dispatcher.process_update(update)
    return 'OK'


def main():
    create_db()
    app = ApplicationBuilder().token(config.token).build()

    # Set the webhook for Telegram
    webhook_url = "https://ваш-домен.com/webhook"
    app.bot.set_webhook(url=webhook_url)

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            FIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            PHONE: [
                MessageHandler(filters.CONTACT, get_phone),
                MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("export", export_users))

    app.run_polling()

if __name__ == "__main__":
    main()
