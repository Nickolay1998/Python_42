##list1 = [18,23,45,"Hell","Game",23,"Stpo"]
##n_l = list(filter(lambda i: i if str(i).isdigit()==True else False,  list1))
##print(n_l)

##list_num=[1,4,5,11,8,9,21,10,-15]
####l = list(map(lambda i: i+1 if i%2==0 else i-1,  list_num))
####print(l)
###map(функция,значения) работает с каждым значением
##
##k = list(map(lambda i: str(i), list_num))
##print(k)
##for i in range(len(k)):
##    print(type(k[i]))

import random
##g = [random.randint(-20,20) for i in range(15)]
##print(g)
##f_g = list(filter(lambda i: i>0, g))
##print(f_g)

####reduce  может обьеденить все элементы списка из этой кучи получить число
##reduce  => sum
##
##g = list(filter(lambda i: i%2==0,k))
##h = [chr(i) for i in g]
##print(h)

##gl = [random.randint(1,100) for i in range(30)]
##f_gl = list(filter(lambda i: i>=65 and i<=90,gl ))   генератор случайных слов
##new_list = [chr(i) for i in f_gl]
##print("".join(new_list))
##CPTWERYY

##gl = [random.randint(1,100) for i in range(30)]
##f_gl = list(filter(lambda i: i>=65 and i<=90,gl ))   #генератор случайных слов
##new_list = list(map(lambda i: chr(i),f_gl))
##print("".join(new_list))
##def f():
##    a = sum(even_list)
##    b = sum(odd_list)
##    if a>b:
##        print("even>odd")
##    else:
##        print("even<odd")
##
##list_num =[11,15,17,1,2,8,9,36,41,47,48,24,51,7,27,31,74,78,81,16,33,56,90,97,94,20,13,8,6,64]
##even_list = list(filter(lambda i: i%2==0,list_num))
##odd_list = list(filter(lambda i: i%2!=0,list_num))
##print(sum(even_list))
##print(sum(odd_list))
##
##f()

##def sum_1(a):
##    list_ev=list(filter(lambda i: i%2==0 ,list_1))
##    print(list_ev)
##    list_od=list(filter(lambda i: i%2!=0 ,list_1))
##    print(list_od)
##    a=sum(list_ev)
##    b=sum(list_od)
##    if a>b:
##        print ('list_ev>list_od')
##        print ("sum_a = ", a,"  sum_b = ",b)
##    else:
##        print ('list_od>list_ev')
##        print ("sum_a = ", a,"  sum_b = ",b)
###------
##list_1=[11,15,17,1,2,8,9,36,41,47,48,24,51,7,27,31,74,78,81,16,33,56,90,97,94,20,13,8,6,64]
##sum_1(list_1)

##text ="The Python is a new language for us. So, we started learning it a few months ago."
##list_text = list((text))
##list_text.remove("e")
##list_text.remove("o")
##list_text.remove("y")
##list_text.remove("i")
##list_text.remove("u")
##list_text.remove("a")
##print("".join(list_text))
##list_new = (list(filter(lambda i: i!="P" and i!="y",text)))
##print("".join(list_new))

##text="The 1 position of our order is most important then 2. Please check 1 and 1 and 1 for us."
##new_text=text.replace("1","first").replace("2","second")
##print(new_text)
## 
##list_text=list((text))
##list_letter=list(filter(lambda i: str(i).isalpha() ,list_text))
##print(list_letter)
##list_num=list(map(lambda i: ord(i),list_letter))
##print(sum(list_num))
##
##def Decorator(a): #Welcome
##    print("Hello User")
##    def Text():
##        print("Code starts working...")
##        a() #Welcome()
##        print("OK")
##    return Text
## 
##def Decorator1(a): #Welcome
##    print("Good job")
##    def Text():
##        print("Python Code working...")
##        a() #Welcome()
##        print("Finish")
##    return Text
## 
## 
##@Decorator
##@Decorator1
##def Welcome():
##    print("Welcome")
 
 
##Welcome()

##def even_odd(func):
##    if func()%2==0:
##        print('Even')
##    else:
##        print('Odd')
## 
## 
##@even_odd
##def startnumber():
##    a=random.randint(1,1000)
##    print(a)
##    return a

##def even_odd(func):
##    a=func()
##    if a%3==0:
##        print("Yes, 3 ")
##    else:
##        print("No, 3 ")
## 
## 
##@even_odd
##def startnumber():
##    a=random.randint(1,1000)
##    print(a)
##    return a

##def even_odd(func):
##    a=func()
##    if a%2==0:
##        print("Even")
##    else:
##        print("Odd")
##def lennumber(func):
##    print(len(str(func())))
##
##
##@even_odd
##@lennumber
##def startnumber():
##    a=random.randint(1,1000)
##    print(a)
##    return a 

##def decorator(a):
##    if a()%2==0 :
##        print("even")
##    else:
##        print("Odd")
##    return a
##def decorator1(a):
##    return len(str(a))
## 
##@decorator
##@decorator1
##def welcome():
##    a=random.randrange(1,1000)
##    return a
##
##print(welcome())
tuple1 = ("admin","user","superadmin","superuser")
tuple2 = tuple((1,2,3,4,5))
##print(tuple1)

