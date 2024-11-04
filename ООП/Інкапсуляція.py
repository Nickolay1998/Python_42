#Інкапсуляція
class Mobile:
   __imei = '123'
   _color = 'grey'
   __os = 'Android'
   _model = 'Pixel'

   def change_imei(self, new_imei):
      self.__imei = new_imei

   def show_imei(self):
      return self.__imei

   def change_color(self, new_color):
      self._color = new_color

   def show_color(self):
      return self._color

   def __change_battery(self,new_battery):
       return f"Battery changed{new_battery}"

   def service_center(self,new_battery):
       return self.__change_battery(new_battery)
        

pixel7 = Mobile()

print(pixel7.service_center(123))
##print(pixel7.imei)
##pixel7.imei = 232
##print(pixel7.imei)
##print(pixel7._model)
##print(pixel7.__os)  ###выдаст ошибку потому что приватний рівень
##123
##232
##Інкапсуляція це спосіб скрити або зробити не доступні для зміни поля або методи
## Рівні доступу
##Публічний рівень
##Захищений рівень _поле(бажано не лізти)
##Приватний рывень __поле(неможна змінити)


