import telebot
import random
from telebot import types
import math
bot = telebot.TeleBot("6734050072:AAEWJ5wRWvnBd1B3GB_gPzkwHrFaIGoc36g")
@bot.message_handler(commands=["start"])
def w(message):
        bot.send_message(message.chat.id, "Новые показания света ")
        bot.register_next_step_handler(message, a)
    
def a(message):
    try:
        global x
        x = int(message.text)
        if len(str(x))==5:
            bot.send_message(message.chat.id, "Старые показания света ")
            bot.register_next_step_handler(message, b)
        else:
            w(message)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
        w(message)  # Возврат к функции w для повторного ввода

def b(message):
    try:
        global y
        y = int(message.text)
        if len(str(y))==5:
            bot.send_message(message.chat.id, "Новые показания воды ")
            bot.register_next_step_handler(message, с)
        else:
            a(message)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
        a(message)  # Возврат к функции w для повторного ввода

def с(message):
    try:
        global p
        p = int(message.text)
        if len(str(p))==3:
            bot.send_message(message.chat.id, "Старые показания воды ")
            bot.register_next_step_handler(message, j)
        else:
            b(message)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
        b(message)  # Возврат к функции w для повторного ввода

def j(message):
    try:
        global k
        k = int(message.text)
        if len(str(k))==3:
            bot.send_message(message.chat.id, "Квт ")
            bot.register_next_step_handler(message, m)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
        c(message)  # Возврат к функции w для повторного ввода

def m(message):
    try:
        global n
        n = int(message.text)
        bot.send_message(message.chat.id, "Кбм ")
        bot.register_next_step_handler(message, v)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
        w(message)  # Возврат к функции w для повторного ввода

def v(message):
    try:
        global u
        u = int(message.text)
        bot.send_message(message.chat.id, "Мусор ")
        bot.register_next_step_handler(message, h)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
        w(message)  # Возврат к функции w для повторного ввода

def h(message):
    try:
        global z
        z = int(message.text)
        xy = x-y
        pk = p-k
        nxy = xy*n
        upk = pk*u
        summ = nxy+upk+z
        bot.send_message(message.chat.id, f"Свет: {nxy}", parse_mode="html")
        bot.send_message(message.chat.id, f"Вода: {upk}", parse_mode="html")
        bot.send_message(message.chat.id, f"Мусор: {z}", parse_mode="html")
        bot.send_message(message.chat.id, f"Сумма: {summ}", parse_mode="html")      
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
        w(message)  # Возврат к функции w для повторного ввода
bot.infinity_polling()
