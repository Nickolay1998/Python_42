##class Device:
##    Model = input()
##    Firm = input()
##    Price = int(input())
##
##    def show_model(self,Model):
##        self.Model = Model
##        return f"This model is {Model}"
##
##    def show_firm(self,Firm):
##        self.Firm = Firm
##        return f"This firm is {Firm}"
##
##    def show_price(self,Price):
##        self.Price = Price
##        return f"This price is {Price}"
##
##    def show_function(self):
##        return "The function is "
##
##    def show_type(self):
##        return "The type is"   
##class CoffeeMachine(Device):
##    def funct1(self):
##        return "setting the grind size of coffee beans"
##    def funct2(self):
##        return "frothing milk"
##    def funct3(self):
##        return "setting the shutdown timer"
##    def type1(self):
##        return "Automatic"
##    def type2(self):
##        return "Capsule"
##    def type3(self):
##        return "On instant coffee"
##        
##c =  CoffeeMachine()
##print(c.show_model(c.Model))
##print(c.show_firm(c.Firm))
##print(c.show_price(c.Price))
##print(c.show_function(),c.funct1())
##print(c.show_function(),c.funct2())
##print(c.show_function(),c.funct3())
##print(c.show_type(),c.type1())
##print(c.show_type(),c.type2())
##print(c.show_type(),c.type3())
##
##
##class Blender(Device):
##    def funct1(self):
##        return "Grinding food"
##    def funct2(self):
##        return "preparation of emulsions"
##    def funct3(self):
##        return "whisking drinks"
##    def type1(self):
##        return "Stationary"
##    def type2(self):
##        return "High speed submersible"
##    def type3(self):
##        return "High power submersible"
##
##b = Blender()
##print(b.show_model(b.Model))
##print(b.show_firm(b.Firm))
##print(b.show_price(b.Price))
##print(b.show_function(),b.funct1())
##print(b.show_function(),b.funct2())
##print(b.show_function(),b.funct3())
##print(b.show_type(),b.type1())
##print(b.show_type(),b.type2())
##print(b.show_type(),b.type3())
##    
##class MeatGrinder(Device):
##    def funct1(self):
##        return "grinding other types of products"
##    def funct2(self):
##        return "device for making minced meat"
##    def type1(self):
##        return "Mechanical"
##    def type2(self):
##        return "Household"
##    def type3(self):
##        return "Industrial"
##
##m = MeatGrinder()
##print(m.show_model(m.Model))
##print(m.show_firm(m.Firm))
##print(m.show_price(m.Price))
##print(m.show_function(),m.funct1())
##print(m.show_function(),m.funct2())
##print(m.show_type(),m.type1())
##print(m.show_type(),m.type2())
##print(m.show_type(),m.type3())

##class Ship:
##    weapons = ["ROCKET","BOMB","TORPEDO","Air Defense","artillery"]
##    device = ["Electronic warfare","RADAR"]
##    name = "?"
##    speed = "?"
##    leght = "?"
##    pro = "?"        
##    def Name(self,name):
##        self.name = name
##        return f"The name ship is {name}"
##
##    def Speed(self,speed):
##        self.speed = speed
##        return f"The speed is {speed}"
##
##    def Leght(self,leght):
##        self.leght = leght
##        return f"The leght is {leght}"
##
##
##class Frigate(Ship):
##    def destroy(self,weapons):
##        return f"destroy submarine use weapon is {weapons}"
##
##    def search(self,device):
##        return f"search submarine use device is {device}"  
##f =  Frigate()
##print(f.Name("BLACK"),f.destroy(f.weapons[0]))
##print(f.Name("BLACK"),f.search("RADAR"))
##
##class Destroyer(Ship):
##    def Accompaniment(self,speed,leght):
##        return f"Your ship has {speed} speed and leght is {leght} you can accompaniment ships "
##    def Protect(self,weapons,device):
##        return f"Protect your ship identify eneme rocket use {device} and destroy it use {weapons} "
##
##d = Destroyer()
##print(d.Name("Flying Holland"),d.Accompaniment(50,300))
##print(d.Name("Flying Holland"),d.Protect(d.weapons[3],d.device[0]))
##
##class Cruiser(Ship):
##    def support(self,weapons):
##        return f"Support your {weapons}"
##    def attak(self,device,weapons):
##        return f"Identify the enemy use {device} and destroy it use {weapons}"
##c = Cruiser()
##print(c.Name("Raver"),c.support(c.weapons[0]),"and",c.support(c.weapons[4]),sep=",")
##print(c.Name("Raver"),c.attak(c.device[1],c.weapons[2]))
    
##class Money:
##    count_money = 5
##    kopeck = 0.34
##
##    def __add__(self,kopeck,count_money):
##        return  self.currency + self.kopeck
##
##class Product(Money):
##    name_product = "what is product?"
##    reduction_price = float(input("num for reduction  "))
##    def show_price(self):
##        return f"{self.count_money + self.kopeck}"
##
##    def __sub__(self,count_money,kopeck,reduction_price):
##        (self.count_money + self.kopeck)-self.reduction_price
##
##    def price_reduction(self):
##        (self.count_money + self.kopeck)-self.reduction_price
##
##    def show_reduction(self,name_product):
##        if (self.count_money + self.kopeck)-self.reduction_price>0:
##            return f"{name_product}{(self.count_money + self.kopeck)-self.reduction_price}"
##        else:
##            return "Error"
##        
##p = Product()
##print(p.show_reduction("milk "))

    
    
    
    
        
    
    
    


