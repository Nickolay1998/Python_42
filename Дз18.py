import telebot
import random
from telebot import types
import math
bot = telebot.TeleBot("6734050072:AAEWJ5wRWvnBd1B3GB_gPzkwHrFaIGoc36g")
@bot.message_handler(content_types=["text"])

##1. Написать чат-бот, который по команде от пользователя: пользователь вводит 
##значение от 1 до 7. Выводит название дня недели.
##def days(message):
##    if message.text =="1":
##        bot.send_message(message.chat.id,"Понедельник")
##    elif message.text =="2":
##        bot.send_message(message.chat.id,"Вторник")
##    elif message.text =="3":
##        bot.send_message(message.chat.id,"Среда")
##    elif message.text =="4":
##        bot.send_message(message.chat.id,"Четверг")
##    elif message.text =="5":
##        bot.send_message(message.chat.id,"Пятница")
##    elif message.text =="6":
##        bot.send_message(message.chat.id,"Суббота")
##    elif message.text =="7":
##        bot.send_message(message.chat.id,"Воскресенье")        
##    else:
##        bot.send_message(message.chat.id,"Error")
##    
##2. Написать чат-бот, который по команде от пользователя: пользователь вводит 
##значение от 1 до 12. Выводит название месяца и время года.        
##def mounth(message):
##    if message.text =="1":
##        bot.send_message(message.chat.id,"Январь,Зима")
##    elif message.text =="2":
##        bot.send_message(message.chat.id,"Февраль,Зима")
##    elif message.text =="3":
##        bot.send_message(message.chat.id,"Марта,Весна")
##    elif message.text =="4":
##        bot.send_message(message.chat.id,"Апрель,Весна")
##    elif message.text =="5":
##        bot.send_message(message.chat.id,"Май,Весна")
##    elif message.text =="6":
##        bot.send_message(message.chat.id,"Июнь,Лето")
##    elif message.text =="7":
##        bot.send_message(message.chat.id,"Июль,Лето")
##    elif message.text =="8":
##        bot.send_message(message.chat.id,"Август,Лето")
##    elif message.text =="9":
##        bot.send_message(message.chat.id,"Сентябрь,Осень")
##    elif message.text =="10":
##        bot.send_message(message.chat.id,"Октябрь,Осень")
##    elif message.text =="11":
##        bot.send_message(message.chat.id,"Ноябрь,Осень")
##    elif message.text =="12":
##        bot.send_message(message.chat.id,"Декабрь,Зима")  
##    else:
##        bot.send_message(message.chat.id,"Error")

##3. Написать чат-бот, который по команде от пользователя, показывает 1 из 7 
##стикеров в произвольном порядке.

##@bot.message_handler(content_types=["sticker"])   ##Через эту команду узнал id
##def user_sticker(message):
##    sticker_id = message.sticker.file_id
##    bot.send_message(message.chat.id,sticker_id)
##@bot.message_handler(content_types=["text"])
##def stickers(message):
##    if message.text=="Sticker":
##        num = str(random.randint(1,7))
##        if num=="1":
##            bot.send_sticker(message.chat.id,"CAACAgIAAxkBAANeZubG3d2hQSbiDQNkUX4QAWmV3VwAAgcLAAIvD_AG9V1bcxvUVWM2BA")
##        elif num=="2":
##            bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAPLZubfz4qXfZmdq8Q3JR1gm9kAAWvnAAIWAAPANk8TYCHXLaIEtmc2BA")   
##        elif num=="3":
##            bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAPNZubf_77gP5Na4pk2F6vnrQoYaDwAAhMAA8A2TxOqs4f3fzjKpTYE")
##        elif num=="4":
##            bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAPPZubgGtoiGah_Og53uPMoVm-AU8AAAhUAA8A2TxPNVqY7YZ5k5zYE")
##        elif num=="5":
##            bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAPRZubgMiQmCMSyHKkx4BOT1I7kQUQAAmcCAAJSFOEKPataGbK1rWs2BA")
##        elif num=="6":
##            bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAPTZubgNWmDYH64YG8K-EbBoh4TBQoAAm0ZAAJCr2kAAcN6pwIFtpPBNgQ")
##        elif num=="7":
##            bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAPVZubgPfamgYQgc77a045i_ib7e5QAAkIAA-lVBRiGW2J5mAvbmjYE")
##    else:
##        bot.send_message(message.chat.id,"Error")
##4. Написать чат-бот, который по команде от пользователя: производит расчет 
##площади стен в комнате. Площадь стен рассчитывается по формуле 2*(a*h + 
##b*h)* 0.92., где h – высота стены, a и b – стороны основания (стороны пола).

