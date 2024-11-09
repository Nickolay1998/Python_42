##"C:/Users/admin/Desktop/.txt","r"
##f = open("C:/Users/admin/Desktop/Путь к питону.txt","w")
##w = f.write("Sasuke and Sakura")
##f.close()
##
##f = open("C:/Users/admin/Desktop/Путь к питону.txt","r")
##r = f.read()
##print(r)
##f.close
##-------------------------------------------------------------------------------
##a = "Hello"
##with open("C:/Users/admin/Desktop/Путь к питону.txt","w") as f:
##    w=f.write(a) 
##with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f:
##    r=f.read()
##    print(r)
##Hello
##-----------------------------------------------------------------------------
##with open("C:/Users/admin/Desktop/Путь к питону.txt","a") as f:
##    w=f.write("Hell"*2) 
##with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f:
##    r=f.read()
##    print(r)  
##HelloHello

##with open("C:/Users/admin/Desktop/Путь к питону.txt") as f:
##    r=f.read()
##    print(r)  
##Выведет то что в фале так как по умолчанию стоит режим r
##--------------------------------------------------------------------------------------
##with open("C:/Users/admin/Desktop/Путь к питону.txt","a") as f:
##    w=f.write(" Hell") 
##with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f:
##    r=f.read(3) # задаем количество символов которые мы хотим вывести
##    print(r)    
##-------------------------------------------------------------------------------------------------------------
##readlines() #Чтение по линиям

with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f:
    r=f.readlines() 
    print(r)
##['Hellо\n', 'Hell Hell\n', 'Fine\n', 'hi how are you'] # команда выводит слова в файле в виде списка
##через табуляцию он делает новый элемент списка  и пишет в конце элеменат \n
##----------------------------------------------------------------------------------------------------------------
##readline()       #читаем значения только в одной линии.
##with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f:
##    r=f.readline() 
##    print(r)
##------------------------------------------------------------------------------------
##with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f:
##    r=f.read() 
##    print(len(r))
##---------------------------------------------------------------------------
##можно работать с 2 файлами одновременно
##with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f,with open("C:/Users/admin/Desktop/Keylabs.txt","r") as f:
##--------------------------------------------------------------------------------
##Зависать в файл 10 раднмоных чисел
##import random
##with open("C:/Users/admin/Desktop/Путь к питону.txt","w") as f:    
####    w = f.write(",".join([str(i) for i in [random.randint(10,99) for i in range(10)]]))  # 1 вариант
##        w = f.write(",".join(list(map(str,[random.randint(10,99) for i in range(10)]))))
##with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f:
##    r = f.read()
##    print(r)
##------------------------------------------------------------------------------------------------------    
##Нужно сгенерировать  раз 5.После кода прожимаем F5 пять раз
import random
##with open("C:/Users/admin/Desktop/Путь к питону.txt","a") as f:    
##        w = f.write(",".join(list(map(str,[random.randint(10,99) for i in range(10)])))+"\n")
##with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f:
##    r = f.read()
##    print(r)

##40,37,19,50,39,65,21,56,91,99
## 1  раз F5

##40,37,19,50,39,65,21,56,91,99
##17,52,16,84,48,31,32,17,93,29
## 2 раз F5

##40,37,19,50,39,65,21,56,91,99
##17,52,16,84,48,31,32,17,93,29
##87,25,86,40,48,78,99,74,88,67
## 3 раз F5

##40,37,19,50,39,65,21,56,91,99
##17,52,16,84,48,31,32,17,93,29
##87,25,86,40,48,78,99,74,88,67
##31,20,39,50,77,11,26,74,89,62
## 4 раз F5

##40,37,19,50,39,65,21,56,91,99
##17,52,16,84,48,31,32,17,93,29
##87,25,86,40,48,78,99,74,88,67
##31,20,39,50,77,11,26,74,89,62
##24,17,94,48,49,85,19,44,65,79
##5 раз F5

##with open("C:/Users/admin/Desktop/Путь к питону.txt","r") as f:
##    r = f.read()
##    t = r.split()
##    l = ','.join(t)
##    s = l.split(",")
##    print(s)
##    print(sum([int(i) for i in s]))
    


    
    
    

  
    
    
    
    
    
   
   
   
    
    
    
    

