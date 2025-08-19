from flask import Flask, request
import telebot
import os

# Environment’dan TOKEN olish
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("❌ TOKEN topilmadi! Render Dashboard > Environment > TOKEN ni tekshiring")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("🚗 Авто о/с шарт расмийлаштириш")
    btn2 = telebot.types.KeyboardButton("🎁 Авто хадя шарт расмийлаштириш")
    btn3 = telebot.types.KeyboardButton("🏠 Квартира о/с шарт расмийлаштириш")
    btn4 = telebot.types.KeyboardButton("🏢 Нотариал тасдиқ")
    btn5 = telebot.types.KeyboardButton("📄 Ариза топшириш")

    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4, btn5)

    bot.send_message(
        message.chat.id,
        "Assalomu alaykum! Qaysi xizmat kerak?",
        reply_markup=markup
    )

# 🚗 Автомашина шартнома
@bot.message_handler(func=lambda m: m.text == "🚗 Авто о/с шарт расмийлаштириш")
def avtomashina(message):
    bot.send_message(message.chat.id,
    """🚗 Автомашина олди сотди шартномаси учун керак бўлган хужжатлар:
1. Шахсий ҳужжатлар
2. Транспорт воситаси қайд гувоҳномаси
3. Мулкдорларнинг розилиги (агар умумий бўлса)
4. Мерос ҳужжатлари (агар мерос бўлса)
5. Ишончнома (агар вакил орқали бўлса)
👉 Batafsil ma'lumot: +998-93-781-43-50"""
    )

# 🎁 Авто хадя шартнома
@bot.message_handler(func=lambda m: m.text == "🎁 Авто хадя шарт расмийлаштириш")
def avto_hadya(message):
    bot.send_message(message.chat.id,
    """🎁 Автомашина хадя шартномаси учун керак бўлган хужжатлар:
1. Шахсий ҳужжатлар
2. Транспорт воситаси қайд гувоҳномаси
3. Мулкдорларнинг розилиги (агар умумий бўлса)
4. Мерос ҳужжатлари (агар мерос бўлса)
5. Ишончнома (агар вакил орқали бўлса)
👉 Batafsil ma'lumot: +998-93-781-43-50"""
    )

# 🏠 Квартира шартнома
@bot.message_handler(func=lambda m: m.text == "🏠 Квартира о/с шарт расмийлаштириш")
def uyjoy(message):
    bot.send_message(message.chat.id,
    """🏠 Квартира олди-сотди шартномаси учун керак бўлган хужжатлар:
1. Шахсий ҳужжатлар
2. Мулк ҳуқуқини тасдиқловчи ҳужжат
3. Мулкдорларнинг розилиги (агар умумий бўлса)
4. Хусусийлаштириш ҳужжатлари
5. Ишончнома (агар вакил орқали бўлса)
👉 Batafsil ma'lumot: +998-93-781-43-50"""
    )

# 🏢 Нотариал тасдиқ
@bot.message_handler(func=lambda m: m.text == "🏢 Нотариал тасдиқ")
def notarial(message):
    bot.send_message(message.chat.id,
    """🏢 Нотариал тасдиқ учун керак бўлади:
1. Ариза ёзилган шакл
2. Шахсий ҳужжатлар
3. Ишончнома (агар вакил орқали бўлса)
👉 Batafsil ma'lumot: +998-93-781-43-50"""
    )

# 📄 Ариза топшириш
@bot.message_handler(func=lambda m: m.text == "📄 Ариза топшириш")
def ariza(message):
    bot.send_message(message.chat.id,
    """📄 Ариза топшириш учун:
1. Ариза шакли тўлдирилган бўлиши
2. Паспорт асли
3. Қўшимча ҳужжатлар (агар талаб этилса)
👉 Batafsil ma'lumot: +998-93-781-43-50"""
    )

# Default javob
@bot.message_handler(func=lambda m: True)
def default(message):
    bot.send_message(message.chat.id, "❗ Iltimos, pastdagi menyulardan birini tanlang!")

# Webhook route
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# Flask serverni ishga tushirish
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
