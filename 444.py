import random
##g = [random.randint(65,90) for i in range(20)]
##d = ','.join(list(map(str,g)))
##p = ','.join(list(map(chr,g)))
####with open("C:/Users/admin/Desktop/Nums.txt","w") as f:
####    f.write(d)
####
####with open("C:/Users/admin/Desktop/Chr.txt","w") as c:
####    c.write(p)
##    
##with open("C:/Users/admin/Desktop/Nums.txt","r") as f:
##    print(f.read())
##
##with open("C:/Users/admin/Desktop/Chr.txt","r") as c:
##    print(c.read())    

        
##list_num=[random.randint(1,99) for i in range(20)]
##with open("C:/Users/admin/Desktop/Even.txt","w") as e:
##    e.write(' '.join([str(i) for i in list_num if i%2==0]))
##with open("C:/Users/admin/Desktop/Odd.txt","w") as o:
##    o.write(' '.join([str(i) for i in list_num if i%2!=0]))
##


##with open("C:/Users/admin/Desktop/testpython.txt","w") as f:
##    for i in range(5):
##        f.write("*"*5)
##        f.write("\n")
##with open("C:/Users/admin/Desktop/testpython.txt","r") as f:
##    print(f.read())
##----------------------------------------------------------------------------
##with open("C:/Users/admin/Desktop/testpython.txt","w") as f:
##    for i in range(10):
##        p = (" "*(i*1))
##        f.write(p+"*")
##        f.write("\n")
##with open("C:/Users/admin/Desktop/testpython.txt","r") as f:
##    print(f.read())
##УНИВЕРСАЛЬНАЯ ДИАГОНАЛЬ
##for i in range(10):
##    p = (" "*i)
##    print(p,"*")
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##print([a[i] for i in range(len(a)) if a[i]<5])
##print(list(filter(lambda i:i<5,a)))
##for i in a:
##    if i<5:
##        print(i,end="")
##----------------------------------------------
##Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
##print(list(set(a)&set(b)))
##print(list(filter(lambda elem: elem in b, a)))
##---------------------------------------------------
##Отсортируйте словарь по значению в порядке возрастания и убывания.
##dt_1 = {"p3":3,"p4":4,"p2":2,"p1":1}
##print(dict(zip(sorted(dt_1.keys()),sorted(dt_1.values()))))

##dict_a = {1:10, 2:20}
##dict_b = {3:30, 4:40}
##dict_c = {5:50, 6:60}
##
##dict_a.update(dict_b)
##dict_a.update(dict_c)
##print(dict_a)
##a = int(input())
##for i in range(a):
##    with open("C:/Users/admin/Desktop/22.txt","a") as f:   
##        f.write(" ".join(list(map(str,[chr(random.randint(65,90)) for i in range(10)])))+"\n")
##with open("C:/Users/admin/Desktop/22.txt","r") as f:
##    print(f.read())
    
##f = [' '.join([chr(random.randint(65,90)) for i in  range(a)]) for i in range(a)]
##print(f)
##
##g = [f[i]"\n" for i in range(a)]
##print(g)

##x = int(input("Новые показания света "))
##y = int(input("Старые показания света "))
##p = int(input("Новые показания воды "))
##k = int(input("Старые показания воды "))
##n = int(input("Квт "))
##u = int(input("Кбм "))
##z = int(input("Мусор "))
##xy = x-y
##pk = p-k

##nxy = xy*n
##upk = pk*u
##summ = nxy+upk+z
##print("Свет ",nxy)
##print("Вода ",upk )
##print("Мусор",z)
##print("Сумма",summ)
##my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}      
##print(sorted(my_dict, reverse=True)[:3])

##Нужно вывести первые n строк треугольника Паскаля.
##В этом треугольнике на вершине и по бокам стоят единицы,
##а каждое число внутри равно сумме двух расположенных над ним чисел.
##def pascal_triangle(n):
##   row = [1]
##   y = [0]
##   for x in range(max(n, 0)):
##      print(row)
##      row = [left + right for left, right in zip(row + y, y + row)]
##   
##pascal_triangle(6)

##Напишите проверку на то, является ли строка палиндромом. Палиндром —
##это слово или фраза, которые одинаково читаются слева направо и справа налево.
##a = input()
##if a==a[::-1]:
##    print(a,a[::-1],"Ok")
##else:
##    print("No")
##
##def is_palindrome(string):
##    return string == string[::-1]
##print(is_palindrome('abba')




##def convert(seconds):
##    days = seconds // (24 * 3600)
##    seconds %= 24 * 3600 # second%24*3600
##    hours = seconds // 3600
##    seconds %= 3600
##    minutes = seconds // 60 # seconds//60
##    seconds %= 60  # seconds%60
##    print(f'{days}:{hours}:{minutes}:{seconds}')
##
##convert(1234)

##a = input()
##numl = list(map(int,a.split(",")))
##print(numl[0],numl[-1])
##
##n = int(input())
##n2 = int(str(n)*2)
##n3 = int(str(n)*3)
##print(n+n2+n3)

##def solve(n):
##    n1 = n
##    n2 = int(str(n) * 2)
##    n3 = int(str(n) * 3)
##    print(n1 + n2 + n3)
##
##solve(1)
##Напишите программу, которая
##выводит чётные числа из заданного списка и останавливается, если встречает число 237.
##numbers = [    
##    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
##    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
##]
##
##for x in numbers:
##    if x == 237:
##        break
##    elif x % 2 == 0:
##        print(x)



