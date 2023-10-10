import random

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = random.randint(30, 70)
        self.happiness = random.randint(30, 70) 
        self.energy = random.randint(30, 70)
        
    def feed(self):
        self.hunger -= 10    
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
    def play(self):
        self.happiness += 20
        self.energy -= 15    
            
    def status(self):
        print(f"The Animal's name is {self.name}\nIt is a/an {self.species}\nIt is {self.age} years old")
        print(f"Hunger Level: {self.hunger}")
        print("")
        
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def bark(self):
        print(f"The Dog's name is {self.name}\nIt is a/an {self.breed}\nIt says: woof! woof! woof!")    
 
class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Cat", age)
        self.breed = breed

    def purr(self):
        print(f"The Cat's name is {self.name}\nIt is a/an {self.breed}\nIt says: purr... purr... purr")  
        
class Parrot(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, "Parrot", age)
        self.species = species

    def whistle(self):
        print(f"The Parrot's name is {self.name}\nIt belongs to {self.species} species\nIt says: whistles") 
        
class Rabbit(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Rabbit", age)
        self.breed = breed

    def whimp(self):
        print(f"The Rabbit's name is {self.name}\nIt is a/an {self.breed}\nIt whimpers")
        
class Fish(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, "Fish", age)
        self.species = species

    def swim(self):
        print(f"The Fish's name is {self.name}\nIt is a/an {self.species}\nIt swims")    
                               
class Monkey(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Monkey", age)
        self.breed = breed

    def chatter(self):
        print(f"The Monkey's name is {self.name}\nIt is a/an {self.breed}\nIt chatters")
        
if __name__ == "__main__":
    Animals = [Dog("Spookie", 2, "German Shepherd"),
               Cat("Kitty", 1, "Persian"),
               Parrot("Melody", 0.5, "African Grey"),
               Rabbit("Hidden", 0.5, "Holland Lop"),
               Fish("Rocket", 0.2, "Gold Fish"),
               Monkey("Teeny", 1, "Chimpanzee")]
    
    while True:
        print("Welcome to the Virtual Pet Zoo :)")
        print("1. Feed the animals")
        print("2. Play with an animal")
        print("3. View animal status")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            for animal in Animals:
                animal.feed()
        elif choice == "2":
            for animal in Animals:
                animal.play()
        elif choice == "3":
            for animal in Animals:
                animal.status()
        elif choice == "4":
            print("Goodbye :) See you next time :) ")
            break
        else:
            print("Invalid choice! Please try again.")
