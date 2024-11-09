                                                       ##урок 2
##Формула радиуса
##import math
##R=float(input())
##print("S=",round(math.pi,2)*R**2)
##Способ возведения в степень через библиотеку
##import math
##a = int(input())
##print(math.pow(a,2))
##5^(2/3)
##print(float(5**(2/3))) 2.92........, а если print(int(5**(2/3))) то будет 2
##5**(1/3) кубический корень из 5
## >, <, >=,<=
##print(5>2) логический тип данных сработал и выдает True или False
##print(5>2 and 6>4) True  а если какое-то условие не правильно будет False
##print(5>2 or 6<4) True потому что если одно из условий выполняется
##Когда что-то сравниваем или присваиваем мы ставим == а одно это если переменная
##< > знак неравенства
##библиотека random - генератор случайных чисел.
import random
import math
##Используется 2 метода: randint(start,finish) и randrange(start,finish,step) step 1 по умолчанию
## а=random.randint(1,3)
## print(a)
##а1=random.randrange(1,10) 
##а2=random.randrange(0,11,5) будет выпадать 0 5 10 
##а3=random.randrange(10) ##найди число от 0 до 10 указали просто границу до какого числа
##print(a1)
##print(a2)
##print(a3)
##random () 0< =c <=1 это по умолчанию интервал.Будет выдавать случайные числа в интервал 0 1
##a1= random.random()
##print(a1)
##a1= random.random()
##print("a1=",round(a1*100,2))
                                                                          ## Задачи
##a = int(input())
##b = random.randint(1,5)
##print(a**b+10)

##b = random.randint(1,100)
##print(b>50)

##a = random.randint(1,10)
##b = random.randint(5,15)
##print(a>b)

##R= random.random() преобразовать радиус умножить на 10 и потом найти площадь
##P = math.pi,
##r0 = round(R*10,2)
##print(round(P*r0**2,2) )
## или print("S=",round(math.pi*math.pow(r0,2),2))

##a = random.randint(1,9)
##random.randint(1,9)
##print(str(a)+str(b))
## print(a,b,sep="") sep разделитель или и мы ставим ничего чтобы цифры сошлись
##Если будет random.randint(10,99) print(a*100+b)



