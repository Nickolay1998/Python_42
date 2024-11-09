##class Cash:
##    def __init__(self, x):
##        self.x = x
##        self.cash = f"{x}"  
##    def __get__(self, instance, owner):
##        if not hasattr(instance, self.cash ):
##            y = self.x(instance)
##            instance.__dict__[self.cash] = y
##        return instance.__dict__[self.cash]
##
##class Cashclass:
##    @Cash 
##    def start(self):
##        return "Hello"  
##m = Cashclass()
##print(m.start) 
##m2 = Cashclass()
##print(m2.start)

##class Integer:
##    def __init__(self, name):
##        self.name = name
##
##    def __set__(self, instance, value):
##        if not isinstance(value, int):
##            raise TypeError("Must be type int")
##        instance.__dict__[self.name] = value
##
##class Intd:
##    x = Integer('x')
##    def __init__(self, x):
##        self.x = x
##        
##i = Intd(10)
##print("Result",i.x)
##try:
##    i.x = "Hello"  
##except TypeError as e:
##    print(e)


##class Readonly:
##    def __init__(self, name):
##        self.name = name
##    def __get__(self, instance, owner):
##        return instance.__dict__.get(self.name)
##    def __set__(self, instance, value):
##        if self.name in instance.__dict__:
##            raise AttributeError(f"Read only this {self.name}")
##        instance.__dict__[self.name] = value
##class AttributeClass:
##    Attribute = Readonly('Attribute')
##    def __init__(self, value):
##        self.Attribute = value
##a = AttributeClass("Hello")
##print("Result:",a.Attribute)  
##try:
##    a.Attribute = "Goodbye"
##except AttributeError as x:
##    print(x)

    

