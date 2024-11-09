import random
##while "Игра": 
##    print(" Начать игру + \n Выход -")
##    a = input()
##    if a =="+" :
##        b = int(input())
##        c = int(input())
##        if b>3 or c>3:
##            print("Error")
##        else:
##            f = random.randint(0,3)
##            g = random.randint(0,3)
##            if b==f or c==g or b==g or c==f:
##                print(f,g,"You win")
##            else:
##                print(f,g,"You lose")
##    elif a=="-":
##        break
while "Игра": 
    print(" Начать игру + \n Выход -")
    a = input()
    if a =="+" :
        f = random.randint(0,3)
        g = random.randint(0,3)
        c = random.randint(0,3)
        if f==g==c:
            print(f,g,c,"Джекпот")
        else:
            print(f,g,c,"You lose")
    elif a=="-":
        break        
         
        

