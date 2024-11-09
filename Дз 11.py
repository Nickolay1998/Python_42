##import random
##n = []
##a = random.randint(0,10)
##for i in range(a+1):
##    b = random.randint(50,60)
##    n.append(b)
##print(n)
##print("Сумма числе = ",sum(n))
##print("Максимальное число = ",max(n))
##print("Минимальное число = ",min(n))
##n.sort(reverse=True)
##print("Сортировка по убиванию = ",n)
##n2 = [i for i in n if i%3==0 or i%7==0]
##print(n2)
##print("Сумма чисел из интервала /3 и /7 = ",sum(n2))
##print("Среднее значение = ",round(sum(n)/len(n),1))
##a ="Python is a popular programming language known for its simplicity and readability. It has a wide range of applications and is used for web development, data analysis, artificial intelligence, and more. Python's extensive libraries and frameworks make it highly versatile, and its beginner friendly syntax allows new programmers to quickly learn and start coding. Its community-driven approach and vast resources make Python a go-to language for both beginner and experienced developers."
####print("Общее количество символов = ",len(a))
##b = a.replace(".","").replace(",","")
##list1 = b.split(" ")
####print(list1)
##print("Cлова длинна которых больше 8")
##for i in range(len(list1)):
##    if  len(list1[i])>8:
##        print(list1[i],end=" ")
##print("\n")
##g0 = [i for i in list1 if len(i)>8] #Через генератор вариант 1
##print(" ".join(g0))
##print("\n")
##g = [list1[i] for i in range(len(list1)) if len(list1[i])>8] #Через генератор вариант 2
##print(" ".join(g))
##print("\n")
##print("Cлова длинна которых равна либо 4 и меньше 8")
##for i in range(len(list1)):
##    if  len(list1[i])<8 or len(list1[i])==4:
##        print(list1[i],end=" ")
##print("\n")
##g1 = [list1[i] for i in range(len(list1)) if len(list1[i])<8 or len(list1[i])==4] #через генератор
##print(" ".join(g1))
##print("\n")
##print("Сколько End = ",list1.count("and"))
##print("Сколько слов = ",len(list1))
##s=0
##j=0
##for i in range(len(a)):
##    if a[i]=="P":
##        s=s+1
##    if a[i]=="p":
##        j=j+1
##print("Количество P = ",s)
##print("Количество p = ",j)
##s=0
##j=0