##1 ваирант   Тут мне интернет помог
##@bot.message_handler(commands=["start"])
##def w(message):
##    bot.send_message(message.chat.id,"Введите число a")
##    bot.register_next_step_handler(message,a)          
##
##def a(message):
##    global x
##    x = int(message.text)
##    bot.send_message(message.chat.id,"Введите число b")
##    bot.register_next_step_handler(message,b)
##    
##def b(message):
##    global y
##    y=int(message.text)
##    bot.send_message(message.chat.id,"Введите число  h")
##    bot.register_next_step_handler(message,h)
##
##def h(message):
##    global z
##    z=int(message.text)
##    s = 2*(x*z+y*z)*0.92
##    bot.send_message(message.chat.id,s)
##
##2 вариант Тут я освоил немного Try и Except
##@bot.message_handler(commands=["start"])
##def w(message):
##    bot.send_message(message.chat.id, "Введите число a")
##    bot.register_next_step_handler(message, a)
##
##def a(message):
##    try:
##        global x
##        x = int(message.text)
##        bot.send_message(message.chat.id, "Введите число b")
##        bot.register_next_step_handler(message, b)
##    except ValueError:
##        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
##        w(message)  # Возврат к функции w для повторного ввода
##
##def b(message):
##    try:
##        global y
##        y = int(message.text)
##        bot.send_message(message.chat.id, "Введите число h")
##        bot.register_next_step_handler(message, h)
##    except ValueError:
##        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
##        w(message)  # Возврат к функции w для повторного ввода
##
##def h(message):
##    try:
##        global z
##        z = int(message.text)
##        s = 2 * (x * z + y * z) * 0.92
##        bot.send_message(message.chat.id, f"Результат: {s}")
##    except ValueError:
##        bot.send_message(message.chat.id, "Ошибка! Введите корректное число.")
##        w(message)  # Возврат к функции w для повторного ввода

##def user_text(message):
##    @bot.message_handler(content_types=["text"])
##    def user_capec(message):
##        list_text1=message.text.split(",")
##        print(list_text1)
##        a=int(list_text1[0])
##        h=int(list_text1[1])
##        b=int(list_text1[2])
##        print(a)
##        print(h)
##        print(b)
##        if len(list_text1)!=3:
##            bot.send_message(message.chat.id,"OSHIBKA NASANIKA",parse_mode="html")
##        else:
##            c=2*(a*h+b*h)*0.92
##            bot.send_message(message.chat.id,c,parse_mode="html")

bot.infinity_polling()


##5. Создайте в файле массив 10 на 10 и заполните его в случайном порядке 
##буквами в верхнем регистре. Правда ли, что в данном массиве присутствует 
##читаемое слово. Случайные числа находятся в интервале от 65 до 90, что 
##позволит использовать для перевода чисел в буквы Unicode.

##a = int(input())
##for i in range(a):
##    with open("C:/Users/admin/Desktop/22.txt","a") as f:   
##        f.write(" ".join(list(map(str,[chr(random.randint(65,90)) for i in range(a)])))+"\n")
##with open("C:/Users/admin/Desktop/22.txt","r") as f:
##    print(f.read())      

       


           
