#  Differences of Inheritance and PolyMorphism

# Inheritance
def main():
    class Vehicle():
        def __init__(self, owner, model, category, year):
            self.owner = owner
            self.model = model
            self.category = category
            self.year = year
        
        def startUp(self):
            print(f"The {self.category} is warming up...")
    
    class Boat(Vehicle): # Inheriting the __init__ of the Vehicle class
        def drive(self):
            print(f"{self.owner} is driving your {self.model}.")
    
    class Plane(Vehicle):
        def drive(self):
            print(f"{self.owner} is piloting the aircraft.")
    
    class Car(Vehicle):
        def drive(self):
            print(f"{self.owner} is driving his/her {self.model}")
        
    boat1 = Boat("Derek", "Sunseeker Predator 50", "boat", "2022")
    plane1 = Plane("Cecelia", "Cirrus SR22", "plane", "2022")
    car1 = Car("Andre", "Toyota Camry", "car", "2022")
    
    # boat1.startUp() # Testing if boat1 works
    # plane1.startUp() # Testing if plane1 works
    # car1.startUp() # Testig if car1 works

    # Uncomment Lines 37-47 when you want to demo this portion of Inheritance

    # search = str(input(f"What type of vehicle are you looking for?"))

    # if (search.lower() not in {boat1.category, plane1.category, car1.category}):
    #     print("There is no vehicle of that type...")
    # else:
    #     if (search.lower() == boat1.category):
    #         print(f"We have a {boat1.model} registered under {boat1.owner}.")
    #     elif (search.lower() == plane1.category):
    #         print(f"We have a {plane1.model} registered under {plane1.owner}.")
    #     elif (search.lower() == car1.category):
    #         print(f"We have a {car1.model} registered under {car1.owner}.")
    
    # __________________________________________________________________________________________________________________
    
    #Polymorphism
            
    class Animal():
        def eat(self):
            print("*Nibble Nibble*")
    
    class Cat(Animal):
        pass
    
    class Dog(Animal):
        def eat(self): # Overriding eat() from inherited 'Animal' class
            print("*Nom Nom*")
    
    class Horse(Animal):
        def eat(self): # Overriding eat() from inherited 'Animal' class
            print("*Munch Munch*")
    
    class Mouse(Animal):
        pass

    cat = Cat()
    dog = Dog() # Polymorphed
    horse = Horse() # Polymorphed
    mouse = Mouse()

    # cat.eat()
    # dog.eat()
    # horse.eat()
    # mouse.eat()

#------------------------------------------------------------------

    class Weapon:
        def __init__(self, name, damage, durability, attack_speed):
            self.name = name
            self.damage = damage
            self.durability = durability
            self.attack_speed = attack_speed

        def attack(self):
            print(f"The {self.name} attacks, dealing {self.damage} damage.")

    class Sword(Weapon):
        def attack(self):
            print(f"Swing your sword, dealing {self.damage} damage per strike.")

    class Bow(Weapon):
        def attack(self):
            print(f"Shoot arrows from your bow, dealing {self.damage} damage per arrow.")

    class Dagger(Weapon):
        def attack(self):
            print(f"Stab with your dagger, dealing {self.damage} damage per stab.")

    # Example of using polymorphism with method overriding
    weapons = [
        Sword("Excalibur", 30, 100, 1.5),
        Bow("Longbow", 20, 80, 2.0),
        Dagger("Assassin's Dagger", 15, 50, 1.8)
    ]

    for weapon in weapons:
        weapon.attack()

if __name__ == "__main__":
    main()