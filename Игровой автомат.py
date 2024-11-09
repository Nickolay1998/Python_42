import random
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
