
tuple1 = ("admin","user","superadmin","superuser")
tuple2 = tuple((1,2,3,4,5))
##print(tuple1)
##
##print(tuple2)
##
##print(tuple1[2])
##
##print(tuple2[1])
##
##print(len(tuple1))
##
##print(max(tuple2))
##
##print(sum(tuple2))
##
##for i in range(len(tuple1)):
##    print(tuple1[i])

##user1,*users,user4 = tuple1 #присвоение
##print(user1)
##print(users)
##print(user4)
####admin
####['user', 'superadmin']
####superuser

##i0,i1= tuple2  Выведет ошибку потому что в кортеже 5 значений а ты вывел только 2
##print(i0)
##print(i1)

##admin
##['user', 'superadmin', 'superuser']

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

##Задача вычеслить сколько раз встречается любой елемент списка
##print(tuple1.count("admin"))
##print(tuple1.count("user"))
##print(tuple1.count("admin"))
##print(tuple1.count("superadmin"))
##print(tuple1.count("superuser"))

##for i in range(len(tuple1)):
##    print(tuple1.count(tuple1[i]))
##Кортеж меньше нагрузки берет чем список,он постоянный данные не меняются,стабильный набор данных
##защищенность данных_________________________________________
##Множества
set1 = {1,2,3,3,3,4,4,5}
set2 = set((1,2,3))

##print(type(set1))
##print(type(set2))
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
##set1 = {1,2,3,4,5}
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
##[15, 18, 17, 15, 15, 18, 13, 20, 14, 20, 16, 11, 19, 10, 18, 12, 17, 19, 20, 20]
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

##dict
##{key1:value1,key2:value2}
##dic_text1 = {"Game":1,"Play":2,"Level":3,"Start":10}
##print(dic_text)

#list=>dixt
##d_list = dict([["Game",1],["Play",2],["Level",3]])
##print(d_list)
##
### tuple=>dict
##dt_tuple=dict([("Game",1),("Play",2),("Level",3)])

#2 symbols = len =2
##dt_2s=dict(["G1","P2","L3","S5"])
##print(dt_2s)
##
#zip function
##keylist = ["Game","Level","Start"]
##valuelist = [1,2,3,10]
##dt_zip = dict(zip(keylist,valuelist))
##print(dt_zip)
#ключи не могут повторятся,индексация тольок по ключу
dt_1 = {"p1":"Movie","p2":"Sci-Fi","p3":"Star wars","p4":2019,"p5":"Part 7"}
dt_2 = {"p2":"Horror","p4":2017,"p6":"USA,UK"}
##print(dt_1["p1"])
##print(dt_1["p2"])
##print(dt_1["p5"])
##Movie
##Sci-File
##Part 7                                      выведет значение ключа

##if "p2" in dt_1:
##    print("Yes")
##else:
##    print("No") 
##Yes                   проверка, есть ли такой ключ?

##for i,j in dt_1.items():
##    print(i,j)
##p1 Movie
##p2 Sci-Fi                   Можем увидеть параметры всего словаря ключи и значения
##p3 Star wars
##p4 2019
##p5 Part 7

##for i,j in dt_1.items():
##    print(type(i),type(j))
##              key i     value j
##<class 'str'> <class 'str'>
##<class 'str'> <class 'str'>
##<class 'str'> <class 'str'>
##<class 'str'> <class 'int'>
##<class 'str'> <class 'str'>

##dt_1["p6"]=100      Добавляет параметр
##print(dt_1)
##{'p1': 'Movie', 'p2': 'Sci-Fi', 'p3': 'Star wars', 'p4': 2019, 'p5': 'Part 7', 'p6': 100}

##dt_1["p4"]=100      #Меняет параметр
##print(dt_1)
##{'p1': 'Movie', 'p2': 'Sci-Fi', 'p3': 'Star wars', 'p4': 100, 'p5': 'Part 7'}

##dt_1["p4"]=2019      #Можно вернуть обратно р4 старый ключ
##print(dt_1)
##{'p1': 'Movie', 'p2': 'Sci-Fi', 'p3': 'Star wars', 'p4': 2019, 'p5': 'Part 7'}

##print(dt_1.get("p1"))       ####получаем значение
##print(dt_1["p1"])
##Movie
##Movie

##for i in dt_1:
##    print(dt_1.get("p1"))
##Movie
##Movie
##Movie
##Movie
##Movie

##for i in dt_1:
##    print(dt_1["p1"])
##Movie
##Movie
##Movie
##Movie
##Movie

##dt_1.update([("p1","Game"),("p4",2020)])      
##print(dt_1)        #можем менять нескольно параметров
##{'p1': 'Game', 'p2': 'Sci-Fi', 'p3': 'Star wars', 'p4': 2020, 'p5': 'Part 7'}
##
##print(dt_1)
##dt_1.update(dt_2) #Можем обновить словарь
##print(dt_1)
##{'p1': 'Game', 'p2': 'Horror', 'p3': 'Star wars', 'p4': 2017, 'p5': 'Part 7', 'p6': 'USA,UK'}

##del dt_1["p6"]      #Удаляет указаный элемент
##print(dt_1)

##dt_1.clear()
##print(dt_1)        #удаляет все
##{}

