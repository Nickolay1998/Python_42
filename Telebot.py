# parse_mode="html" # можно делать теги
#<b> text </b>  жирный шрифт
#<i>text</i>  or <em> italic курсив
#<u>text</u>  подчеркнутый
##import random
import telebot
bot=telebot.TeleBot("7768845863:AAFbu0aDimoj0k6Zb1GLZYmOYT1p9GRdFAM")
##@bot.message_handler(commands=["start"]) #прописываем команду на которую он будет реагировать
##def start(message):
##    bot.send_message(message.chat.id,"<b>Hello</b>",parse_mode="html") 
##    bot.send_message(message.chat.id,"<i>Hello</i>",parse_mode="html")
##    bot.send_message(message.chat.id,"<u>Hello</u>",parse_mode="html")
##    bot.send_message(message.chat.id,"<b><u><i>Hello</i></u></b>",parse_mode="html") #  что вводит в первую очередь нужно писать в последнюю где слеш

@bot.message_handler(content_types=["text"]) #что мы будем делать(доп функционал для бота который будет реагировать на текст)
def user_text(message):
    if message.text=="Start":
        bot.send_message(message.chat.id,"Hi Hi"+message.from_user.first_name)
    elif message.text =="Num":
        num = random.randint(1,1000)
        bot.send_message(message.chat.id,num)
    elif message.text =="Show":
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAANiZubG5xnQHQMKizk8nKeJfk9-A_EAAggLAAIvD_AGb-QAARlf9XhfNgQ')  #Выводит стикер
    elif message.text =="Photo":
        ph = open("C:/Users/admin/Pictures/images.jfif","rb")   #Выводит фото
        bot.send_photo(message.chat.id,ph)
    else:
        bot.send_message(message.chat.id,"Error")
bot.infinity_polling() 
##
##@bot.message_handler(content_types=["sticker"])
##def user_sticker(message):
##    sticker_id = message.sticker.file_id
##    bot.send_message(message.chat.id,sticker_id)
##
##bot.infinity_polling() # команда чтобы зациклить бот чтобы он был в действии
##import telebot
##from google.cloud import bigquery
##from google.oauth2 import service_account
##
##bot=telebot.TeleBot("6734050072:AAEWJ5wRWvnBd1B3GB_gPzkwHrFaIGoc36g")
##credentials=service_account.Credentials.from_service_account_file("C:/Users/admin/Downloads/Telegram Desktop/itstep-382618-558382b49c6f.json")
##project_id="itstep-382618"
##client=bigquery.Client(credentials=credentials,project=project_id)
##@bot.message_handler(content_types=['text'])
####def info(message):
##    if message.text.lower()=="sum":
##        query_job=client.query("""
##                                SELECT 
##                                round(sum(tb.payment_sum),2) AS sum_total
##                                FROM `itstep-382618`.itstep_bot.data_tb AS tb  
##                               """)
##        results=query_job.result()
##        bot.send_message(message.chat.id,results)
##
##    elif message.text.lower()=="gsum":
##        query_job=client.query("""
##                                SELECT 
##                                tb.period,
##                                round(sum(tb.payment_sum),2) AS sum_total
##                                FROM `itstep-382618`.itstep_bot.data_tb AS tb
##                                GROUP BY tb.period
##                                ORDER BY 2 DESC
##                                LIMIT 5 
##                               """)
##        results=query_job.result()
##        bot.send_message(message.chat.id,results)

##bot.infinity_polling()

