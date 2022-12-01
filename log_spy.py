from telegram import Update
from telegram.ext import ContextTypes
# import aiofiles   # Не получилось создаваать файл динамически

def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('db.csv', 'a') as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')