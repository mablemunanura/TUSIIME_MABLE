from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

TOKEN : Final = '7999835293:AAGBNBqNk7OA8kh9qFUEFgjJYf_Eyr2Dcoc'
BOT_USERNAME :Final = '@MableTusiimeBot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, thank you for chatting with me.')

#Responses
def handle_response(text:str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am doing well, thanks for asking.'
    
    if 'bye' in processed:
        return 'Bye, enjoy your day.'

    messages = [
        "You need 8 hours of sleep daily",
        "Keep hydrating",
        "Jesus loves you",
        "You are doing great",
        "I love you",
        "Practice makes progress",
        "It is well with my soul",
        "You're cool",
        "John 3:16 and 1 John 3:16"
    ]

    return random.choice(messages)

async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    text:str = update.message.text
    response:str = handle_response(text)

    await update.message.reply_text(response)

if __name__ == "__main__":
    print('Starting bot.....')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start',start_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print('Polling.....')
    app.run_polling(poll_interval=5)
