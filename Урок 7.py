##1
import  random
##a = random.randint(10,50)
##b = random.randint(51,100)
##c = int(input())
##for i in range(a,b,c):
##    print(i)
##while a<=b:
##        print(a,end=" ")
##        a=a+c
##2
##a = input()
##while a:               
##        print(a)
##        a=a[:-1]
##for i in range(len(a),0,-1):
##        print(a[:i])
##3
##a=int(input("Size a="))
##b=int(input("Size b ="))
##c=input("Symbol =")
##for i in range(a):
##    for j in range(b):
##        print(c, end="")
##    print("\n", end="")
##4

##5
##a=int(input("Size a="))
##b=int(input("Size b ="))
##for i in range(a):
##    for j in range(b):
##            if (j+i)%2==0:
##                    print("@", end="")
##            else:
##                    print(" ",end ="")
##    print("\n", end="")
##isalpha только текст
##islnum только цифры
##isdigital состоит из цифр 
##6
##text ="Python175"
##for i in range(len(text)):
##        if(text[i].isdigit()):           #вывести только цифры из текста
##                print(text[i],end="")
##text ="Python175"
##for i in range(len(text)):
##        if(text[i].isalpha()):           #только текст
##                print(text[i],end="")
##text ="Python175"
##for i in range(len(text)):           ##количество пробелов
##        if(text[i].isspace()):           
##                print(text[i],end="")
##text ="Python175 i25 100 751"
##s = 0
##for i in range(len(text)):
##        if(text[i].isdigit()):           ##сумма чисел из текста
##                s=s+int(text[i])
##                print(text[i],end="")
##print("\n")
##print(s)
##text = input()
##s =0
##for i in range(len(text)):
##        if(text[i].isspace()):           #Количество слов
##                s = s+1
##                print(text[i],end=" ")
##print("\n")
##print(s+1)

        
