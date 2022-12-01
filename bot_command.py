from telegram import Update
from telegram.ext import ContextTypes
import datetime
from log_spy import *
from sympy import Symbol, collect

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Приветики, {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'/hi - привет\n/time - время до тысячных секунды\n\
/help - помощь\n/calc - калькулятор (пиши математические выражения)\n\
/express - запись суммы многочленов, введённых через пробел')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text[6::]
    await update.message.reply_text(f'Результат = {eval(msg)}')

async def express_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    sum = update.message.text[9::]
    sum = sum.replace('^', '**').replace('x', '*x').replace('=0', '')
    first = sum.split(' ')[0]
    second = sum.split(' ')[1]
    x = Symbol('x')
    result = str(collect(first + '+' + second, x))
    await update.message.reply_text(f'В результате получаем такой многочлен = {result}')
