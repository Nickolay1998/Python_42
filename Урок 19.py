##import random
##while "Игра": 
##    print(" Начать игру + \n Выход -")
##    a = input()
##    if a =="+" :
##        f =  str(random.randint(0,3))
##        g = str(random.randint(0,3))
##        c = str(random.randint(0,3))
##        if f==g==c:
##            s=f,g,c,"Джекпот" 
##        else:
##           s=f,g,c,"You lose"     
##        with open("C:/Users/admin/Desktop/testpython.txt","w") as f:
##            f.write(" ".join(s))
##        with open("C:/Users/admin/Desktop/testpython.txt","r") as f:
##            print(f.read())
##    elif a=="-":
##        break    
  
    
##while True:
## 
##    print("Select operation")
##    print("1. +")
##    print("2. -")
##    print("3. *")
##    print("4. :")
##    print("5. fINISH")
## 
##    a = input("Select number (1/2/3/4/5): ")
##    if a == '5':
##        print("Finish.")
##        break
## 
##    num1 = int(input("Enter number 1: "))
##    num2 = int(input("enter number 2: "))
## 
##    if a == '1':
##        result = num1 + num2
##        print("+",result)
##    elif a == '2':
##        result = num1 - num2
##        print("-",result)
##    elif a == '3':
##        result = num1 * num2
##        print("*", result)
##    elif a == '4':
##        if num2 != 0:
##            result = num1 / num2
##            print(":",result)
##        else:
##            print("Error, division 0")
##    else:
##        print("Error")
## 
##with open("C:/Users/admin/Desktop/testpython.txt","w") as file:
##    result=str(result)
##    file.write(result)

##def writefile(ab):
##    with open("C:/Users/admin/Desktop/testpython.txt","a") as file_in:
##        file_in.write(str(ab)+"\n")
## 
##a=int(input("num_1 = "))
##b=int(input("num_2 = "))
##c=int(input("select: 1- + ,2 - -, 3 - *, 4 - /"))
## 
##if c==1:
##    ab=a+b
##    writefile(ab)
##    print(ab)
##elif c==2:
##    ab=a-b
##    writefile(ab)
##    print(ab)
##elif c==3:
##    ab=a*b
##    writefile(ab)
##    print(ab)
##elif c==4:
##    ab=a/b
##    writefile(ab)
##    print(ab)
##else:
##    print("Error")

import telebot
bot=telebot.TeleBot("7422277575:AAGHilGqvo3_N9tLx7bCOAeEIYKblokYFcQ")
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"<b><u>Hello</u></b>",parse_mode="html")
@bot.message_handler(content_types=['text'])
def user_text(message):
    if message.text=="Hi":
         bot.send_message(message.chat.id," Hi! Hi!"+message.from_user.last_name)
    elif message.text=="Num":
        num=random.randint(1,1000)
        bot.send_message(message.chat.id,num)
##    elif message.text=="photo":
##        ph = open("C:/Users/admin/Pictures/Camera Roll")
##        bot.send_photo(message.chat.id,ph)
    elif message.text=="show":
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAANWZuMt9M_57lSP4irtu_iEUYK-u64AAhILAAIvD_AG-SyFxS4rEbw2BA")
    else:
        bot.send_message(message.chat.id," Error")

@bot.message_handler(content_types=['sticker'])
def user_sticker(message):
    sticker_id=message.sticker.file_id
    bot.send_message(message.chat.id,sticker_id)
bot.infinity_polling()


