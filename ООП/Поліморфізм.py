###Поліморфізм
##class Grinder:
##    def start(self,products):
##        self.products = products
##        if  self.products == "meat":
##            return "mince"
##        elif  self.products == "branch":
##            return "sawdust"
##        else:
##            return f"grinded {self.products}"
##g = Grinder()
##print(g.start("coffee"))


class Grinder:
    __id = 0
    name = 'default'
    def start(self, products): #поліморфний метод
        self.products = products
        if self.products == 'meat':
            return 'mince'
        elif self.products == 'branch':
            return 'sawdust'
        else:
            return f'grinded {self.products}'
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if Grinder.name == 'default':
            self.__id = id
        else:
            self.__id = 1
    
    @id.deleter
    def id(self):
        return self.__id
            

##some_grinder = Grinder()
##print(some_grinder.start('coffee'))
##print(some_grinder.start('meat'))
##print(some_grinder.start('branch'))
##print(some_grinder.id)
##some_grinder.id=3
##print(some_grinder.id)

##class Mobile:
##   __imei = '123'
##   __password = "qw12"
##   color = 'grey'
##   os = 'Android'
##   model = 'Pixel'
##   name = 'default'
##   _cover ="Silver"
##   sim = "Vodafone"
##   __number ="0952344523"
##   @property 
##   def imei(self):
##       return self.__imei
##       
##   @imei.setter
##   def imei(self, imei):
##       if Mobile.name == 'default':
##           self.__imei = imei
##       else:
##           self.__imei = 1
##    
##   @imei.deleter
##   def imei(self):
##       return self.__imei
##
##g = Mobile()
##print(g.__imei())

##class Table:
##    count = 0    
##    def __init__(self,name): #Магічний метод dunder method
##        Table.count += 1
##        self.name = name # поле обьекта класу
##
##    def change_name(self,name):
##        self.name = name
##
##    def __str__(self):
##        return self.name
##
##wood = Table("redwood")
##print(wood.name)
##print(wood.count)
###### redwood
##stone = Table("redstone")
##print(stone.name)
##print(stone.count)     
##print(wood)
##print(stone)

##class OrwellMath:
##    def __init__(self, number):
##        self.number = number
##
##    def __str__(self):
##        return self.number
##
##    def __add__(self, other):
##        return self.number + other.number + 1
##
##    def __eq__(self, other):
##        if self.number == other.number:
##            return "Hello"
##        else:
##            return "Not"

##print(int(2) + int(2))
##print(OrwellMath(2) + OrwellMath(2))
##
##print(int(2) == int(2))
##print(OrwellMath(2) == OrwellMath(3))

class Number:
    num = int(input())
    
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        return self.num+other.num

    def __sub__(self,other):
        return self.num-other.num

    def __mul__(self,other):
        return self.num*other.num

    def __truediv__(self,other):
        return self.num/other.num
print(Number.num+int(2))
print(Number(3)+Number(2))
print(Number(3)-Number(2))
print(Number(3)*Number(2))
print(Number(3)/Number(2))

##class Number:
##    value = int(input())
##    
##    
##    def __init__(self,value):
##        self.value=value
##        
##    def __add__(self,other):
##        return self.value+other.value
##    
##    def __add__(self,other):
##        return self.value-other.value
##    
##    def __add__(self,other):
##        return self.value*other.value
##    
##    def __add__(self,other):
##        return self.value/other.value
##    
##
##print(Number.value+int(2))
##print(Number(2)+Number(3))

class NumberM:
    value = 10
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __add__(self, other):
        if hasattr(other, 'value'):
            return self.value + other.value
        else:
            return self.value + other

    def __sub__(self, other):
        if hasattr(other, 'value'):
            return self.value - other.value
        else:
            return self.value - other

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value


print(NumberM(3) + NumberM(2))
print(NumberM(3) + int(4))
print(NumberM(3) - float(4.5))

