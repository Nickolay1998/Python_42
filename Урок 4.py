## % //
##18=x*7+y  # x- целочисленное деления y = остаток от деления
##18=2*7+4
##print(18%7) # %  дает остатоко от деления
##print(18//7) # // - целочисленное деления
##print(4%2) Even четное
##print(5%2) Odd нечетное
##a = int(input("Number "))
##if a%2==0:
##    print("Even")                            
##else:                             - Определения на четность или не четность
##    print("Odd")
##1
##random 1 -277
## Even/Odd
import random
##a = random.randint(1,277)
##print("Number ",a)
##if a%2==0:
##    print("Even")                            
##else:
##    print("Odd")

##2
## random 1-350
##Even +1 / Odd
##a = random.randint(1,350)
##if a%2==0:
##    print("Odd",a+1)                            
##else:
##    print("Even",a-1)
##a = "Hello Python!!!!"  длина текста
##print(len(a))

##3
## text Even/Odd
##a= input()
##if len(a)%2==0:
##    print("Even")
##else:
##    print("Odd")
##a = "Hello Python!!!!" индекс в квадратных скобках текста который считается с нуля
##print(a[4])
##a = "Hello Python!!!!"
##print(a[1:8]) a{start: finish -1} то есть выведется 7 индексов
##a = "Hello Python!!!!"
##print(a[:9]) ## выведится 8 символов задали только финиш
##a = "Hello Python!!!!"
##print(a[:len(a):2]) ## Выводит символы с шагом 2 каждый второй индекс выводится если 2 ставить
##a = "Hello Python!!!!"
##print(a[::-1]) в обратном порядке

##4
## text = text True
## text = txet False
##a = "text"
##b = a[::-1]
##print(a==b)

##5
## Text
##random - sumbol
##a = "Hello Python!!!!"
##b = random.randint(0,len(a)-1) # ставим -1 чтобы было 15 индексов
##print(a[b])
##t = ord("a") # из буквы в цифры
##r = chr(97) # из цифр  в буквы
##print(t,r)

##6
##Random -> 65-90
##Symbol
##a= random.randint(65,90)
##print(chr(a))
## 2 варианта

##7 text - one sumbol(random) - number
##a =  input()
##b = random.randint(0,len(a)-1)
##print(ord(a[b]))

##8 47-74
##a = input()
##print(a[::-1])
##a1=47//10=4
##a2=47-4*10=7
##a3=47%10=7
##a21= 7*10+4=74
##a31 =7*10+4 = 74
##a=int(input())
##a1=a//10 
##a2=a-a1*10 
##a3=a%10
##a21=a2*10+a1
##a31=a3*10+a1
##print(a)
##print(a21)
##print(a31)
##a = int(input())
##print((a%10)*10+(a//10))

##9
## text if even + random symbol (65-90)
## text if odd  + random symbol(33-64)
##a = input()
##if len(a)%2==0:
##    print(a+chr(random.randint(65,90)))
##else:
##    print(a+chr(random.randint(33,64)))
