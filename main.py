import telebot
from telebot import types
import datetime
from db_add import add
import socket


bot = telebot.TeleBot('1602905794:AAFj2svXMQDKydWN6LETAkTJyAoZLP6XuXw')
line = {}


@bot.message_handler(commands=["start"])
def start_msg(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Мои напоминания')
    itembtn2 = types.KeyboardButton('Создать новое напоминание')
    itembtn3 = types.KeyboardButton('Выйти')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)


@bot.message_handler(content_types='text')
def create_note(message):
    if message.text == 'Создать новое напоминание':
        send = bot.send_message(message.chat.id, "Введите, пожалуйста, дату и время напоминания в виде "
                                                 "день/месяц/год час:минута:секунда")
        bot.register_next_step_handler(send, date_time_input)


def date_time_input(message):
    global line
    try:
        d = datetime.datetime.strptime(message.text, "%d/%m/%Y %H:%M:%S")
        if d < datetime.datetime.now():
            8 / 0
        line['NoteDate'] = d
        send = bot.send_message(message.chat.id, 'Прекрасно! Введите, пожалуйста, текст напоминания')
        bot.register_next_step_handler(send, note_input)
    except ValueError:
        send = bot.send_message(message.chat.id, "Такой даты и времени не существует, попробуйте ещё раз")
        bot.register_next_step_handler(send, date_time_input)
    except ZeroDivisionError:
        send = bot.send_message(message.chat.id, "Это напоминание устарело, введите, пожалуйста, новое")
        bot.register_next_step_handler(send, date_time_input)


def note_input(message):
    global line
    note = message.text
    line['NoteText'] = note
    line['UserId'] = message.from_user.id
    bot.send_message(message.chat.id, "Готово, напоминание создано! Уведомление придёт Вам в указанное время")
    add(line)


if __name__ == '__main__':
    bot.infinity_polling()

# {
#    "content_type":"text",
#    "id":162,
#    "message_id":162,
#    "from_user":{
#       "id":368769335,
#       "is_bot":false,
#       "first_name":"Медведь",
#       "username":"hey_hey_hey_hey_hey",
#       "last_name":"Веселительный",
#       "language_code":"ru",
#       "can_join_groups":"None",
#       "can_read_all_group_messages":"None",
#       "supports_inline_queries":"None"
#    },
#    "date":1620498005,
#    "chat":{
#       "id":368769335,
#       "type":"private",
#       "title":"None",
#       "username":"hey_hey_hey_hey_hey",
#       "first_name":"Медведь",
#       "last_name":"Веселительный",
#       "photo":"None",
#       "bio":"None",
#       "description":"None",
#       "invite_link":"None",
#       "pinned_message":"None",
#       "permissions":"None",
#       "slow_mode_delay":"None",
#       "sticker_set_name":"None",
#       "can_set_sticker_set":"None",
#       "linked_chat_id":"None",
#       "location":"None"
#    },
#    "forward_from":"None",
#    "forward_from_chat":"None",
#    "forward_from_message_id":"None",
#    "forward_signature":"None",
#    "forward_sender_name":"None",
#    "forward_date":"None",
#    "reply_to_message":"None",
#    "edit_date":"None",
#    "media_group_id":"None",
#    "author_signature":"None",
#    "text":"Создать новое напоминание",
#    "entities":"None",
#    "caption_entities":"None",
#    "audio":"None",
#    "document":"None",
#    "photo":"None",
#    "sticker":"None",
#    "video":"None",
#    "video_note":"None",
#    "voice":"None",
#    "caption":"None",
#    "contact":"None",
#    "location":"None",
#    "venue":"None",
#    "animation":"None",
#    "dice":"None",
#    "new_chat_member":"None",
#    "new_chat_members":"None",
#    "left_chat_member":"None",
#    "new_chat_title":"None",
#    "new_chat_photo":"None",
#    "delete_chat_photo":"None",
#    "group_chat_created":"None",
#    "supergroup_chat_created":"None",
#    "channel_chat_created":"None",
#    "migrate_to_chat_id":"None",
#    "migrate_from_chat_id":"None",
#    "pinned_message":"None",
#    "invoice":"None",
#    "successful_payment":"None",
#    "connected_website":"None",
#    "reply_markup":"None",
#    "json":{
#       "message_id":162,
#       "from":{
#          "id":368769335,
#          "is_bot":false,
#          "first_name":"Медведь",
#          "last_name":"Веселительный",
#          "username":"hey_hey_hey_hey_hey",
#          "language_code":"ru"
#       },
#       "chat":{
#          "id":368769335,
#          "first_name":"Медведь",
#          "last_name":"Веселительный",
#          "username":"hey_hey_hey_hey_hey",
#          "type":"private"
#       },
#       "date":1620498005,
#       "text":"Создать новое напоминание"
#    }
# }