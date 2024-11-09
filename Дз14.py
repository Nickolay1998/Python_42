##1. Напишите программу, которая покажет все автоморфные числа в интервале от 
##1 до 10000. Автоморфные числа. Натуральное число называется автоморфным 
##если его запись – это последние цифры его квадрата.
##def ten():
##    for i in range(1,10001):
##        if i==(i**2)%10:
##            print(i,"=",i**2)
##
##def one_hundred():
##    for i in range(1,10001):
##        if i==(i**2)%100 and i!=1:
##            print(i,"=",i**2)
##
##def thousand():
##    for i in range(1,10001):
##        if i==(i**2)%1000 and i!=1:
##            print(i,"=",i**2)
##def ten_thousand():
##    for i in range(1,10001):
##        if i==(i**2)%10000 and i!=625 and i!=1:
##            print(i,"=",i**2)
##ten()
##one_hundred()
##thousand()
##ten_thousand()

##2. Напишите программу, которая вычисляет сумму неизвестного количества 
##натуральных чисел, записанную в виде символьной строки.

##def sumlist():
##    s=0
##    for i in range(len(text_num)):
##        s=s+int(text_num[i])              1 вариант
##    print(s)        
##text ="1+25+12+34+89"
##text_num = text.split("+")
##
##sumlist()

##text ="1+25+12+34+89"
##text_num = text.split("+")
##
##g = [int(i) for i in text_num]  #2 вариант
##print(sum(g))

####text_num2 = list(map(lambda i: int(i),text_num )) 3 вариант
####print(sum(text_num2))

##3. Напишите программу, которая на вход получает число и два символа, а на 
##выходе рисует квадрат
##def first_symbol():
##    return "#"*2
##def second_symbol():
##    return "@"*2
##
##a = 5
##for i in range(a):                                        1 Вариант
##    i=i+1
##    if i%2!=0:
##        print(first_symbol(),second_symbol(),first_symbol(),second_symbol(),first_symbol())
##    else:
##        print(second_symbol(),first_symbol(),second_symbol(),first_symbol(),second_symbol())

##a= int(input())
##f = "#"
##s = "@"
##for j in range(1,a+1):
##    print("\n")
##    if j%2!=0:
##        for i in range(1,a+1):
##                if i%2!=0:                                    2 вариант
##                    print(f*2,end="")
##                else:
##                    print(s*2,end="")        
##    else:
##        for i in range(1,a+1):
##            if i%2!=0:
##                 print(s*2,end="")
##            else:
##                print(f*2,end="")

##def fun1():
##    for i in range(1,a+1):
##        if i%2!=0:
##            print(f*2,end="")
##        else:
##            print(s*2,end="")                         3 вариант
##
##def fun2():
##    for i in range(1,a+1):
##        if i%2!=0:
##            print(s*2,end="")
##        else:
##            print(f*2,end="")
##
##a= int(input())
##f = "#"
##s = "@"
##for j in range(1,a+1):
##    print("\n")
##    if j%2!=0:
##        fun1()
##    else:
##        fun2()
        
##4. Дан текст:
text = """As of October 2023, several exciting PC games have been released or announced, including titles like "Starfield" an action RPG set in space, and "Lies of P" a dark reimagining of the Pinocchio tale. Upcoming highly anticipated games include "Avowed" and "Hellblade II: Senua's Saga" which are expected to push the boundaries of storytelling and graphics. Keep an eye out for indie games as well, as they often bring fresh and innovative gameplay experiences."""
####a) Сумму всех цифр в тексте.
##text_num = list(filter(lambda i: i.isdigit(),text))
##s_num = list(map(lambda i: int(i),text_num))
##print(sum(s_num))

##b) Кол-во букв в тексте.
##text_text = list(filter(lambda i: i.isalpha(),text))
##print(len(text_text))

##c) Кол-во знаков пунктуации (, : . ‘ “).
##text_sumbols = list(map(lambda i: i!='.' and i!=',' and i!=':' and i!='"' and i!='`',text))
##print(text_sumbols.count(False))

##d) Переведите все буквы в число запишите их в одну строку.
##text_text = list(filter(lambda i: i.isalpha(),text))
##ord_text = list(map(lambda i: ord(i),text_text))
##str_ord_text = list(map(lambda i: str(i),ord_text))
##g = ' '.join(str_ord_text)
##print(g)

##e) Напишите функцию, которая оставит все слова больше 5 букв.
##def more5value():
##    for i in  range(len(t2)):             1 вариант
##        if len(t2[i])>5:
##            print(t2[i],end=" ")
##t = text.replace('2','').replace('0','').replace('3','').replace(':','').replace(',','').replace('.','').replace('"','').replace('`','')
##t2 = t.split(" ")
##more5value()


##t3= lambda i:[t2[i] for i in range(len(t2)) if len(t2[i])>5] 2 вариант
##print(' '.join(t3(1)))




