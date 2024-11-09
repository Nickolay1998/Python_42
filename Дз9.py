##1 Показать на экране таблицу умножения для всех чисел от 1 до 10
##i=1
##for i in range(1,11):
##    j=1
##    for j in range(0,10):
##        j=j+1
##        print(i,"*",j,"=",j*i,end=" ")
##    print("\n",end="")

##2 Используя цикл for нарисуйте пустой квадрат, если пользователь задает размер стороны и  символ:
a = int(input())
c = input()
for i in range(a):
    i=i+1
    if i==2 or i==3 or i==4:
        print(c," "*4,c)
    else:
        print(c*5)

##3 Используя цикл for возведите в квадрат все числа от 11 до 99 и выведите результат на экран.
##s=0
##for i in range(1,10):
##    s=s+10
##    for j in range(1,10):
##            j=j+s
##            if j!=20 and j!=30 and j!=40 and  j!=50 and j!=60 and j!=70 and j!=80 and j!=90:
##                print(j,end=" ")
##    print("\n",end="")

##4 Пользователь вводит с клавиатуры диаметр окружности. В зависимости от выбора пользователя, посчитайте либо площадь, либо периметр окружности.

##import math
##d = int(input("Диаметр окружности "))
##r = d/2
##p =round(math.pi,2)
##print("Площадь окружности = ",p*r**2)
##print("Площадь окружности = ",p*(d/2)**2)
##print("Площадь окружности = ",p*pow(d/2,2))
##print("Периметр окружности = ",2*p*r)
##print("Периметр окружности = ",2*p*(d/2))

#5 Напишите программу, которая на вход получает пять слов, а на выходе в случайном  порядке берет из каждого слова по одному символу и составляет из них слово.
##import random
##word1 = input()
##word2 = input()
##word3 = input()
##word4 = input()
##word5 = input()
##a = random.randrange(len(word1))
##a1 = word1[a]
##b = random.randrange(len(word2))
##b1 = word2[b]
##c = random.randrange(len(word3))
##c1 = word3[c]
##d = random.randrange(len(word4))
##d1 = word4[d]
##f = random.randrange(len(word5))
##f1 = word4[f]
##print("Result:",a1+b1+c1+d1+f1)

##6 Напишите программу, которая на вход получает слово от 5 до 10 символов, а на выходе делает замену этого слова на символы.
##a = input()
##if len(a)==5:
##    print(a.replace(a[0],"@").replace(a[1],"#").replace(a[2],"&").replace(a[3],"!").replace(a[4],"+"))
##elif len(a)==6:
##     print(a.replace(a[0],"@").replace(a[1],"#").replace(a[2],"&").replace(a[3],"!").replace(a[4],"+").replace(a[5],"//"))
##elif len(a)==7:
##     print(a.replace(a[0],"@").replace(a[1],"#").replace(a[2],"&").replace(a[3],"!").replace(a[4],"+").replace(a[5],"//").replace(a[6],"!"))
##elif len(a)==8:
##     print(a.replace(a[0],"@").replace(a[1],"#").replace(a[2],"&").replace(a[3],"!").replace(a[4],"+").replace(a[5],"//").replace(a[6],"!").replace(a[7],"#"))
##elif len(a) ==9:
##     print(a.replace(a[0],"@").replace(a[1],"#").replace(a[2],"&").replace(a[3],"!").replace(a[4],"+").replace(a[5],"//").replace(a[6],"!").replace(a[7],"#").replace(a[8],"&"))    
##elif len(a)==10:
##    print(a.replace(a[0],"@").replace(a[1],"#").replace(a[2],"&").replace(a[3],"!").replace(a[4],"+").replace(a[5],"//").replace(a[6],"!").replace(a[7],"#").replace(a[8],"&").replace(a[9],"!"))
##else:
##    print("Error")lH:g5LmDxVr9,E