##import telebot
##from google.cloud import bigquery
##from google.oauth2 import service_account
## 
####credentials=service_account.Credentials.from_service_account_file("C:/Users/admin/Downloads/Telegram Desktop/itstep-382618-558382b49c6f.json")
####project_id="itstep-382618"
####client=bigquery.Client(credentials=credentials,project=project_id)
#### 
##bot=telebot.TeleBot("6734050072:AAEWJ5wRWvnBd1B3GB_gPzkwHrFaIGoc36g")
##credentials=service_account.Credentials.from_service_account_file("C:/Users/admin/Downloads/Telegram Desktop/itstep-382618-558382b49c6f.json")
##project_id="itstep-382618"
##client=bigquery.Client(credentials=credentials,project=project_id)
##@bot.message_handler(content_types=['text'])
##def info(message):
##    if message.text.lower()=="sum":
## 
##        credentials=service_account.Credentials.from_service_account_file("C:/Users/admin/Downloads/Telegram Desktop/itstep-382618-558382b49c6f.json")
##        project_id="itstep-382618"
##        client=bigquery.Client(credentials=credentials,project=project_id)
## 
##        query_job=client.query("""
##                        SELECT 
##                        t2.UserCity,
##                        count(t2.UserCity) AS countUserbyCity,
##                        sum(t1.sumTotal) AS sumbyCity
##                        FROM 
##                                        (
##                                                SELECT DISTINCT(dt.user_id) AS IDuser1, 
##                                                sum(dt.payment_sum) AS sumTotal
##                                                FROM itstep_bot.data_tb as dt
##                                                GROUP BY IDuser1
##                                        ) AS t1
##                        INNER JOIN 
##                                        (
##                                                SELECT DISTINCT(db.id_client) AS IDuser2,
##                                                db.id_city AS UserCity
##                                                FROM itstep_bot.data_base as db
##                                        ) AS t2 
##                        ON t1.IDuser1= t2.IDuser2
##                        GROUP BY t2.UserCity
##                        ORDER BY 3 desc
##                               """)
##        results=query_job.result()
##        text_listbq=list(results)
## 
## 
##        with open("C:/Users/admin/Desktop/text_bq.txt","r") as textBQ:
##            list_read=textBQ.read()
##        
##
##        bot.send_message(message.chat.id,list_read)
##bot.infinity_polling()
import random
import telebot
from telebot import types
from google.cloud import bigquery
from google.oauth2 import service_account
credentials=service_account.Credentials.from_service_account_file("C:/Users/admin/Downloads/Telegram Desktop/itstep-382618-558382b49c6f.json")
project_id="itstep-382618"
client=bigquery.Client(credentials=credentials,project=project_id)
bot=telebot.TeleBot("6734050072:AAEWJ5wRWvnBd1B3GB_gPzkwHrFaIGoc36g")
@bot.message_handler(commands=['link'])
def start(message):
    markup=types.InlineKeyboardMarkup()
    buttonOne=types.InlineKeyboardButton(text="YouTube",url="www.youtube.com")
    markup.add(buttonOne)
    bot.send_message(message.chat.id,"Click",reply_markup=markup)


@bot.message_handler(commands=['select'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    butOne=types.KeyboardButton("Start")
    butTwo=types.KeyboardButton("Finish")
    markup.add(butOne,butTwo)
    bot.send_message(message.chat.id,"Select",reply_markup=markup)

@bot.message_handler(content_types=['text'])
def buttonText(message):
    if message.text=="Start":
        bot.send_message(message.chat.id,"WIN")
    elif message.text=="Finish":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne=types.KeyboardButton("Level")
        butTwo=types.KeyboardButton("Score")
        butThree=types.KeyboardButton("Back")
        markup.add(butOne,butTwo,butThree)
        bot.send_message(message.chat.id,"Chooce",reply_markup=markup)
    elif message.text=="Back":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        butOne=types.KeyboardButton("Start")
        butTwo=types.KeyboardButton("Finish")
        markup.add(butOne,butTwo)
        bot.send_message(message.chat.id,"Select",reply_markup=markup)
    elif message.text=="Level":
        a=random.randint(1,50)
        bot.send_message(message.chat.id,a)            
    elif message.text=="Score":
        query_job=client.query("""
                        SELECT round(sum(dt.payment_sum),2)
                        FROM itstep_bot.data_tb as dt
                               """)
        results=query_job.result()
        bot.send_message(message.chat.id,results)        
    else:
        bot.send_message(message.chat.id,"Error")

bot.infinity_polling()
    
