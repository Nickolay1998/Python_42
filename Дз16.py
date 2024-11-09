##а) Необходимо создать словарь, как минимум 3-я способами;
##d = {'type': 'A', 'class': 'High', 'Price':1000, 'Level': 5, 'Room':25, 'Fee': 'Yes'}
##print(type(d))
##------------------------------------------------
##key_list = ["type","class","Price","Level","Room","Fee"]           # 2 способ
##valuse_list = ['A',"High",1000,5,25,"Yes"]
##dict_l = dict(zip(key_list,valuse_list))
##print(type(dict_l))
##-----------------------------------------------
##dt_tuple = dict((("type","A"),("class","High"),("Price",1000),("Level",5),("Room",25),("Fee","Yes")))  #3 способ
##print(type(dt_tuple))
##-----------------------------------------------------
####b) Добавить в словарь, новую пару Discount: 0.2;
##d["Discount"]=0.2
##print(d)

####c) Заменить значение в паре Price, c 1000 на 1500;
##d["Price"]=1500
##print(d)

####d) Удалить ключ Fee
##del d["Fee"]
##print(d)
##e) Создать список, используя кроме выше указанного словаря, ещё вот такие 
##пары:
dict_lists = [
{"type": "A", "class": "High", "Price": 1500, "Level": 5, "Room": 25,"Discount" : 0.2},
{"type": "A", "class":"Middle","Price": 700," Level": 2," Room": 10,"Discount": 0.1},
{"type": "B", "class": "High", "Price":1200, "Level": 7, "Room":38, "Discount": 0},
{"type": "B","class":"High", "Price":1200, "Level": 8, "Room":39, "Discount": 0.2},
{"type": "C", "class": "Low", "Price":600, "Level": 3, "Room":16, "Discount": 0.3}]

##f) Для созданного списка используя filter () и lambda функцию покажите список в 
##котором Price >800
##pricel = list(filter(lambda i: i["Price"]>800,dict_lists))
##print(pricel)

##h) Для созданного списка используя filter () и lambda функцию покажите список в 
##котором Discount=0

##discount_l = list(filter(lambda i: i["Discount"]==0,dict_lists))
##print(discount_l)

##i) Для созданного списка используя filter () и lambda функцию покажите список в 
##котором class=High.

##High_l=list(filter(lambda i: i["class"]=="High",dict_lists))
##print(High_l)
