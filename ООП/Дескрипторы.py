##class Integer:
##    def __init__(self, name):
##        self.name = name
##
##    def __set__(self, instance, value):
##        if not isinstance(value, int):
##            raise ValueError("Значение должно быть целым числом")
##        instance.__dict__[self.name] = value
##
##    def __get__(self, instance, owner):
##        return instance.__dict__.get(self.name)
##
##    def __delete__(self, instance):
##        raise AttributeError("Нельзя удалить атрибут")
##
##class Point:
##    x = Integer('x')
##    y = Integer('y')
##
##    def __init__(self, x, y):
##        self.x = x
##        self.y = y
##
##p = Point(10, 20)
##print(p.x)  # Вывод: 10
####p.x = 30    # Работает нормально
####p.x = 'a'   # Выдаст ошибку: ValueError: Значение должно быть целым числом
##
##



class CachedResult:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        # Получаем значение атрибута из словаря instance.__dict__
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # Устанавливаем значение в словарь instance.__dict__
        instance.__dict__[self.name] = value


class MyClass:
    x = CachedResult('x')

    def __init__(self, x):
        self.x = x  # Устанавливаем значение через дескриптор


# Создаем экземпляры и проверяем
m = MyClass(10)
print(m.x)  # Ожидаемый вывод: 10

m2 = MyClass(15)
print(m2.x)  # Ожидаемый вывод: 15

# Проверка дескриптора на уровне класса
print(MyClass.x)  # Дескриптор, а не значение, потому что мы обращаемся через класс

