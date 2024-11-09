#Задания 1
a=int(input("Day number "))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")
else:
    print("Error")
#Задания 2
a=int(input("Month number"))
if a==1:
    print("Winter")
elif a==2:
     print("Winter")
elif a==3:
    print("Spring")
elif a==4:
    print("Spring")
elif a==5:
    print("Spring")
elif a==6:
    print("Summer")
elif a==7:
    print("Summer")
elif a==8:
    print("Summer")
elif a==9:
    print("Fall")
elif a==10:
    print("Fall")
elif a==11:
    print("Fall")
elif a==12:
    print("Winter")
else:
    print("Error")
# Задания 3
a= int(input("Число1 "))
b= int(input("Число2 "))
if a>b:
    print(b,a)
elif a<b:
    print(a,b)
else:
    print("The same numbers")
#Задания 4
import random
a = random.randint(1,1000)
b = input("Парне или Не парне")
if  b=="Парне" and  a%2==0:
    print( a,"You win")
elif b=="Не парне" and a%2!=0:
     print(a,"You win")
else:
    print(a,"Bot win")
##Задания 5
##Вариант1 
a = float(input("Kм/год "))
print("м/c",round(a/3.6,1))

## Вариант2
a=int(input("Км "))
b=int(input("год "))
print("м/c",round((a*1000)/(b*60*60),1))

##Вариант3
a=int(input("Км "))
b=int(input("год "))
c=a/b
print(round(c/3.6,1))

##Вариант 4
a=int(input("Км "))
b=int(input("год "))
print(a/b)
c=int(input("Км/год "))
if a/b==c:
    print("м/с",round(c/3.6,1))
else:
    print("Error")
##Задания 6
a = input("Color ")
if a=="Red":
    print("Stop")
elif a=="Green":
    print("Go")
elif a=="Yellow":
    print("Wait")
else:
    print("Error")


