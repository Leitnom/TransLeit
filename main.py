from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from chatbot import start, handle_callback_query, handle_text
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ['TELEGRAM_TOKEN']

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(handle_callback_query))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    
    updater.start_polling()
    
    print("Bot iniciado")
    updater.idle()

if __name__ == '__main__':
    main()
