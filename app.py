import os
from flask import Flask, request
import telebot

TOKEN = "8428773284:AAG0Kuiy2tDikoli-bZ66_Mn90GuVbgkZMw"
MASTER_ID = 7128354703
# اترك SERVER_URL فارغاً الآن، سنضعه بعد إنشاء الخدمة في Render
SERVER_URL = "" 

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    if SERVER_URL:'https://rbt-x-project.onrender.com'
        bot.remove_webhook()
        bot.set_webhook(url=f"{SERVER_URL}/{TOKEN}")
        return f"<h1>RBT-X: System Online</h1><p>Master {MASTER_ID} in control.</p>", 200
    return "<h1>RBT-X: Set SERVER_URL first!</h1>", 200

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    if message.from_user.id == MASTER_ID:
        bot.reply_to(message, "🚨 استجابة فورية: النظام يعمل يا Master Noor.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
