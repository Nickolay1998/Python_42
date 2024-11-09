import random
##t=[]
##for i in range(30):
##    a= random.randint(65,90)
##    if a%2==0:
##        t.append(a)
##        print(chr(a),end="") #number => letter one word 1 вариант
##print("\n")
##print(t)
##print(sum(t))
##gl = [chr(i) for i in t]  #number => letter => one word 2 вариант
##print("".join(gl)) 

##l = []
##for i in range(30):
##    a= random.randint(65,90) #### Находим четные числа из списка через генератор
##    l.append(a)
##gl = [i for i in l if i%2==0] #Even
##print(gl) 
##print(sum(gl))
##p= [chr(i) for i in l if i%2==0]   #number => letter one word 1 вариант
##print("".join(p))
##
##d = [chr(i) for i in gl]  #number => letter one word 2 вариант
##print("".join(d))
##
##c = "".join([chr(i) for i in gl]) #number => letter one word 3 вариант
##print(c)
##
##y = "".join([chr(i) for i in [i for i in l if i%2==0]]) #number => letter one word 4 вариант
##print(y)
##                0          1
list_m = [[1,2,3],[7,8,9]]
##             0 1 2    0 1 2
##print(list_m[0][2]) #из первого списка показывает третий элемент
##3
##print(list_m[0])   
##[1, 2, 3]
##s=0
##for i in range(len(list_m)):
##    for j in range(len(list_m[i])):
##            s=s+list_m[i][j]
##print("Cумма = ",s)

##gl = [[list_m[i][j] for j in range(len(list_m[i]))] for i in range(len(list_m))]
##print(gl) # Вывод через генератор
####[[1, 2, 3], [7, 8, 9]]      

##random matrix  3*3 [[x,x,x],[x,x,x],[x,x,x]]
##a = []
##for i in range(3):
##    b= []
##    for j in range(3):
##        x = random.randint(10,50)
##        b.append(x)
##    a.append(b)
##print(a)
####[[46, 23, 42], [24, 24, 15], [26, 10, 41]]
##
##g_33 = [[random.randint(10,50) for j in range(3)] for i in range(3)] # черех генератор
##print(g_33)
####[[46, 23, 42], [24, 24, 15], [26, 10, 41]]       

##def namefunction(param,param):
##    body function
#Функция может выводит какой-то результат,можем просить функцию сделать какие-то вычисления
#и отдала дальше эти дальше эти вычисления
##def number_num():
##    print("Hell Python")
###main code (Где мы эту функцию вызываем)
##number_num()

##def print_text(): 
##    a = input("Name => ")   #Можно задавить доп параметр для дальнейших действий
##    print("Hello",a ,"!") 
##
###main code (Где мы эту функцию вызываем)
##print_text()

##def number_num(a,b,c):
##    r=a*2+b**2+c*10
##    print(r)
##
###main code
##x = int(input("a = "))
##y = int(input("b = "))
##z = int(input("c = "))
##number_num(x,y,z)

##def number_num(a,b,c):
##    r=a*2+b**2+c*10
##    return r #Если мы хотим после калькуляций дальше делала что-то

#main code
##x = int(input("a = "))
##y = int(input("b = "))
##z = int(input("c = "))
##print(number_num(x,y,z)) #Выведи то что вернет тебе эта функция
##13
##x = int(input("a = "))
##y = int(input("b = "))
##z = int(input("c = "))
##print(number_num(x,y,z)*2) #Можем работать с этой функцией например умножить на 2 потому что
## возвращает
##26

##def f():
##    n = []
##    for i in range(20):
##        a=random.randint(10,50) #Вариант 1 
##        n.append(a)
##    return n
###main code
##print(sum(f()))
##if sum(f())%2==0:
##    print("Even")
##else:
##    print("Odd")
##------------
##def f():
##    n = []
##    for i in range(20):
##        a=random.randint(10,50) #Вариант 2
##        n.append(a)
##    print(sum(n))
##    if sum(n)%2==0:
##        print("Even")
##    else:
##        print("Odd")
##f()
    
##def rand_list():
##    list_num=[]
##    for i in range(3):
##        num=random.randint(65,90)
##        list_num.append(num)
##    return list_num
###------- main code ----------------
##a=rand_list()
##print(a)
##print(a[1])

###Или

##def rand_list():
##    list_num=[]
##    for i in range(3):
##        num=random.randint(65,90)
##        list_num.append(num)
##    return list_num
###------- main code ----------------
##
##print(rand_list())
##print(rand_list()[1])



