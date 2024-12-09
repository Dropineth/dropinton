# from telegram import Update
# from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler

token = '7758145376:AAH3u98Ojty8Szu0xkDtGmi1sFRUXtXOx8w'

def start(update: Update, context: CallbackContext):
    # context.bot.send_message(chat_id=update.effective_chat.id, text="Let's start!")
    # context.bot.send_message(text="Hello world from robot", chat_id=-1002404363413)
    # text = `🎮 Join me in Bull's Back: Earn, and Win! 🏆\n🚀 Let's play and earn together!`
    # text = "🚀【Title】\n🎯【Sub Title】\n\n 🕗时间：November 07, 20:00 UTC+8 \n 🌐Host：Web3Labs \n 🤝Co-Organizer: ABC,\n 🔗Link: \n Come on, Bala Bala"
    chatID = update.effective_chat.id
    text = "🎉Welcome to Drpoin! \n\n🌵DROPIN｜🌍Gaming Reforestation｜🌳Fostering climate action \n\n🔥Share this game with your friends to play and earn together."

    keyboard = [
        [
            InlineKeyboardButton("PLAY GAME", url="https://t.me/dropin_lotto_bot?startapp"),
        ]
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard) 
    
    context.bot.send_photo(chat_id=chatID, photo=open("banner.png","rb"), caption=text,  reply_markup=reply_markup)
           
    # 或
    # update.message.reply_text("Let's start!")

def keyboard_callback(update: Update, context: CallbackContext): 
    query = update.callback_query 
    query.answer() 
    query.edit_message_text(text=f"Selected option: {query.data}") 
    
    
if __name__ == '__main__':
    updater = Updater(token=token, use_context=True) 
    start_handler = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_handler) 
    # updater.dispatcher.add_handler(CallbackQueryHandler(keyboard_callback)) 
    updater.start_polling() 
    updater.idle() 
