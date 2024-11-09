##1. Напишите программу, которая на вход получает значения двух чисел a и b, а
##на выходе показывает разницу их преобразований. При этом число a и b,
##преобразуются по разным алгоритмам:

##import math
##def f1():
##    p=round(math.pi,2)
##    a = int(input("Введите число а = "))
##    return ((a**4)*p+100)/a**2
##def f2():                                                                     
##    p=round(math.pi,2)                                #1 вариант
##    b = int(input("Введите число b = "))
##    return (((b**3)+100)*p)/b**2
##
##print(f1()-f2())

##def f1():
##    return ((a**4)*p+100)/a**2
##def f2():
##    return (((b**3)+100)*p)/b**2
##                                                                  #2 вариант
##p=round(math.pi,2)
##a = int(input("Введите число а = "))
##b = int(input("Введите число b =  "))
##print(f1()-f2())

##x = int(input("Ввведите а = "))
##y = int(input("Ввведите b = "))
##p=round(math.pi,2)
##a = lambda i: ((i**4)*p+100)/i**2      #3 вариант
##b = lambda i: (((i**3)+100)*p)/i**2
##print(a(x)-b(y))

##a = int(input("Введите число а = "))
##b = int(input("Введите число b  = "))
##p=round(math.pi,2)                            #4 вариант
##c = ((a**4)*p+100)/a**2
##d = (((b**3)+100)*p)/b**2
##print(c-d)

##2. Напишите программу, которая на вход получает слово размером до 5 букв, а
##на выходе складывает сумму из чисел соответствующих символов и проверят
##полученную сумму на четность или нечетность. Для перевода буквы/символа
##в число используйте ord(). Используйте функции при написании программы.


##def f():
##    s=0
##    for i in range(len(text)):
##        print(text[i],"=",(ord(text[i])))
##        s = ord(text[i])+s
##    print("Cумма = ",s)
##    if s%2==0:
##        print("Слово",text,"Четное")
##    else:
##        print("Слово",text,"Не четное")
##               
##text=input("Введите текст ")
##if len(text)<=5:
##    f()
##else:
##    print("Error")

##3. Дан список [“Category”,5,10,”Movie”,”Game”,20,18,”App”,”Source”,50]
##3.1. Посчитайте сумму чисел из этого списка.

##list_1 = ["Category",5,10,"Movie","Game",20,18,"App","Sourse",50]
##list_num = list(filter(lambda i: i!="Category" and i!="Movie"and i!="Game" and i!="App"and i!="Sourse",list_1))
##print(sum(list_num))
##3.2. Сделайте список только из текста и отсортируйте его.
##list_text = list(filter(lambda i: i!=5 and i!=10 and i!=20 and i!=18 and i!=50,list_1))
##list_text.sort()
##print(list_text)
##3.3. Поменяйте местами 7-й и 2-й элемент списка.
##list_1[1]=18
##list_1[6]=5
##print(list_1)
##3.4. Удалите из списка все четные элементы.

##n = []
##for i in range(len(list_1)):
##    if i%2!=0:
##        n.append(list_1[i])
##print(n)       
##g = [list_1[i] for i in range(len(list_1)) if i%2!=0] # Через генератор
##print(g)

##4. Напишите функцию, которая в случайном порядке определяем месяц, а
##также функцию, которая в случайном порядке определяем день. На выходе у
##пользователя есть функция, которая показывает, какой это знак Зодиака.

##import random
##def moon():
##    x = random.randint(1,12)
##    return x
##def day():
##    y = random.randint(1,31)
##    return y
##
##
##def znak():
##    if a==1 and b>=21 and  b<=31 or a==2 and b>=1 and b<=18:
##        print("Водолей")
##    elif a==2 and b>=19 and b<=31 or a==3 and b>=1 and b<=20:
##        print("Рыбы")
##    elif a==3 and b>=21 and b<=31 or a==4 and b>=1 and b<=20:
##        print("Овен")
##    elif a==4 and b>=21 and b<=31 or a==5 and b>=1 and b<=21:
##        print("Телец")
##    elif a==5 and b>=22 and b<=31 or a==6 and b>=1 and b<=21:
##        print("Близнецы")
##    elif a==6 and b>=22 and b<=31 or a==7 and b>=1 and b<=22:
##        print("Рак")
##    elif a==7 and b>=23 and b<=31 or a==8 and b>=1 and b<=23:
##        print("Лев")
##    elif a==8 and b>=24 and b<=31 or a==9 and b>=1 and b<=23:
##        print("Дева")
##    elif a==9 and b>=24 and b<=31 or a==10 and b>=1 and b<=23:
##        print("Весы")
##    elif a==10 and b>=24 and b<=31 or a==11 and b>=1 and b<=22:
##        print("Скорпион")
##    elif a==11 and b>=23 and b<=31 or a==12 and b>=1 and b<=21:
##        print("Стрелец")
##    elif a==12 and b>=22 and b<=31 or a==1 and b>=1 and b<=20:
##        print("Козерог")
##
##a = moon()
##b = day()
##print(a,b)
##znak()

##5. Напишите функцию, которая в случайном порядке определяем месяц, а
##также функцию, которая в случайном порядке определяем день. На выходе у
##пользователя есть функция, которая показывает, какой это сезон (Зима, Лето,
##Осень, Весна).

##import random
##def moon():
##    x = random.randint(1,12)
##    return x
##def day():
##    y = random.randint(1,31)
##    return y
##
##def vremya_goda():
##    if a==1 and b>=1 and b<=31 or a==2 and b>=1 and b<=31 or a==12 and b>=1 and b<=31:
##       print("Зима")
##    elif a==3 and b>=1 and b<=31 or a==4 and b>=1 and b<=31 or a==5 and b>=1 and b<=31:
##        print("Весна")
##    elif a==6 and b>=1 and b<=31 or a==7 and b>=1 and b<=31 or  a==8 and b>=1 and b<=31:
##        print("Лето")
##    elif a==9 and b>=1 and b<=31 or a==10 and b>=1 and b<=31 or a==11 and b>=1 and b<=31:
##        print("Осень")        
##a = moon()
##b = day()
##print(a,b)
##vremya_goda()
