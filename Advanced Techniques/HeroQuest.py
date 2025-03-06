
import random

class Hero:           #camelcase is conventional for class names

    #i believe this is an object

    def __init__(self, givenName): #init for initialise, not sure yet what this means, it's called a constructor
        self.health = 100 #self defines this value as unique to the specific instance of the hero class created
        self.name = givenName


    #these look like procedures and functions, but they are called methods as they are the behaviors of a class

    def inspect(self):
        print(self.name, "is a mighty hero")
        print("they have", self.health, "health remaining")

    def takedamage(self, amount):
        self.health -= amount

    def attack(self, target):
        damage = random.randint(1,20)

        target.takedamage(damage)

        print(self.name,"has attacked",target.name,"for",damage,"damage")
        print(target.name, "now has", target.health, "health remaining")



class Mage(Hero): #mage is a subclass of hero and has inherited their methods and attributes
    #overiding
    # def __init__(self, givenName):
    #     self.health = 50
    #     self.name = givenName
    #     self.intelligence = 100
    
    def __init__(self, givenName):
        super().__init__(givenName) #reads the parent (or super) classes attributes
        self.health = 50
        self.intelligence = 100

    def fireball(self):
        print("fireball")
    
    def inspect(self):
        print(self.name, "is an intelligent hero")
#a better aproach would be to have the classes in seperate files, to be imported


myHero = Hero("Stephan")
sidekick = Mage("Turkmenistan")


# print(myHero.name)
# print(sidekick.name)

# myHero.inspect()
# sidekick.inspect()

# myHero.takedamage(20)

# myHero.inspect()

myHero.attack(sidekick)