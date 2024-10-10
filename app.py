from flask import Flask, request
import os
import telebot

TELEGRAM_TOKEN = os.environ.get('7245109449:AAFwxXVauolRKUOnDjxdgAYJfCu3E3zhKZY')  # Получите токен из переменной окружения
bot = telebot.TeleBot(TELEGRAM_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Flower Shop!"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    bot.process_new_updates([telebot.types.Update.de_json(update)])
    return '', 200  # Возврат пустого ответа с кодом 200

@app.route('/set_webhook', methods=['GET'])
def set_webhook():
    webhook_url = f"https://{request.host}/webhook"
    bot.remove_webhook()  # Удалите старый вебхук, если есть
    bot.set_webhook(url=webhook_url)  # Установите новый вебхук
    return f"Webhook set to {webhook_url}", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
