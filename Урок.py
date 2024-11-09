##                  C:\.....\file_name.txt,r
##file_text= open(file_name,mode)
##r+ -> read+write
##w+ =>  read+write
##a+ =>  read+append
# rb => чтение двуичного файла
##режим чтения по умолчанию
##file_text.close()
##
##with open(file_name,mode) as file_text:
##    <body file>
##-------------------------------------------------------------
##C:\Users\admin\Desktop
##file_text=open("C:/Users/admin/Desktop/testpython.txt","r")
##f_read = file_text.read()
##print(f_read)
##file_text.close()

##with open("C:/Users/admin/Desktop/testpython.txt","r") as file_text:
##    f_read = file_text.read()
##    print(f_read)
    
##with open("C:/Users/admin/Desktop/testpython.txt","a") as file_text:
##       file_text.write("Hello")
##       
##       
##with open("C:/Users/admin/Desktop/testpython.txt","r") as file_text:
####    file_text.write("Hello")
##       f_read = file_text.read()
##       print(f_read)

##with open("C:/Users/admin/Desktop/testpython.txt","r") as file_text:
##       f_read = file_text.read(10) #Количество символов которые мы хотим увидеть в скобках
##       print(f_read)

##with open("C:/Users/admin/Desktop/testpython.txt","w") as file_text:
##    file_text.write("Hello")
##
##with open("C:/Users/admin/Desktop/testpython.txt","r") as file_text:
##       f_read = file_text.read()
##       print(f_read)
##Hello
##-----------------------------------------------------------
##readlines() #прочитать текст по линиям

##with open("C:/Users/admin/Desktop/testpython.txt","r") as file_text:
##    f_read = file_text.readlines()
##    print(f_read)

##['Hello python!!! Hello user!!\n', 'Hello user!!!\n', 'Let`s start work on programm.']
##-----------------------------------------------------------------------------------
##with open("C:/Users/admin/Desktop/testpython.txt","r") as file_text:
##    f_read = file_text.readlines()
##    print(type(f_read))
##<class 'list'>
##-------------------------------------------------------------
##with open("C:/Users/admin/Desktop/testpython.txt","r") as file_text:
##    f_read = file_text.readline() # прочитает только 1 одну линию
##    print(f_read)
##Hello python!!!   
##-----------------------------------------------
##with open("C:/Users/admin/Desktop/testpython.txt","r") as file_text:
##    f_read = file_text.read() 
##    print(len(f_read)) # покажет количество символов
##75
##-------------------------------------------------------
##with open("file_name","r") as file_text,with open("file_name","2") as file_text:
##работа с двумя файлами одновременно
##import random
##with open("C:/Users/admin/Desktop/testpython1.txt","w") as file_text:
##    print(' '.join(list(map(str,[random.randint(10,99) for i in range(10)]))))
##----------------------------------------------------------
##import random
##with open("C:/Users/admin/Desktop/testpython1.txt","w") as file_text:
##    #file_read=file_text.read()
##    list_num=[random.randint(10,99) for i in range(10)]
##    list_str=list(map(str,list_num))
##    str_list=", ".join(list_str)
##    file_text.write(str_list)
##    #file_read=file_text.read()
##    #print(file_read)
##-------------------------------------------------------------- 
import random
with open("C:/Users/admin/Desktop/testpython1.txt","a") as file_text:
   #file_read=file_text.read()
    list_num=[random.randint(10,99) for i in range(10)]
    list_str=list(map(str,list_num))
    str_list=", ".join(list_str)
    file_text.write(str_list)
    #file_read=file_text.read()
    #print(file_read)
  

##with open("C:/Users/admin/Desktop/testpython1.txt","r") as file_text:
##    file_read=file_text.read()
##    list_text=file_read.split()
##    ln=[int(i.replace(",","")) for i in list_text]
##    print(sum(ln))
##    list_map=list(map(lambda i: int(i.replace(",","")),list_text))
##    print(list_map)
   
   
