##1.Пользователь с клавиатуры вводит элементы списка:
##Необходимо найти:
##a) Сколько раз число 2 присутствует в списке (необходимо при расчетах считать числа по модулю);
##list1 = [2, 0, 1, 2, 5, 7, 8, -2, -3, -8, 2, 10, 15, 4, 4, 11, 0, 0, -10, -5, 3, 3, 7, 7, 20]
##list2= []
##for i in range(len(list1)):
##    s = abs(list1[i])
##    list2.append(s)
##print(list2.count(2))

##b) Покажите максимальное число из списка;

##list1 = [2, 0, 1, 2, 5, 7, 8, -2, -3, -8, 2, 10, 15, 4, 4, 11, 0, 0, -10, -5, 3, 3, 7, 7, 20]
##print(max(list1))

##c) Покажите минимальное число из списка;
##list1 = [2, 0, 1, 2, 5, 7, 8, -2, -3, -8, 2, 10, 15, 4, 4, 11, 0, 0, -10, -5, 3, 3, 7, 7, 20]
##print(min(list1))

##d) Сделайте сортировку;

##list1 = [2, 0, 1, 2, 5, 7, 8, -2, -3, -8, 2, 10, 15, 4, 4, 11, 0, 0, -10, -5, 3, 3, 7, 7, 20]
##list1.sort()
##print(list1)

##e) Посчитайте количество отрицательных чисел;

##list1 = [2, 0, 1, 2, 5, 7, 8, -2, -3, -8, 2, 10, 15, 4, 4, 11, 0, 0, -10, -5, 3, 3, 7, 7, 20]
##list2= []
##for i in range(len(list1)):
##    if list1[i]<0:
##        list2.append(list1[i])
##        print(list1[i],end=" ")
##print("\n")
##print("Количество чисел",len(list2)) 

####f) Посчитайте количество положительных чисел;
##list1 = [2, 0, 1, 2, 5, 7, 8, -2, -3, -8, 2, 10, 15, 4, 4, 11, 0, 0, -10, -5, 3, 3, 7, 7, 20]
##list2= []
##for i in range(len(list1)):
##    if list1[i]>=0:
##        list2.append(list1[i])
##        print(list1[i],end=" ")
##print("\n")
##print("Количество чисел",len(list2))
##g) Посчитайте количество нулей 0.
##list1 = [2, 0, 1, 2, 5, 7, 8, -2, -3, -8, 2, 10, 15, 4, 4, 11, 0, 0, -10, -5, 3, 3, 7, 7, 20]
##print(list1.count(0))

##2.Пользователь с клавиатуры вводит элементы списка:
##Необходимо найти:
##a) Сумму всех чисел входящих в список;
##print(sum(list2))

####b) Количество элементов входящих в список;
##list2 = [5, 0, 1, 5, 10, 11, 15, 3, 18, 7, 2, 10, 8, 21, 19, 36, 5, 47]
##print(sum(list2))

####c) Среднее значение элементов списка;

##list2 = [5, 0, 1, 5, 10, 11, 15, 3, 18, 7, 2, 10, 8, 21, 19, 36, 5, 47]
##print(round(sum(list2)/len(list2),1))
##a=sum(list2)
##b=len(list2)
##print(a/b)

##d) Показать все четные значения списка;

##list2 = [5, 0, 1, 5, 10, 11, 15, 3, 18, 7, 2, 10, 8, 21, 19, 36, 5, 47]
##list3= []
##for i in range(len(list2)):
##    if (list2[i])%2==0:
##        list3.append(list2[i])
##print(list3) 

##e) Показать все нечетные значения списка.
##list2 = [5, 0, 1, 5, 10, 11, 15, 3, 18, 7, 2, 10, 8, 21, 19, 36, 5, 47]
##list3= []
##for i in range(len(list2)):
##    if (list2[i])%2!=0:
##        list3.append(list2[i])
##print(list3) 

##3. Пользователь с клавиатуры вводит элементы списка:
##Необходимо найти:
##a) Сортировку списка;

##list3 = ["Car","Cat","Dog","Word","Street","Tree","Free","Tax","House","Second","First","Lamp","Year","Join","Jump","Ice","Brother","Free","Word","Year","Page"]
##list3.sort()
##print(list3)

##b) Количество элементов входящих в список;
##list3 = ["Car","Cat","Dog","Word","Street","Tree","Free","Tax","House","Second","First","Lamp","Year","Join","Jump","Ice","Brother","Free","Word","Year","Page"]
##print(len(list3))

##c) Показать каждый третий элемент списка [“Car”,”Word”, ….];
##list3 = ["Car","Cat","Dog","Word","Street","Tree","Free","Tax","House","Second","First","Lamp","Year","Join","Jump","Ice","Brother","Free","Word","Year","Page"]
##print(list3[::3])

##d) Добавить к списку такие элементы “Play”,”Game”,”Movie”, “Star”;
##list3 = ["Car","Cat","Dog","Word","Street","Tree","Free","Tax","House","Second","First","Lamp","Year","Join","Jump","Ice","Brother","Free","Word","Year","Page"]
##list3.extend(["Play","Game","Movie","Star"])
##print(list3)

##e) Удалить из списка “First”,”Year”,”Ice”,”Street”;
##list3 = ["Car","Cat","Dog","Word","Street","Tree","Free","Tax","House","Second","First","Lamp","Year","Join","Jump","Ice","Brother","Free","Word","Year","Page"]
##list3.remove("First")
##list3.remove("Year")
##list3.remove("Ice")
##list3.remove("Street")
##print(list3)

##f) Показать список в обратном порядке;
##list3 = ["Car","Cat","Dog","Word","Street","Tree","Free","Tax","House","Second","First","Lamp","Year","Join","Jump","Ice","Brother","Free","Word","Year","Page"]
##print(list3[::-1])

##g) Создать список, который будет состоять из элементов под индексами 2, 5, 7, 10, 15, 17, 19, 20.
##list3 = ["Car","Cat","Dog","Word","Street","Tree","Free","Tax","House","Second","First","Lamp","Year","Join","Jump","Ice","Brother","Free","Word","Year","Page"]
##list4 = []
##list4.extend([list3[2],list3[5],list3[7],list3[10],list3[15],list3[17],list3[19],list3[20]])
##print(list4)
