#webhook heroku - this tutorial works on cloud. 
#   to run flask on local server
#       export FLASK_APP=tutorial6
#       flask run
#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots#vps
#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks
#https://python-telegram-bot.readthedocs.io/
#https://seminar.io/2018/09/03/building-serverless-telegram-bot/
#https://www.heroku.com/
from flask import Flask, render_template, request

import os
import telegram

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def webhook():
    bot = telegram.Bot(token=os.environ["YOURAPIKEY"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id     = update.effective_chat.id
        message_id  = update.message.message_id
        text        = update.message.text
        first_name  = update.effective_chat.first_name
        try:
            file_id = update.message.photo[-1].file_id
            newFile = bot.get_file(file_id)
            #newFile.download('test.jpg')
            # Reply with the same message
            #bot.sendMessage(chat_id=chat_id, text=f"test {bot.get_file(file_id)} {first_name}")
            bot.sendMessage(chat_id=chat_id, reply_to_message_id=message_id, text=newFile.file_path)
            #bot.send_photo(chat_id=chat_id, photo=newFile)
            return 'ok'
        except Exception:
            bot.sendMessage(chat_id=chat_id, text=f"只限圖片")
            return 'ok'
    return 'error'

def index():
    return webhook()
