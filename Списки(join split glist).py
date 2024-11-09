##text = "Python Hello!"
##list_text = list((text))    #Из текста в список
##print(list_text)
##
### метод join
##print("".join(list_text)) #Из списка в теск
##print(",".join(list_text)) #то что в кавычках это разделитель который будет стоять после каждого элемента
####P,y,t,h,o,n, ,H,e,l,l,o
##a = ":"
##print(a.join(list_text))
####P:y:t:h:o:n: :H:e:l:l:o
##a = ":"*2
##print(a.join(list_text))
####P::y::t::h::o::n:: ::H::e::l::l::o
####-----------------------------
####a = input() 
####print(a.join(list_text))          #Можно через input задать разделитель какой хочешь
##
###метод split
####text2 = list(text.split(" "))
####print(text2)
####['Python', 'Hello']
##text3 = text.split(" ")
##print(text3)
####['Python', 'Hello']
##text4 = text.split("!")
##print(text4)
####['Python Hello', '']
##text5 = text.split("P")
##print(text5)
####['', 'ython Hello!']
##t = "2, Hello"
##t1 = t.replace(",","")
##print(t1)
##t2 = t1.split(" ")
##print(t2)

##t = "Hello my name is Nick"
##t2 = t.split(" ") # поставил пробел в скобки выведется все кроме пробела и в списке
##print(t2)
####['Hello', 'my', 'name', 'is', 'Nick']
import random
##n = []
##for i in range(20):
##    a = random.randint(65,90)  #генератор случайных слов
##    n.append(chr(a))
##print(n)
##print(len(n))
##print(n[::4])
##print("".join(n[::4]))

##n = []
##b = random.randint(4,10)
##for i in range(b):
##    a = random.randint(65,90)  #генератор случайных слов
##    n.append(chr(a))
##print("".join(n[::2]))
##print(len(n))

##n = []
##for i in range(20):
##    a = random.randint(33,122)  #генератор случайных паролей на 20 значений
##    n.append(chr(a))
##print("".join(n[::2]))

##t = input()
##l = list((t))
##print(l)
##for i in range(len(l)):     # Проверка на числа
##    if l[i].isdigit():
##        print(l[i],end=" ")
##        print(type(int(l[i])))
##----------------
##g = [t[i] for i in range(len(t)) if t[i].isdigit()]
##print(g)
##g2= [type(int(t[i])) for i in range(len(t)) if t[i].isdigit()]
##print(g2) #Проверка чисел через ГЕНЕРАТОР СПИСКОВ
##------------
#Генератор списков
## g = [result for i in.....{if } ]

##list_n=[5,10,11,7,0,14,3,1,21,22,18,3,15,27] # Вывести данные списка в квадрате
##g_list =[i*i for i in list_n ]
##print(list_n)
##print(g_list)
####[5, 10, 11, 7, 0, 14, 3, 1, 21, 22, 18, 3, 15, 27]
####[25, 100, 121, 49, 0, 196, 9, 1, 441, 484, 324, 9, 225, 729]
##
##list_n=[5,10,11,7,0,14,3,1,21,22,18,3,15,27] # Вывести данные списка в квадрате
##g_list =[i**2 for i in list_n ]
##print(list_n)
##print(g_list)
####[5, 10, 11, 7, 0, 14, 3, 1, 21, 22, 18, 3, 15, 27]
####[25, 100, 121, 49, 0, 196, 9, 1, 441, 484, 324, 9, 225, 729]

##list_n=[5,10,11,7,0,14,3,1,21,22,18,3,15,27] # Вывести данные списка в квадрате но только четные числа
##g_list =[i for i in list_n if i%2==0 ]
##g_list1 =[i*i for i in list_n if i%2==0 ]
##print(g_list)
##print(g_list1)
##[10, 0, 14, 22, 18]
##[100, 0, 196, 484, 324]

##list_list=["Movie","Play","Game","Map","Style"]
##g_list = [i.replace("M","m").replace("P","p") for i in list_list]
##g_list2 = [i.lower() for i in list_list]
##g_list3 = [i.upper() for i in list_list]
##g_list4 = [i.lower() for i in list_list if i =="Game"]
##g_list5 = [i.lower() for i in list_list if len(i) ==3]
##print(list_list)
####['Movie', 'Play', 'Game', 'Map', 'Style']
##print(g_list)
####['movie', 'play', 'Game', 'map', 'Style']
##print(g_list2)
####['movie', 'play', 'game', 'map', 'style']
##print(g_list3)
####['MOVIE', 'PLAY', 'GAME', 'MAP', 'STYLE']
##print(g_list4)
####['game']
##print(g_list5)
####['map']
##l = []
##for i in range(20):
##    a = random.randint(10,200)
##    l.append(a)
##print(l)
##gl = [i for i in l if i%3==0 and i%7==0]
##print(gl)
##[52, 21, 97, 52, 148, 134, 146, 149, 122, 109, 187, 62, 159, 102, 165, 156, 184, 105, 163, 188]
##[21, 105]

