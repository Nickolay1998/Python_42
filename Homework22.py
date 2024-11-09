##class Сircle:    
##    def __init__(self, radius,p=3.14):
##        self.radius = radius
##        self.p = p           
##    def __str__(self):
##        return f"{round(2*self.radius*self.p,2)}"
##    
##    def __iadd__(self, num):
##        self.radius += num
##        return self
##    
##    def __isub__(self, num):
##        self.radius -= num
##        return self
##    
##    def __eq__(self,other):
##        return self.radius == other.radius
##
##    def __lt__(self, other):
##        return self.radius*2*self.p < other.radius*2*self.p
##    
##    def __le__(self, other):
##        return self.radius*2*self.p <= other.radius*2*self.p
##    
##    def __gt__(self, other):
##        return self.radius*2*self.p > other.radius*2*self.p
##    
##    def __ge__(self, other):
##        return self.radius*2*self.p >= other.radius*2*self.p
##
##print(Сircle(5)==Сircle(5))
##print(Сircle(5)>Сircle(3))
##print(Сircle(5)<Сircle(3))
##print(Сircle(5)>=Сircle(3))
##print(Сircle(5)<=Сircle(3))
##circle = Сircle(10+5)
##circle1 = Сircle(10-3)
##circle2 = Сircle(10)
##circle3 = Сircle(10)
##print(circle)
##print(circle1)
##circle2 += 2
##circle3 -= 4
##print(circle2)
##print(circle3)

##class Complex:
##    def __init__(self, x,y):
##        self.x = x
##        self.y = y
##
##    def __add__(self,other):
##        return complex(self.x,self.y)+complex(other.x,other.y)
##
##    def __sub__(self,other):
##        return complex(self.x,self.y)-complex(other.x,other.y)
##
##    def __mul__(self,other):
##        return complex(self.x,self.y)*complex(other.x,other.y)
##
##    def __mul__(self,other):
##        return complex(self.x,self.y)*complex(other.x,other.y)
##
##    def __truediv__(self, other):
##        return complex(self.x,self.y)/complex(other.x,other.y)
##        
##
##print(Complex(3,3)+Complex(3,3))
##print(Complex(3,3)-Complex(2,2))
##print(Complex(3,3)*Complex(2,2))
##print(Complex(3,3)/Complex(2,2))

##class Airplane:
##    def __init__(self,x):
##        self.x = x
##        
##    def __str__(self):
##        if self.x>0:
##            return f"{self.x}"
##        else:
##            return f"error"
##
##    def __eq__(self,other):
##        return self.x == other.x
##
##    def __iadd__(self, x):
##        self.x += x
##        return self
##    
##    def __isub__(self, x):
##        self.x -= x
##        return self
##
##    def __lt__(self, other):
##        return self.x < other.x
##    
##    def __le__(self, other):
##        return self.x <= other.x
##    
##    def __gt__(self, other):
##        return self.x > other.x
##    
##    def __ge__(self, other):
##        return self.x >= other.x
##
##a = int(input("Кількість "))
##print(Airplane("passenger")==Airplane("military"))
##print("збільшення пасажирів на",a,Airplane(500+a))
##print("зменшення пасажирів на",a,Airplane(500-a))
##a2 = Airplane(500)  
##a3 = Airplane(1000) 
##a2 += a
##a3 -= a
##print("збільшення пасажирів +",a,a2)
##print("зменшення пасажирів -",a,a3)
##print(Airplane(1500)>Airplane(1000))
##print(Airplane(1500)<Airplane(1000))
##print(Airplane(1500)>=Airplane(1000))
##print(Airplane(1500)<=Airplane(1000))

##class Flat:
##    def __init__(self,s):
##        self.s = s  
##
##    def __str__(self):
##        if self.s>0:
##            return f"{self.s}"
##        else:
##            return f"error"
##
##    def __eq__(self,other):
##        return self.s == other.s
##
##    def __lt__(self, other):
##        return self.s < other.s
##    
##    def __le__(self, other):
##        return self.s <= other.s
##    
##    def __gt__(self, other):
##        return self.s > other.s
##    
##    def __ge__(self, other):
##        return self.s >= other.s
##
##    def __gt__(self,other):
##        return self.s != other.s
##        
##print(Flat(50)==Flat(40))
##print(Flat(40)<Flat(80))
##print(Flat(34)>Flat(82))
##print(Flat(77)>=Flat(23))
##print(Flat(23)<=Flat(67))   



