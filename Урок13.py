import random
##def p():
##    s = int(input("Цифра2 "))
##    return s 
##def f(b):
##    return b *10
##def g():
##    return random.randint(10,99)*p()
##    
##
##a = input("Введите цифру ")
##
##if a.isdigit()==True:
##    print(f(int(a))*g())
##else:
##    print("Not")


##def kv():
##    return a**2
##def cub():
##    return a**3
##
##print("Квадрат/Куб")
##b = input("Выберите вариант ")
##
##a = int(input("Введите число "))
##if b=="Куб":
##    print(cub())
##elif b=="Квадрат":
##    print(kv())
##else:
##    print("Error")

##def powertwo():
##    n=int(input("Input number"))
##    return n**2
## 
##def powerthree():
##    n=int(input("Input number"))
##    return n**3
###--------main()------------------
## 
##a=int(input("1 ^2, 2 ^3"))
##if a==1:
##    print(powertwo())
##elif a==2:
##    print(powerthree())
##else:
##    print("Error")

##def list_n():
##    n = []
##    a = int(input())
##    for i in range(a):
##        n.append(random.randint(10,99))
##    print(n)
##    return(n)
##
##def sum_list_n():
##    t=sum(list_n())
##    print(t)
##    return t
##
##def evenodd():
##    if sum_list_n()%2==0:
##        print("Even")
##    else:
##        print("Odd")
##
##evenodd()
##list_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,21]
##new_list = list(filter(lambda i:i%2==0, list_num))
##new_list2 = list(filter(lambda i:i%3==0 and i%7==0, list_num))
##print(new_list)
##print(new_list2)

##list_n = [random.randint(10,99) for i in range(20)]
##n_list = list(filter(lambda i: i>65,list_n))
##print(n_list())
##a=int(input())
##b=int(input())
##max_n = lambda a,b: a if a>b else b
##print(max_n)

##l_n=[lambda i=i: i*10 for i in range(20)]
##for j in l_n:
##    print(j(), end=" ")


