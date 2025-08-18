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
    btn1 = telebot.types.KeyboardButton("🚗 Oldi-sotdi")
    btn2 = telebot.types.KeyboardButton("🏠 Kadastr")
    btn3 = telebot.types.KeyboardButton("🎁 Hadya")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Assalomu alaykum! Qaysi xizmat kerak?", reply_markup=markup)

# Tugmalar
@bot.message_handler(func=lambda m: True)
def answer(message):
    if message.text == "🚗 Avtomashina oldi-sotdi shartnomasi":
        bot.send_message(message.chat.id,
                         "🚗 Oldi-sotdi shartnomasi uchun kerakli bo'lgan hujjatlar:\n"
                         "- Taraflarning shaxsini tasdiqlovchi hujjatlar asli(pasport yoki uning o'rnini bosuvchi hujjatlar\n- Mulk egalarining nikoh guvohnomasi yoki nikoh shartnomasi\n- Transport vositasini qayd etish guvohnomasi(texnik pasport)\n"
                         "- Davlat boji: 500 000 so‘m\n"
                         "👉 Notarius: Dadajon aka")
    elif message.text == "🏠 Kadastr":
        bot.send_message(message.chat.id,
                         "🏠 Kadastr hujjati uchun kerak bo‘ladi:\n"
                         "- Pasport\n- Uy hujjatlari\n"
                         "- Davlat boji: 300 000 so‘m\n"
                         "👉 Notarius: Dadajon aka")
    elif message.text == "🎁 Hadya":
        bot.send_message(message.chat.id,
                         "🎁 Hadya hujjati uchun kerak bo‘ladi:\n"
                         "- Pasport\n- Hujjat nusxalari\n"
                         "- Davlat boji: 200 000 so‘m\n"
                         "👉 Notarius: Dadajon aka")
    else:
        bot.send_message(message.chat.id, "Iltimos, pastdagi menyularni tanglang! 🙂")

# Faqat BIR MARTA webhook route
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


