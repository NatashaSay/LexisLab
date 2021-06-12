import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from django.conf import settings

from django.conf import settings

import requests

words = requests.get('http://127.0.0.1:8000/api/')
print(words.text)
print(words)

themes = requests.get('http://127.0.0.1:8000/themes/')
print(themes.text)
print(themes)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    
    update.message.reply_text('Hi!')


def help(update, context):
   
    update.message.reply_text('Help!')


def echo(update, context):
    
    update.message.reply_text(update.message.text)


def error(update, context):
    
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def get_words(update, context):

    update.message.reply_text(words)


def get_themes(update, context):

    update.message.reply_text(themes)


def main():
   
    updater = Updater(settings.TOKEN, use_context=True)

    
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("get_words", get_words))
    
    dp.add_handler(MessageHandler(Filters.text, echo))


    dp.add_error_handler(error)

    
    updater.start_polling()

    
    updater.idle()


if __name__ == '__main__':
    main()