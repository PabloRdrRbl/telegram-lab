#
#
# Basic Telegram's bot example following:
# [https://github.com/python-telegram-bot/python-telegram
# -bot/wiki/Extensions-–-Your-first-Bot]
#


from telegram.ext import CommandHandler, MessageHandler, Updater
from telegram.ext import Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging

# Logging configuration
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
                            %(message)s', level=logging.INFO)

# Create an Updater object
updater = Updater(token='149523184:AAE34JHtb7cVYclzi5812Barw7pkO979GqM')

dispatcher = updater.dispatcher


def start(bot, update):
    """
    Process an specific type of update and sends a message.
    """
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(bot, update):
    """
    Returns all the non-command messages it receives.
    """
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=update.message.text)

echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answerInlineQuery(update.inline_query.id, results)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler([Filters.command], unknown)
dispatcher.add_handler(unknown_handler)

# Start the bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
