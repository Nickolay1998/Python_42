a = input()
j = int(input("Индекс "))
for i in range(len(a)):
    if j==0:
        print(a[i].replace(a[j],"#"))
    elif j==1:
        print(a[i].replace(a[j],"*"))
        
