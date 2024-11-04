##@property
##Аннотация @property позволяет определить метод, который будет доступен как атрибут класса.
##Это называется "геттером" — методом, который возвращает значение атрибута.
##При этом внешний код может обращаться к этому методу, как к обычному атрибуту, не зная, что это на самом деле метод.
##class Person:
##    def __init__(self, name):
##        self._name = name
##
##    @property
##    def name(self):
##        return self._name
##
##p = Person("Alice")
##print(p.name)  # Вывод: Alice
##Здесь name ведет себя как обычное свойство объекта
##хотя на самом деле это метод, определённый с @property

##@getter и @setter
##Геттер (getter) позволяет контролировать, как считывается значение атрибута. Он определяется через @property.
##Сеттер (setter) позволяет задать метод, который контролирует изменение значения атрибута.
##Он используется, чтобы избежать некорректных данных или добавить дополнительную логику при изменении атрибута.
##Сеттер определяется с использованием @имя_свойства.setter.
##Пример использования @setter:

##class Person:
##    def __init__(self, name):
##        self._name = name
##
##    @property
##    def name(self):
##        return self._name
##
##    @name.setter
##    def name(self, value):
##        if not isinstance(value, str):
##            raise ValueError("Name must be a string!")
##        self._name = value
##
##p = Person("Alice")
##print(p.name)  # Вывод: Alice
##
##p.name = "Bob"  # Устанавливаем новое имя
##print(p.name)   # Вывод: Bob
##
## p.name = 123  # Ошибка: Name must be a string!
##Здесь мы используем декоратор @property для получения значения атрибута _name
##и @name.setter для проверки данных и установки нового значения.

##Как это работает:
##@property используется для создания "геттера", чтобы обращаться к методу как к атрибуту.
##@setter используется для создания "сеттера", который позволяет определить, как менять значение атрибута.
##@deleter (который мы не рассмотрели, но тоже важен) используется для создания метода, который удаляет атрибут.
##class Person:
##    def __init__(self, name):
##        self._name = name
##
##    @property
##    def name(self):
##        """Геттер для имени"""
##        return self._name
##
##    @name.setter
##    def name(self, value):
##        """Сеттер для имени"""
##        if not isinstance(value, str):
##            raise ValueError("Name must be a string!")
##        self._name = value
##
##    @name.deleter
##    def name(self):
##        """Удаление имени"""
##        print("Deleting name...")
##        del self._name
##p = Person("Alice")
##print(p.name)  # Вывод: Alice
##
##p.name = "Bob"
##print(p.name)  # Вывод: Bob

##del p.name  # Вывод: Deleting name...
##print(p.name)  # Ошибка: AttributeError: 'Person' object has no attribute '_name'

##Итог:
##@property позволяет обращаться к методам, как к атрибутам.
##@setter добавляет проверку или логику при изменении атрибутов.
##@deleter добавляет логику при удалении атрибута.
##Эти механизмы помогают инкапсулировать данные и управлять доступом к ним, что важно для создания более безопасного и гибкого кода.

##isinstance — это встроенная функция в Python, которая проверяет, является ли объект экземпляром указанного класса (или его подкласса).
##Она используется для проверки типа данных объекта.
##isinstance(object, classinfo)
##object — объект, тип которого нужно проверить.
##classinfo — класс или кортеж классов, с которыми нужно сравнить.
##Возвращаемое значение:
##True, если объект является экземпляром указанного класса или его подкласса.
##False, если объект не является экземпляром указанного класса или его подкласса.
# Проверка на принадлежность к типу int
##print(isinstance(5, int))  # Вывод: True
##
### Проверка на принадлежность к типу str
##print(isinstance("hello", str))  # Вывод: True
##
### Проверка на принадлежность к нескольким типам
##print(isinstance(5.5, (int, float)))  # Вывод: True
##
### Проверка на принадлежность к классу и его наследникам
##class Animal:
##    pass
##
##class Dog(Animal):
##    pass
##
##buddy = Dog()
##
##print(isinstance(buddy, Dog))    # Вывод: True
##print(isinstance(buddy, Animal)) # Вывод: True, так как Dog — подкласс Animal
##print(isinstance(buddy, int))    # Вывод: False
##print(isinstance("Hello",int))

##Когда использовать isinstance:
##Для проверки, принадлежит ли объект к определенному типу или классу.
##При необходимости проверить, поддерживает ли объект определенный интерфейс (в случае наследования).
##Чтобы избежать ошибок, связанных с неправильным типом данных.

##def add_numbers(a, b):
##    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
##        raise ValueError("Both arguments must be int or float")
##    return a + b
##
##print(add_numbers(5, 3))      # Вывод: 8
##print(add_numbers(5, "hello"))  # Ошибка: ValueError
##hasattr — это встроенная функция в Python, которая проверяет, существует ли у объекта определённый атрибут (метод или свойство).
##Она возвращает True, если атрибут присутствует, и False, если атрибут отсутствует.
##object — объект, у которого нужно проверить наличие атрибута.
##"attribute_name" — имя атрибута, который нужно проверить, передается как строка.
##Возвращаемое значение:
##True, если объект имеет указанный атрибут.
##False, если объект не имеет указанного атрибута.
##class Car:
##    def __init__(self, brand, model):
##        self.brand = brand
##        self.model = model
##
##    def start_engine(self):
##        print(f"The {self.brand} engine is now running.")
##
### Создаем экземпляр класса
##my_car = Car("Toyota", "Corolla")
##
### Проверяем наличие атрибутов
##print(hasattr(my_car, "brand"))        # Вывод: True
##print(hasattr(my_car, "year"))         # Вывод: False
##print(hasattr(my_car, "start_engine")) # Вывод: True (метод также является атрибутом)
##
### Проверяем наличие метода перед выполнением
##if hasattr(my_car, "start_engine"):
##    my_car.start_engine()
##else:
##    print("Engine cannot be started.")

##class Animal:
##    pass
##
##dog = Animal()
##
### Динамически добавляем атрибут к объекту
##dog.name = "Buddy"
##
### Проверяем наличие атрибута
##print(hasattr(dog, "name"))  # Вывод: True
##print(hasattr(dog, "age"))   # Вывод: False

##Почему hasattr полезен?
##Безопасность: Избегает попыток обращения к несуществующим атрибутам, которые могут вызвать ошибку AttributeError.
##Гибкость: Позволяет проверять наличие атрибутов в динамических и сложных объектах (особенно полезно при работе с объектами или модулями, которые могут быть изменены во время выполнения программы).
##Универсальность: Работает для проверки как методов, так и свойств объекта.
##Итог:
##Функция hasattr позволяет безопасно проверить, существует ли определённый атрибут или метод у объекта.
##Она помогает избежать ошибок, связанных с попыткой доступа к несуществующим атрибутам и делает код более гибким и надежным.

class QTV:
    def __init__(self,x):
        self.x = x
    @property
    def ggg(self):
        return self.x

    
    def ggg1(self,value):
        if not isinstance(value, str):
            raise ValueError("Error")
        self.x = value

q = QTV(5)
print(q.ggg(5))

##q.ggg = 5
####print(q.ggg)     ValueError: Error

