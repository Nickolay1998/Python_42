##class First:
##    data = "123" # атрибут класу,аргумент класса,поле класса,смена класса
##    def create(self):
##        return First.data   # метод класса,функция класса
##variable_name = "snake_style"
##variableName = "camelCase"
##
##one = First()
##print(one.data)
##print(one.create())


##class Borsch:
##    ingridients = ["beet","cabbage","bean","potate"]
##    spices = ["red_pepper", "chile_pepper","garlic"]
##    meat = ["pork","beef","chicken"]
##    value = 3
##    date_to_expire = "2024-10-1"
##    temperature = 3
##        
##    def boiled(self,temperature):
##        self.temperature = temperature
##        return f'boiled for {temperature} degree'
##
##    def eat(self):
##        return f'eat borsch'
##
##    def cut(self):
##        return f"cut_ ingridients"
##
##    def sp(self):
##        return f"add_spices"
##
##    def add_meat(self):
##        return f"add_meat"
##
##    def change_meat(self):
##       return self.meat[2] ="s"

##my_borsch = Borsch()

##print(my_borsch.boiled(my_borsch.temperature))
##print(my_borsch.ingridients[1],my_borsch.cut())
##print(my_borsch.ingridients[2],my_borsch.cut())
##print(my_borsch.ingridients[3],my_borsch.cut())
##print(my_borsch. meat[2],my_borsch.add_meat())
##print(my_borsch. spices[0],my_borsch.sp())
##my_borsch.ingridients.append("onion")
##my_borsch.ingridients.append("carrot")
##my_borsch.ingridients.append("smoked_pear")
##
##your_borsch = Borsch()
##your_borsch.ingridients.append("s")
##
##print(my_borsch.ingridients.meat)
##my_borsch.ingridients.meat("s")        
##print(my_borsch.ingridients)

##class Car:
##   whilestype = ["летние","зимние"]
##   oil = ["АИ-98","А-76"]
##   country = ["Япония","США","Германия"]
##
##   def what_country(self):
##       return f'country:'
##   def what_oil(self):
##       return f'oil:'
##
##   def what_while(self):
##       return f'while:'
##s = Car()
##print(s.what_country(),s.country[1])
##print(s.what_oil(),s.oil[1])
##print(s.what_while(),s.whilestype[1])
##        
                                                               ##Инкапсуляция

#public - публічний рівень name
# protected - захищенний рівень _cover
#private - приватний рівень(напряму недоступний)

class Mobile:
   imei = '123'
   __password = "qw12"
   _color = 'grey'
   os = 'Android'
   model = 'Pixel'
   name = 'default'
   _cover ="Silver"
   sim = "Vodafone"
   __number ="0952344523"

   def change_imei(self, new_imei):
      self.imei = new_imei

   def show_imei(self):
      return self.imei

   def change_color(self, new_color):
      self.color = new_color

   def show_color(self):
      return self.__color

   def change_name(self, new_name):
      self.name = new_name

   def show_name(self):
      return self.name

##pixel7 = Mobile()
##print(pixel7.show_color())
##print(pixel7.show_imei())
##print(pixel7.show_name())
##pixel7.color = 'green'
##pixel7.imei = '456'
##pixel7.name = 'qwerty'
##print(pixel7.show_color())
##print(pixel7.show_imei())
##print(pixel7.show_name())
##pixel7._cover = "black"
##print(pixel7._cover)   

##class Mobille:
##   __sim = "Vodafone"
##   _number ="0952344523"
##   
##   def change_number(self,new_number):
##      self._number = new_number
##   def show_number(self):
##      return self._number
##
##   def change_sim(self,new_sim):
##      self.__sim = new_sim
##   def show_sim(self):
##      return self.__sim   
##
##
##samsung = Mobille()
##samsung._number = "999999"
##samsung.__sim = "Lifesell"
##print(samsung.show_number())
##print(samsung.show_sim())

# Написати 2 методи з методами доступу до них ( один приватний і один захищений)#
##Написати 2 поля з методами доступу до них ( один приватний і один захищений)

                                                   #Наслідування(Успадкування)
class Human:
   name = "John"
   surname = "Doe"
   age = 30
   def eat(self):
      return "I am eating"
   def speak(self):
      return "I am speaking"


##class SeaBuilder(Builder,Sailor)
##seal = SeaBuilder()
##print(seal.name)
##seal.builder()


##john = Human()
##print(john.name)
##print(john.eat())
##bender = Builder()
##print(bender.builder())
##papay = Sailor()
##print(papay.speak())
##print(papay.name)
##print(papay.smoking())


class Builder(Human):
   name = "Default"
   def speak(self):
      return "I am a builder"
   def builder(self):
      return "I am a builder"
class Sailor(Human):
   name = "Jack"
   def speak(self):
      return "I am a sailor"

   def smoking(self):
      return "Bad idea"
class Trucker(Human):
   def drive(self):
      return "I am driving"
   def buyOil(self):
      return "I buy oil"

class firstTrucker(Builder,Trucker):
    pass

class secondTrucker(Sailor,Trucker):
    pass

first=firstTrucker()
second=secondTrucker()

print(first.drive())
print(second.buyOil())
print(second.smoking())
print(first.name)
##                                   Полиморфизм 


