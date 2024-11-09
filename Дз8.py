##1 Показать на экране таблицу умножения для всех чисел от 1 до 9.
##i=1
##for i in range(1,10):
##    j=1
##    for j in range(0,9):
##        j=j+1
##        print(j*i,end= " ")
##    print("\n",end="")
##i=0
##while i<=8:
##    i=i+1
##    j=0
##    for j in range(0,9):
##        j=j+1
##        print(i*j,end=' ')
##    
##    print("\n",end='')

##2 Используя цикл for нарисуйте следующую фигуру, если пользователь задает размер 
##стороны и символ:
##Вариант1
##a=int(input("Сторона квадрата = "))+1
##b=int(input("Сторона квадрата = "))+1
##c=input("Символ = " )
##for i in range(1,a):
##    for j in range(1,b):
##        if i%2!=0:
##            print(c,end='')
##        else:
##            print("",end='')
##    print("\n", end="")
##Вариант 2
##a=int(input("Сторона квадрата = "))
##c=input("Cимвол ")
##for i in range(a):
##    i=i+1
##    if i%2!=0:
##        print(c*5)
##    else:
##        print("")

##3 Используя цикл for нарисуйте следующую фигуру, если пользователь задает размер 
##стороны и символ для четного и нечетного счета:
##Вариант1
##a=int(input("Сторона квадрата = "))+1
##b=int(input("Сторона квадрата = "))+1
##c=input("Символ = ")
##d=input("Символ = ")
##for i in range(1,a):
##    for j in range(1,b):
##        if i%2!=0:
##            print(c,end='')
##        elif i%2==0:
##            print(d,end='')
##    print("\n", end="")
##Вариант2
##a=int(input("Сторона квадрата = "))
##c=input("Cимвол ")
##d= input("Символ ")
##for i in range(a):
##    i=i+1
##    if i%2!=0:
##        print(c*5)
##    else:
##        print(d*5)

##4 Используя цикл for нарисуйте следующую фигуру, если пользователь задает размер 
##стороны и символ:    
##a=int(input("Сторона квадрата = "))
##c=input("Символ = ")
##s=a
##for i in range(a):
##    i=i+1
##    s=s-1
##    print(" "*s,c)
##print("\n",end="")

####5Дан текст: “Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m 
##good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask 
##ChatGPT.

##а) Посчитайте сколько предложений в данном тексте;
##a = "Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask  ChatGPT."
##b = a.replace("!",".").replace("?",".")
##s=0
##for i in range(len(b)):
##    if b[i]==".":
##        s=s+1
##print("Количество предложений = ",s)

##b) Посчитайте сколько пробелов в данном тексте;
##a = "Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask  ChatGPT."
##s=0
##for i in range(len(a)):
##    if a[i].isspace():
##        s=s+1
##print("Количество пробелов = ",s)

##c) Посчитайте сколько раз встречается буква “a”;

a = "Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask  ChatGPT."
s=0
for i in range(len(a)):
    if a[i]=="l":
        s=s+1
print("Количество а = ",s)
print(len(a))

##d) Переведите данный текст в нижний регистр;
##a = "Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask  ChatGPT."
##print(a.lower())

##e) Выведите каждый 5-й символ данного текста;

##a = "Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask  ChatGPT."
##print(a[::4]) ##Вариант 1
##for i in range(0, len(a), 4):  ##Варинт 2
##    print(a[i],end="")

##h) Посчитайте длину текста и если она четная укажите это, если нечетная также укажите это;
##a = "Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask  ChatGPT."
##print(len(a))
##if len(a)%2==0:
##    print("Четное")
##else:
##    print("Не четное")

##i) Выведите данный текст в обратном порядке.

##a = "Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask  ChatGPT."
##print(a[::-1])

##6Дан текст: “Our phone number + 38 (088) 125 67 92 and we are open from 9:00 to 18:00.”

###а) Посчитайте сумму всех чисел входящих в данный текст;
##text = "Our phone number + 38 (088) 125 67 92 and we are open from 9:00 to 18:00."
##s =0
##for i in range(len(text)):
##    if(text[i].isdigit()):
##        print(text[i],end="")
##        s=s+int(text[i])
##print("\n")
##print(s,end="")

####b) Посчитайте сумму всех четных чисел входящих в данный текст;
##text = "Our phone number + 38 (088) 125 67 92 and we are open from 9:00 to 18:00."
##s =0
##for i in range(len(text)):
##    if (text[i].isdigit()):
##        if int(text[i])%2==0:
##            print(text[i],end="")
##            s=s+int(text[i])
##print("\n","Sym= ",s,end=" ")

####с) Посчитайте сумму всех нечетных чисел входящих в данных текст;
##text = "Our phone number + 38 (088) 125 67 92 and we are open from 9:00 to 18:00."
##s =0
##for i in range(len(text)):
##    if (text[i].isdigit()):
##        if int(text[i])%2!=0:
##            print(text[i],end="")
##            s=s+int(text[i])
##print("\n","Sym= ",s,end=" ")

##d) Посчитайте сумму всех чисел входящих в данный текст, которые делятся на 3 без остатка.
##text = "Our phone number + 38 (088) 125 67 92 and we are open from 9:00 to 18:00."
##s =0
##for i in range(len(text)):
##    if (text[i].isdigit()):
##        if int(text[i])%3==0:
##            print(text[i],end="")
##            s=s+int(text[i])
##print("\n","Sym= ",s,end=" ")


