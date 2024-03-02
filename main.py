# 1 - masala

# from collections import namedtuple
#
# info = namedtuple('Books', 'id name pages')
#
# books = [
#     (1, 'Harry Poter', 250),
#     (2, 'Soul', 100),
#     (3, 'Titanik', 300)
#
# ]
#
# for book in books:
#     bk = info(*books)
#     print(bk.id, bk.name, bk.pages)

#------------------------------------

from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7074263196:AAHaqkbUIw_MOJ1n99xKvcVuZ0MJwB7IQrs')

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    name = message.from_user.first_name
    print(message)
    bot.send_message(chat_id, f'Assalomu Alaykum {name}')

@bot.message_handler(content_types=['text'])
def text(message: Message):
    chat_id = message.chat.id
    text = message.text
    bot.copy_message(-4111398575, chat_id, message.message_id)

#2 - handler
@bot.message_handler(content_types=['photo'])
def photo(message: Message):
    chat_id = message.chat.id
    photo = message.photo
    bot.copy_message(-4111398575, chat_id, message.message_id)

#3 - handler
@bot.message_handler(content_types=['video'])
def video(message: Message):
    chat_id = message.chat.id
    video = message.video
    bot.copy_message(-4111398575, chat_id, message.message_id)

# 4 - handler
@bot.message_handler(content_types=['animation'])
def animation(message: Message):
    chat_id = message.chat.id
    animation = message.animation
    bot.copy_message(-4111398575, chat_id, message.message_id)

bot.polling()

#------------------------------------



