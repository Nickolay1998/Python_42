##1
##a = int(input())
##b = int(input())
##c = int(input())
##d = int(input())
##print("min number",min(a,b,c,d),"max number",max(a,b,c,d)) Вариант 1
##Sum = a+b+c+d
##N1= Sum-b-c-d
##N2= Sum-a-c-d
##N3=Sum-a-b-d
##N4=Sum-a-b-c
##if N1<N2 and N1<N3 and N1<N4:
##    print("min number =",N1)
##elif N2<N1 and N2<N3 and N2<N4:
##    print("min number =",N2)
##elif N3<N1 and N3<N2 and N3<N4:
##    print("min number =",N3)
##elif N4<N1 and N4<N2 and N4<N3:                   Вариант 2
##    print("min number =",N4)
##else:
##    print("Error")   
##if N1>N2 and N1>N3 and N1>N4:
##    print("max number =",N1)
##elif N2>N1 and N2>N3 and N2>N4:
##    print("max number =",N2)
##elif N3>N1 and N3>N2 and N3>N4:
##    print("max number =",N3)
##elif N4>N1 and N4>N2 and N4>N3:
##    print("max number =",N4)
##else:
##    print("Error")

##2
##a = int(input())
##t =a/3600//1
##Min = (a-t*3600)/60//1
##sek =a%60
##print(int(a/3600//1),":",int((a-(a/3600//1)*3600)/60//1),":",int(a%60))

#3
##a= int(input())
##print(int(str(a)[::-1]),int(str(a)[::-1])+a,int(str(a)[::-1])*a,abs(int(str(a)[::-1])-a)) 1 варинт
##b=int(str(a)[::-1])
##print(b,b+a,b*a,abs(b-a)) 2 вариант

##4
##a = int(input())
##b = str(a)
##c=len(b)
##if (int(b[0])**c+int(b[1])**c+int(b[2])**c)==a:
##    print("Число Армстронга")
##else:
##    print("не является числом Армстронга")
##a = int(input())
##c=len(str(a))
##if (int(str(a)[0])**c+int(str(a)[1])**c+int(str(a)[2])**c)==a:
##    print("Число Армстронга")
##else:
##    print("не является числом Армстронга")

##5
##a=int(input())
##b=int(str(a)[::-1])
##if a%2==0 and b%2==0:
##    print("Зеркальное число",b,"Оба числа четные")
##elif a%2!=0 and b%2!=0:
##    print("Зеркальное число",b,"Оба числа не четные")
##else:
##    print("Зеркальное число",b,"Одно четное, второе не четное")

##6
##import random
##a=int(input())
##b=int(input())
##c = random.randint(0,1000)
##print(c)
##if a>0 and b>0:
##    print(a*b+c)
##elif a<0 and b<0:
##    print(a*b*c)
##elif a>0 and b<0 or a<0 and b>0:
##    print(a*c+b*c)
##else:
##    print("0")
