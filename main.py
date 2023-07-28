import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler

import readWrite as rw

token = "6591688320:AAEBPbOC9yZjQAhg7QYBOAdeduh7rgb4Q6U"
poopEmoji = '\U0001F4A9'


logging.basicConfig(
    format='%(acstime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hola, me encargo de contar cacas. ¿Qué necesitas?")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text_caps)
    

"""

async def poop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if(update.message.text == poopEmoji):
        rw.add(update.message.from_user.first_name,update.message.date)
        """
        input = update.message.from_user.first_name + ":" + str(update.message.date.date())
        await context.bot.send_message(
            chat_id= update.effective_chat.id,
            text= input
        )
        """ 

async def count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= rw.count()
        )
    except:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= "no hay cagadas"
        )

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        rw.clear()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= "GRACIAS POR TIRAR DE LA CISTERNA"
        )
    except:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= "base de datos pendiente de revisión"
        )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Ni puta idea de lo que dices Hulio."
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    #start_handler = CommandHandler('start',start)
    #echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    #caps_handler = CommandHandler('caps',caps)

    poop_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), poop)
    count_handler = CommandHandler('count',count)
    clear_handler = CommandHandler('clear',clear)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    #application.add_handler(start_handler)
    #application.add_handler(echo_handler)
    #application.add_handler(caps_handler)

    application.add_handler(poop_handler)
    application.add_handler(count_handler)
    application.add_handler(clear_handler)
    application.add_handler(unknown_handler) # siempre el último en ser añadido

    

    application.run_polling()