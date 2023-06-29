from googletrans import Translator
from telegram.ext import CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Inglés a Español", callback_data='en-es'),
            InlineKeyboardButton("Español a Inglés", callback_data='es-en'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = f'¡Bienvenido a mi bot de traducción! Estoy aquí para ayudarte a traducir textos.\n\nPor favor elige un Idioma:'
    update.message.reply_text(text, reply_markup=reply_markup)

def handle_callback_query(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    data = query.data
    if data == 'en-es':
        context.user_data['translation_option'] = 'en-es'
        query.edit_message_text('Seleccionaste: Inglés a Español')
    elif data == 'es-en':
        context.user_data['translation_option'] = 'es-en'
        query.edit_message_text('Seleccionaste: Español a Inglés')

def handle_text(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    translator = Translator()
    translation_option = context.user_data.get('translation_option', 'en-es')
    src, dest = translation_option.split('-')
    translated_text = translator.translate(text, src=src, dest=dest).text
    update.message.reply_text(translated_text)

