import random
##n1 = []
##for i in range(30):
##    a = random.randint(65,90)
##    if a%2==0:
##        n1.append(a)
##print(n1)
##print(sum(n1))
##list_text = [chr(i) for i in n1]
##print(list_text)
##word_text=("".join(list_text))
##print(word_text)

list1 = [[1,2,3],[7,8,9]]
##s=0
##for i in range(len(list1)):
##    for j in range(len(list1[i])):
##       s = s+list1[i][j]
##       print(list1[i][j])
##print("Total",s)

##mat = [[list1[i][j] for j in range(len(list1[i]))] for i in range(len(list1))]
##print(mat) #Вывести матрицу через генератор списка
##

##a = []
##for i in range(3):
##    for j in range(3):
##        b = []
##        a.append(random.randint(10,50))
##    b.append(a)
##print(b)

##def name function (param,param):
##    <body function>
##def kvadrat():
##    a= int(input("a= "))
##    s=a*a
##    return s
##   
##def pryamo():
##    a= int(input("a= "))
##    b= int(input("b= "))
##    s=a*b
##    return s
##
##print("1 =S(kvadrat), 2 -s(pryamo)")
##c = int(input("Select number -"))
##if c==1:
##    print("s = ",kvadrat())
##elif c==2:
##    print("s = ",pryamo())
##else:
##    print("Error")

##def selectOne(a,b):
##    if a==0 and b!=0:
##        print("Winer Player1",a,b)
##    elif a%2!=0 and b%2==0:
##        print("Winer Player2",a,b)
##    elif a==0 and b==0:
##        print("Win - Win",a,b)
##    else:
##        print("Lose - Lose",a,b)
## 
##def selectTwo(a,b):
##        if a>b:
##                print("Winer Player1",a,b)
##        elif a<b:
##                print("Winer Player2",a,b)
##        else:
##                print("Win - Win",a,b)
## 
##def selectThree(a,b):
##        num=int(input("Enter number of 1 to 36\n"))
##        i=min(abs(num-a),abs(num-b))
##        if i==abs(num-a):
##            print("Winer Player1", a,b)
##        elif i==abs(num-Player2):
##            print("Winer Player2", a,b)
##        else:
##            print("Win - Win", a,b)
### main code
##Player1_cube1=random.randint(1,6)
##Player1_cube2=random.randint(1,6)
##Player1_cube3=random.randint(1,6)
##Player1_cube4=random.randint(1,6)
##Player1_cube5=random.randint(1,6)
##Player1_cube6=random.randint(1,6)
## 
##Player1=Player1_cube1+Player1_cube2+Player1_cube3+Player1_cube4+Player1_cube5+Player1_cube6
## 
##print(Player1)
## 
##Player2_cube1=random.randint(1,6)
##Player2_cube2=random.randint(1,6)
##Player2_cube3=random.randint(1,6)
##Player2_cube4=random.randint(1,6)
##Player2_cube5=random.randint(1,6)
##Player2_cube6=random.randint(1,6)
## 
##Player2=Player2_cube1+Player2_cube2+Player2_cube3+Player2_cube4+Player2_cube5+Player2_cube6
## 
##print(Player2)
## 
##a=int(input("Виберіть режим гри: \n1 - Even Odd \n2 - Sum (+) \n3 - Check number\n"))
## 
##if a==1:
##    selectOne(Player1,Player2)
##elif a==2:
##    selectTwo(Player1,Player2)
##elif a==3:
##    selectThree(Player1,Player2)

def rand_list():
    list_num=[]
    for i in range(20):
        num=random.randint(65,90)
        list_num.append(num)
    print(sum(list_num))
    if sum(list_num)%2==0:
        print("Even")
    else:
        print("Odd")
#------- main code ----------------

rand_list()
def rand_list():
    list_num=[]
    for i in range(3):
        num=random.randint(65,90)
        list_num.append(num)
    return list_num
#------- main code ----------------
a=rand_list()
print(a)
print(a[1])
