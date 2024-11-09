t = True
while t ==True:  
    a= int(input("Введите число "))
    b = int(input("Введите степень "))
    for i in range(a-1):  
        i=i+1
        print(i,"= ",end="")
        print(i**b,end=", ")
    print(i+1,"= ",end="")
    print((i+1)**b,end=" ")
    print("\n")
    print("Хотите выйти? ")
    c= input("Да или Нет? ")
    if c=="Да":
        t=False
    
