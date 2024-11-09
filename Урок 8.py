##text = "Python Hello i here."
##print(text.capitalize()) # Оставляет только 1 букву заглавную все маленькие
##print(text.title())
##print(text.lower())
##print(text.upper()) 
##print(text.isalpha())
##print(text.isdigit()) 

##1
##a = int(input())
##n = a*(1+11+111)

#2
##a = input()
##for i in range(len(a)):
##    if a[i].isalpha():
##        print(ord(a[i]),end="")

##3
##text=input()
##new_text=text.replace("A","W").replace("f","i").replace("j","m").replace("e","y").replace("p","s")
##text_new=new_text[::-1]
##text_text=text_new[::3]
##print(text_new)
##print(text_text)
##print()
## 
##summ=0
##for i in range(len(text_text)):
##    if(text_text[i].isalpha()):
##        summ=summ+ord(text_text[i])
##        print(ord(text_text[i]), end=" ")
##print("\n")
##print("Total sum", summ)
##if summ%2==0:
##    print("Even")
##else:
##    print("Odd")

##4
import random
##a = int(input())
##r = random.randint(2,9)
##while t=True
##    for i in range(a):
##        for j in range(a):
##            if(i+j)%r==0:
##                print("#",end="")
##            else:
##                print("*",end="")
##        print("\n",end ='')
##     print("Exit?")   
##t=True
##while t==True:
##    a=int(input("Number = "))
##    r=random.randint(2,9)
##    print("r =", r)
##    for i in range(a):
##        for j in range(a):
##            if (i+j)%r==0:
##                print("#", end="")
##            else:
##                print(" ", end="")
##        print("\n", end="")
##    print("Exit? [y/n]")
##    c=input("Answer =")
##    if (c=="n"):
##        t=True
##    else:
##        t=False
