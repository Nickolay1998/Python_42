                                                    ##Особливості ООП
####Качина типізація приклад
####class Duck:
####    def eat(self):
####        return "Duck"
####class Dog:
####    def eat(self):
####        return "Dog"
####class Frog:
####    def eat(self):
####        return "Frog"
####
####def food_injector(animal):
####    print(animal.eat())
####
####donald = Duck()
####guffie = Dog()
####pepe = Frog()
####
####food_injector(donald)
####food_injector(guffie)
####food_injector(pepe)
####Перевантаження методів приклад
####class Animal:
####    def eat(self):
####        return "Duck eat"
####
####class Dog(Animal):
####    def eat(self):
####        return "Dog eat"
####
####class Frog(Animal):
####    def eat(self):
####        return "Frog eat"
####
####def food_injector(animal):
####    print(animal.eat())
####
####donald = Duck()
####guffie = Dog()
####pepe = Frog()
####
####food_injector(donald)
####food_injector(guffie)
####food_injector(pepe)

 
#Приклад MRO
##class Animal:
##    def eat(self):
##        return 'Animal eat'    
##    def show_a(self):
##        return 'a'
##
##class Bear(Animal):
##    def eat(self):
##        return 'Bear eat'
##    def show_b(self):
##        return 'b'
##
##class Cat(Animal):
##    def eat(self):
##        return 'Cat eat'
##    def show_c(self):
##        return 'c'
##
##class Duck(Bear, Cat):
##    def eat(self):
##        return 'Duck eat'
##    def show_d(self):
##        return 'd'
##    
##class Elephant(Bear):
##    def eat(self):
##        return 'Elephant eat'
##    def show_e(self):
##        return 'e'
##
##class Fox(Cat):
##    def eat(self):
##        return 'Fox eat'
##    def show_f(self):
##        return 'f'
##    
##class Owl(Duck, Elephant, Fox):
##    def eat(self):
##        return 'Owl eat'
##    def show_o(self):
##        return 'o'
    
