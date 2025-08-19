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
    btn1 = telebot.types.KeyboardButton("🚗 Автомашина олди сотди шартномаси расмилаштириш")
    btn2 = telebot.types.KeyboardButton("🚗 Автомашина хадйа шартномаси расмилаштириш")
    btn3 = telebot.types.KeyboardButton("🎁 Hadya")
    markup.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "Assalomu alaykum! Qaysi xizmat kerak?",
        reply_markup=markup
    )

# Avtomashina shartnomasi
@bot.message_handler(func=lambda m: m.text == "🚗 Автомашина олди сотди шартномаси расмилаштириш")
def avtomashina(message):
    bot.send_message(message.chat.id,
    """🚗 Автомашина олди сотди шартномаси расмилаштириш учун керак болган хужжатлар:
1. Тарафлар шахсини тасдиқловчи ҳужжатлар асли (паспорт ёки унинг ўрнини босувчи ҳужжатлар).
2. Транспорт воситасини қайд этиш гувоҳномаси.
3. Агарда умумий мулкни ташкил этса, мулкдорларнинг (эр-хотиннинг, меросхўрларнинг) розилиги 
   (никоҳ гувоҳномаси, никох шартномаси, никоҳ бекор қилинганлиги ҳақида гувоҳнома ёки бир тарафнинг ўлим гувохномаси).
4. Агар мулк меросга асосан тегишли бўлса, мерос гувоҳномасининг асли.
5. Вакилнинг ваколатларини тасдиқловчи ҳужжат (ишончнома).
6. Юридик шахслар учун қўшимча равишда:
   - ваколатли органининг ҳужжати (қарор, умумий мажлис баённомаси, кузатув кенгашининг қарори, буйруқ ва ҳоказо);
   - кузатув кенгашининг қарори тақдим этилган тақдирда автомототранспорт воситасининг қолдиқ баланс қиймати ҳақида юридик шахс раҳбари ва бош ҳисобчисининг имзоси қўйилган маълумотнома ҳамда юридик шахснинг соф активлари ҳақида маълумот;
   - вакилнинг ваколатларини тасдиқловчи ҳужжатлар (ишончнома, қарор ёки буйруқ).
   - тарафлар ўртасида ҳисоб-китоб қилинганлигини тасдиқловчи ҳужжат.

👉 Batafsil ma'lumot +998-93-781-43-50"""
    )

# Kadastr
@bot.message_handler(func=lambda m: m.text == "🚗 Автомашина хадйа шартномаси расмилаштириш")
def kadastr(message):
    bot.send_message(message.chat.id,
                    """🚗 Автомашина хадйа шартномаси расмилаштириш учун керак болган хужжатлар:
1. Тарафлар шахсини тасдиқловчи ҳужжатлар асли (паспорт ёки унинг ўрнини босувчи ҳужжатлар).
2. Транспорт воситасини қайд этиш гувоҳномаси.
3. Агарда умумий мулкни ташкил этса, мулкдорларнинг (эр-хотиннинг, меросхўрларнинг) розилиги 
   (никоҳ гувоҳномаси, никох шартномаси, никоҳ бекор қилинганлиги ҳақида гувоҳнома ёки бир тарафнинг ўлим гувохномаси).
4. Агар мулк меросга асосан тегишли бўлса, мерос гувоҳномасининг асли.
5. Вакилнинг ваколатларини тасдиқловчи ҳужжат (ишончнома).
6. Юридик шахслар учун қўшимча равишда:
   - ваколатли органининг ҳужжати (қарор, умумий мажлис баённомаси, кузатув кенгашининг қарори, буйруқ ва ҳоказо);
   - кузатув кенгашининг қарори тақдим этилган тақдирда автомототранспорт воситасининг қолдиқ баланс қиймати ҳақида юридик шахс раҳбари ва бош ҳисобчисининг имзоси қўйилган маълумотнома ҳамда юридик шахснинг соф активлари ҳақида маълумот;
   - вакилнинг ваколатларини тасдиқловчи ҳужжатлар (ишончнома, қарор ёки буйруқ).
   - тарафлар ўртасида ҳисоб-китоб қилинганлигини тасдиқловчи ҳужжат.

👉 Batafsil ma'lumot +998-93-781-43-50"""
    )
# Hadya
@bot.message_handler(func=lambda m: m.text == "🎁 Hadya")
def hadya(message):
    bot.send_message(message.chat.id,
                     "🎁 Hadya hujjati uchun kerak bo‘ladi:\n"
                     "- Pasport\n- Hujjat nusxalari\n"
                     "- Davlat boji: 200 000 so‘m\n"
                     "👉 Notarius: Dadajon aka")

# Default javob
@bot.message_handler(func=lambda m: True)
def default(message):
    bot.send_message(message.chat.id, "Iltimos, pastdagi menyularni tanlang!")

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

