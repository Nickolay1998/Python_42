##classmetdhod
##    class Pen:
##    model = "ballpen"
##    producer = "BIC"
##
##    @classmetdhod
##    def change_model(cls, model):
##        cls.model = model       
##        
##    def __init__(self,color,width):
##        self.color = color
##        self.width = width
##        
##    def draw(self): #метод обьекта классу
##        return (f"{self.color} line")
##parker = Pen("blue",2)

##class Pen1:  # Class клас (креслення, рецепт)
##    model = 'ballpen'  # Поле класу
##    producer = 'BIC'  # Поле класу
##
##    @classmethod
##    def change_model(cls, model):
##        cls.model = model
##
##    def __init__(self, color, width):  # метод ініціалізації \ магічний метод \ метод обʼекту класу
##        self.color = color
##        self.width = width
##        self.model = Pen1.model
##        # self.color                   # поле обʼекту класу
##
##    def draw(self):                     # метод обʼекту класу
##        return (f'{self.color} line')
##
##parker = Pen1('blue', 2)
##print(parker.draw())
##print(parker.model)
##Pen1.change_model('Fountain pen')
##abc = Pen1('blue', 2)
##print(abc.draw())
##print(abc.model)

##@classmethod — это декоратор, который используется для создания методов класса в Python.
##Класс-методы принимают в качестве первого аргумента сам класс (cls), а не экземпляр класса (self).
##Это означает, что класс-методы могут взаимодействовать с классом, но не зависят от конкретного экземпляра.
##
##Основные особенности @classmethod:
##В качестве первого аргумента методы, декорированные @classmethod,
##принимают сам класс (cls), а не экземпляр.
##
##Класс-методы могут изменять состояние класса,
##то есть работать с атрибутами и методами класса,
##а не с атрибутами конкретного объекта.
##Они могут быть полезны для создания альтернативных конструкторов или методов,
##которые должны работать на уровне класса.
class Person:
    species = "Homo Sapiens"  # Атрибут класса

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Создаем экземпляр класса, используя альтернативный конструктор
        age = 2024 - birth_year
        return cls(name, age)

    @classmethod
    def get_species(cls):
        return cls.species

# Создание экземпляра с использованием основного конструктора
person1 = Person("Alice", 30)
print(person1.name, person1.age)  # Вывод: Alice 30

# Создание экземпляра с использованием класса-метода (альтернативного конструктора)
person2 = Person.from_birth_year("Bob", 1990)
print(person2.name, person2.age)  # Вывод: Bob 34

# Вызов метода класса, который возвращает атрибут класса
print(Person.get_species())  # Вывод: Homo Sapiens
##Объяснение:
##from_birth_year — это класс-метод, который создает экземпляр класса Person, используя альтернативный конструктор.
##Он вычисляет возраст на основе года рождения и возвращает экземпляр класса, вызывая cls().
##Это полезно, если вам нужно создать экземпляр, используя другой набор данных.
##get_species — класс-метод, который возвращает значение атрибута класса species.
##Он показывает, как можно работать с атрибутами класса напрямую.
##Когда использовать @classmethod:
##Когда требуется альтернативный конструктор для создания экземпляров класса на основе различного набора параметров.
##Когда метод работает только с атрибутами или методами самого класса, а не с конкретным экземпляром.
##Когда нужно модифицировать или использовать атрибуты и методы, которые принадлежат классу, а не объекту.
##Отличие от @staticmethod:
##@staticmethod: метод не принимает ни класс (cls), ни экземпляр (self).
##Он не зависит ни от класса, ни от экземпляра, и используется, когда метод логически принадлежит классу, но не работает с его атрибутами.
##@classmethod: метод работает с классом через параметр cls и может изменять состояние класса, взаимодействуя с его атрибутами и методами.
##Пример с использованием @staticmethod и @classmethod:
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return f"This is a class for {cls.__name__}."

# Вызов статического метода
print(MathOperations.add(5, 3))  # Вывод: 8

# Вызов метода класса
print(MathOperations.description())  # Вывод: This is a class for MathOperations.

##В итоге, @classmethod помогает работать с классом и его атрибутами напрямую, без необходимости создавать экземпляры.