##print(tuple2)

##print(tuple1[2])

##print(tuple2[1])

##print(len(tuple1))

##print(max(tuple2))

##print(sum(tuple2))

##for i in range(len(tuple1)):
##    print(tuple1[i])

##user1,*users,user4 = tuple1 #присвоение
##print(user1)
##print(users)
##print(user4)
####admin
####['user', 'superadmin']
####superuser

##user1,user2,user3,user4 = tuple1 #присвоение
##print(user1)
##print(user2)
##print(user3)
##print(user4)
####admin
####user
####superadmin
####superuser

##if "admin" in tuple1:       #Проверить есть ли элемент в кортеже
##    print("yes")
##else:
##    print("no")
##
##a = input()
##if  a in tuple1:       #Проверить есть ли элемент в кортеже
##    print("yes")
##else:
##    print("no")

##print(tuple1.count("admin"))
##1
##print(tuple1.index("admin"))
##0
##tuple11 = tuple1+tuple1
##print(tuple11)
####('admin', 'user', 'superadmin', 'superuser', 'admin', 'user', 'superadmin', 'superuser')

##print(tuple1.count("admin"))
##print(tuple1.count("user"))
##print(tuple1.count("admin"))
##print(tuple1.count("superadmin"))
##print(tuple1.count("superuser"))

##for i in range(len(tuple11)):
##    print(tuple11[i], tuple11.count(tuple11[i]))
##_________________________________________
set1 = {1,2,3,3,3,4,4,5}
set2 = set((1,2,3))

##print(type(set1))
##print(type(set2))
##print(set1)
##print(set2)
##print(set1)
##print(set2)

#intersection  & позволяет увидеть элементы которые есть у каждых множествах
##{1,2,3,4,5} {2,3,6}
##{2,3}
##set1 = {1,2,3,4,5}
##set2 = {2,3,6}
###& | -
##print(set1&set2)
##print(set1.intersection(set2))
##{2, 3}
##{2, 3}

#union => |
##set1 = {1,2,3,4,5}
##set2 = {2,3,6}
##set12 = {1,2,3,4,5,6}
##print(set1|set2)
##print(set1.union(set2))
##{1, 2, 3, 4, 5, 6}
##{1, 2, 3, 4, 5, 6}

#difference - покажет значения не у того не у другого
##set1 = {9,8,1,2,3,4,5}
##set2 = {2,3,6}
##set12 = {1,4,5,6}
##print(set1-set2)
##print(set1.difference(set2))
##{1, 4, 5}
##{1, 4, 5}
##print(set2-set1)
##print(set2.difference(set1))
##{6}
##{6}
##print(set1.symmetric_difference(set2))
##{1, 4, 5, 6}
##for i in set1:
##    print(i)
##1
##2
##3
##4
##5
##for i in set1:
##    print("Yes")
##else:
##    print("No")

##set1.add(8)
##print(set1)        ДОБАВЛЯЕТ ЕЛЕМЕНТ
##{1, 2, 3, 4, 5, 8}

##set1.update([2,8,9],{9,8,7})
##print(set1)
##{1, 2, 3, 4, 5, 7, 8, 9}
##set1.remove(1)
##print(set1)
##{2, 3, 4, 5}

##set1.discard(11) # не выдает ошибки если запишешь число которого нет в во множестве
##print(set1)
##{1, 2, 3, 4, 5}

##print(sorted(set1,reverse=True))
##[9, 8, 5, 4, 3, 2, 1]
##print(len(set1))
##print(max(set1))
##print(min(set1))
##print(sum(set1))

##for i,j in enumerate(set1):
##    print(i,j)
##    0 1
##1 2
##2 3
##3 4
##4 5
##5 8
##6 9
##setf1=frozenset((set1))
##print(sum(setf1)) #будет работать другие команды не будут работать
##frozenset({1, 2, 3, 4, 5, 8, 9})

#Особенность удаление дубликатов

##list_number= [random.randint(10,20) for i in range(20)]
##print(list_number)
##l=list(set(list_number))
##print(l)
##print(tuple(set(list_number)))
##15, 18, 17, 15, 15, 18, 13, 20, 14, 20, 16, 11, 19, 10, 18, 12, 17, 19, 20, 20]
##{10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
t ="Our online English classes feature lots of useful learning materials and activities to help you develop your reading skills with confidence in a safe and inclusive learning environment. Practise reading with your classmates in live group classes, get reading support from a personal tutor in one-to-one lessons or practise reading by yourself at your own speed with a self-study course."
##t2 = t.lower()
##t_f =list(filter(lambda i: i!="." and  i!="," and i!=" " and i!="-" and i!=":" and i!="'",t2))
##print("".join(t_f)) 
##print(set(t_f))
##print(len(set(t_f)))

##text1=list(set(text.lower()))
##text2=list(filter(lambda i: i!=','and i!=' ' and i!=':' and i!="'" and i!='"' and i!="." and i!='-',text1))
##print(text2)
##print(sorted(text2),"  ", len(text2))
