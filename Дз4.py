#1
##a = int(input()) 
##b= str(a)           # 1 вариант
##print(b[::-1])

##a1=a//1000
##a2=a%1000//100 # 2 вариант
##a3=a%100//10
##a4=a%10
##print(a4*1000+a3*100+a2*10+a1)

##a1=a//1000
##a2=a%1000//100*10 # 3 вариант
##a3=a%100//10*100
##a4=a%10*1000
##print(a4+a3+a2+a1)
##print((a%10*1000)+(a%100//10*100)+(a%1000//100*10)+(a//1000)) #вариант 4

#2
##a=int(input())
##a1=a//100
##a2=a%100//10
##a3=a%10
##print("1st number:",a1,"2st number:",a2,"3st number:",a3,"Sum:",a1+a2+a3) # вариант1


##print("1st number:",a//100,"2st number:",a%100//10,"3st number:",a%10,"Sum:",a//100+a%100//10+a%10) # вариант2

#a=input("Трехзначное число ")
#a1=a[0]
#a2 =a[1]                           вариант 3 
#a3=a[2]
#print(a1,a2,a3,int(a1)+int(a2)+int(a3))      

#3
##a = int(input())
##a1 = a//10*7
##a2 = a%10*9  вариант 1
##print(str(a2)+str(a1))
##a1 = a//10*7
##a2 = a%10*9
##b1= a2//10
##b2= a2%10
##b3= b1*1000+b2*100
##print("Num1:",a1,"Num2:",a2,"Total:",b3+a1)

#4
##a= input("Text1: ")
##b= input("Text2: ")
##print("Text1",len(a))
##print("Text2",len(b))
##if len(a)>len(b):
##    print("Text1>Text2")
##else:
##    print("Text2>Text1")

#5
##a = input("text1: ")
##print(a[:len(a):3])

#6
##a = input()
##if a[0]!=a[-1]:
##    print("Unhappy")
##else:
##    print("Happy")
