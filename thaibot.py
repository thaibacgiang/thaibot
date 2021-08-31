from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
def tt(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chào{update.effective_user.full_name}! lượng tiêu thụ của bạn là: 1000w ')

def cs(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chào {update.effective_user.full_name}! Công suất tiêu thụ của bạn là: ')

def da(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chào {update.effective_user.full_name}! Điện áp của bạn là: Đói bụng')

def dd(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chào {update.effective_user.full_name}! Dòng điện của bạn là: Hơi yếu')





updater = Updater('1952032450:AAHC0d57JtHwX9c9OTBLE-0CiJaT3BprjGU')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('tt', tt))
updater.dispatcher.add_handler(CommandHandler('dd', dd))
updater.dispatcher.add_handler(CommandHandler('cs', cs))
updater.dispatcher.add_handler(CommandHandler('da', da))

updater.start_polling()
updater.idle()