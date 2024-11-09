####Превратить текст в список
text1 = "Hello my friend"
##text1 = list((text))
##print(text1)
#### Из списка в текст join
##print(",".join(text1))

a = ","  #с отступом
print(a.join(text1))
##
###split разделение то по которому делится оно исчезает
##t2=text.replace(" ",",")
##text1 = list(text.split(" "))
##print(len(text1))

import random
##n1 =[]
##for i in range(20):
##    a = chr(random.randint(97,122))
##    n1.append(a)
##print(n1)
##print(len(n1))
##print("".join(n1[::4]))
##
##b= random.randint(4,10)
##n1 =[]
##for i in range(b):
##    a = chr(random.randint(97,122))
##    n1.append(a)
##print(n1)
##print(len(n1))
##print("".join(n1))

## random pasword
##n1 =[]
##for i in range(20):
##    a = chr(random.randint(33,122))
##    n1.append(a)
##print("".join(n1))

# add text => list check value on num
##a = input()
##text_list = list(a)
##t_len=len(text_list)
##for i in range(t_len):
##    if (text_list[i].isdigit()):
##        int_a=int(text_list[i])
##        print(int_a)
##        print(type(int_a))

# Каждое числа возвести в степень
list_n=[5,10,11,7,0,14,3,1,21,22,18,3,15,27]
g_list = [i*i for i in list_n]
print(list_n)
print(g_list)

##list_n=[5,10,11,7,0,14,3,1,21,22,18,3,15,27]
##g_list = [i*i for i in list_n]
##g_list1 = [i*i for i in list_n if i%2==0]
##print(list_n)
##print(g_list)
##print(g_list1)

##list_list = ["Move","Play","Game","Map","Style"]
####g_list0 =[i.lower() for i in list_list if i =="Game"]
##g_list1 =[i.lower()*2 for i in list_list if len(i) ==3 or len(i)==5]
##print(g_list1)

##n1 =[]
##for i in range(20):
##    a = random.randint(10,99)
##    n1.append(a)
##print(n1)
##glist = [i for i in n1 if i%3==0 and i%7==0]
##print(glist)


