import logging
from telegram import Update, CallbackQuery
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler

token = "6591688320:AAEBPbOC9yZjQAhg7QYBOAdeduh7rgb4Q6U"

logging.basicConfig(
    format='%(acstime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

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
    
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Ni puta idea de lo que dices Hulio."
    )

async def count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= "EPA"
    )
    print("____________________")
    print(CallbackQuery.message.chat_id)
    print("____________________")

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start',start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps',caps)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    count_handler = CommandHandler('count',count)

    application.add_handler(start_handler)
    #application.add_handler(echo_handler)
    #application.add_handler(caps_handler)
    application.add_handler(count_handler)
    application.add_handler(unknown_handler) # siempre el último en ser añadido

    application.run_polling()