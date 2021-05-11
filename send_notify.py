import telebot


def send(user_id, note):
    bot = telebot.TeleBot('')
    bot.send_message(user_id, note)
    bot.send_message(user_id, note)
    bot.send_message(user_id, note)