##print(dt_1.keys())
####dict_keys(['p1', 'p2', 'p3', 'p4', 'p5'])
##
##key_list=list(dt_1.keys())                                  #Выводит ключи
##print(key_list)
####['p1', 'p2', 'p3', 'p4', 'p5']

##print(dt_1.values())
####dict_values(['Movie', 'Sci-Fi', 'Star wars', 2019, 'Part 7'])
##
##value_list=list(dt_1.values())                                  #Выводит значения
##print(value_list)
##['Movie', 'Sci-Fi', 'Star wars', 2019, 'Part 7']

##key_value_list=list(dt_1.items())
##print(key_value_list)
##[('p1', 'Movie'), ('p2', 'Sci-Fi'), ('p3', 'Star wars'), ('p4', 2019), ('p5', 'Part 7')]

##dt_1.pop("p1")   # удаляет конкретный элемент
##print(dt_1)

##dt_2=dt_1.copy()
##print(dt_2)
##{'p1': 'Movie', 'p2': 'Sci-Fi', 'p3': 'Star wars', 'p4': 2019, 'p5': 'Part 7'}

##dt_2=dt_1.copy()
##dt_2["p6"]=200
##print(dt_1,"copy")
##print(dt_2,"copy")
##{'p1': 'Movie', 'p2': 'Sci-Fi', 'p3': 'Star wars', 'p4': 2019, 'p5': 'Part 7'} copy
##{'p1': 'Movie', 'p2': 'Sci-Fi', 'p3': 'Star wars', 'p4': 2019, 'p5': 'Part 7', 'p6': 200} copy

##Список со словарями
##users_list=[
##{"name":"Jack","role":"admin","year":2010,"salare":120},
##{"name":"Anna","role":"superadmin","year":2015,"salare":130},
##{"name":"Mark","role":"user","year":2022,"salare":60},
##{"name":"Dan","role":"view","year":2019,"salare":100}]
##print(users_list)
##print(users_list[1]) находим по индексу

#salary >80
##users_salary = list(filter(lambda i: i["salare"]>80 and i["year"]>2017,users_list))
##print(users_salary)
##[{'name': 'Dan', 'role': 'view', 'year': 2019, 'salare': 100}]

##for a in users_salary:
##    for i,j in a.items():
##        print(i," ",j)
##name   Dan
##role   view
##year   2019
##salare   100

##sort_salary=sorted(users_list,key=lambda i:i["salare"])
##print(sort_salary)
##
##for a in sort_salary:
##    for i,j in a.items():
##        print("{}:{}".format(i,j))

##name:Mark
##role:user
##year:2022
##salare:60
##name:Dan
##role:view
##year:2019
##salare:100
##name:Jack
##role:admin
##year:2010
##salare:120
##name:Anna
##role:superadmin
##year:2015
##salare:130

##sort_year=sorted(users_list,key=lambda i:i["year"])
##print(sort_year)

# user => superuser
#viewer => user
#superadmin => admin

##users_list=[
##{"name":"Jack","role":"admin","year":2010,"salare":120},
##{"name":"Anna","role":"superadmin","year":2015,"salare":130},
##{"name":"Mark","role":"user","year":2022,"salare":60},
##{"name":"Dan","role":"view","year":2019,"salare":100}]
##
##users_list[3].update(([("role","user")]))
##print(users_list)
##
##users_list[2]["role"]="superuser"
##users_list2=users_list.copy()
##print(users_list2,"new")
##
##users_list3 = users_list2[0]["salare"]=150
##users_list3 = users_list2.copy()
##print(users_list3)


##def l():
##    if "login1" and "login2" in users:
##        print("Yes")
##    else:
##        print("No")
##
##def p():
##    if "pass1" and "pass2" in users:
##        print("Yes")
##    else:
##        print("No")
##
##users = {"login1":"admin", "pass1":1111, "login2":"user", "pass2":2222}
##l()
##p()

##log_pass={"login1": "admin", "pass1":1111, "login2": "user", "pass2":2222}
## 
##value_list=list(log_pass.values())
##print(value_list)
## 
##a=input("login =")
##b=int(input("pass="))
## 
## 
##if a in value_list:
##    if b==value_list[value_list.index(a)+1]:
##        print("yes")
##    else:
##        print("Error pass")
##else:
##    print("no user in system")


##def log_pass(a,b):
##    log_pass={"login1": "admin", "pass1":1111, "login2": "user", "pass2":2222}
##    value_list=list(log_pass.values())
## 
##    if a in value_list:
##        #print("yes")
##        #print(value_list.index(a)+1)
##        if b==value_list[value_list.index(a)+1]:
##            print("yes")
##        else:
##            print("Error pass")
##    else:
##        print("no user in system")
##
##a=input("login =")
##b=int(input("pass="))
##log_pass(a,b)

##log_pass={"login1": "admin", "pass1":1111, "login2": "user", "pass2":2222}
##value_list=list(log_pass.values())
##print(value_list)














##[{'name': 'Jack', 'role': 'admin', 'year': 2010, 'salery': 120}, {'name': 'Anna', 'role': 'superadmin', 'year': 2015, 'salery': 130}, {'name': 'Mark', 'role': 'user', 'year': 2022, 'salery': 60}, {'name': 'Dan', 'role': 'view', 'year': 2019, 'salery': 100}]
##json ФАЙЛ
##json
##    user1:"name":"Jack",
##            "role":"admin",
##            "year":2010,
##            "salery":120
    
