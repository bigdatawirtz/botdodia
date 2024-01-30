import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

# Authentication to manage the bot
import os
TOKEN = os.getenv('TOKEN')

if TOKEN==None:
    print('Lembra indicar a variable TOKEN')
    print('p.ex: docker run --rm -e TOKEN=o_teu_token telebot')
    exit(1)

# Show logs in terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# This function responds to start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Son un bot, dime algo!")

# This function responds to echo handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from taboas import *
async def table7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=taboa_do_7()) 

async def downloader(update, context):
    file = await context.bot.get_file(update.message.document)
    filename = update.message.document.file_name
    await file.download_to_drive(filename)

    answer = open('resposta.txt', "rb")
    await context.bot.send_document(chat_id=update.effective_chat.id, document=answer)



if __name__ == '__main__':
    # Start the application to operate the bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Handler to manage the start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Handler to manage text messages
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    table7_handler = CommandHandler('table7', table7)
    application.add_handler(table7_handler)


    application.add_handler(MessageHandler(filters.Document.ALL, downloader))

    # Keeps the application running
    application.run_polling()