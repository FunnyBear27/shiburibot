import telebot


def send(user_id, note):
    bot = telebot.TeleBot('1602905794:AAFj2svXMQDKydWN6LETAkTJyAoZLP6XuXw')
    bot.send_message(user_id, note)
    bot.send_message(user_id, note)
    bot.send_message(user_id, note)
