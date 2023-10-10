class Animal:
    def __init__(self, age, name):
        self.name = name
        self.age = age
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        
    def play(self):
        self.hunger += 10
        self.energy -= 20
        self.happiness += 30
        
    def feed(self):
        self.hunger -= 30
        self.energy += 10
        
    def sleep(self):
        self.energy += 40
        
    def get_status(self):
        return f"Name: {self.name},\n Age: {self.age}\n Hunger level: {self.hunger}\n Energy level: {self.energy}\n Happiness level: {self.happiness}"
    
class VPZ:
    def __init__(self):
        self.available_pet = [
            Animal(1,"dog"),
            Animal(0.5, "cat"),
            Animal(2, "monkey"),
            Animal(3, "fish"),
            Animal(1.5, "parrot"),
        ]    
        self.adopted_pet = None
           
    def display_available_pet(self):
        print("Available Pets:")
        for index, pet in enumerate(self.available_pet):
            print(f"{index + 1}. {pet.name}")           
            
    def check_pet_status(self):
        if self.adopted_pet:
            print("Pet status:")
            print(self.adopted_pet.get_status())
        else:
            print("No pet adopted.")
            
    def adopt_pet(self, index):
        if 1 <= index <= len(self.available_pet):
            self.adopted_pet = self.available_pet.pop(index -1)
            print(f"You have adopted {self.adopted_pet.name}")
        else:
            print("Invalid choice!")
            
    def start(self):
        print("welcome to Virtual Pet Zoo.")
        while True:
            print("\nOptions:")
            print("1. View available pets.")
            print("2. Check pet status")
            print("3. Adopt a pet")
            print("4. Play with pet")
            print("5. Feed pet")
            print("6. Make the pet sleep")
            print("7. Exit!")
            
            choice = input("Enter your choice:")
            
            if choice == "1":
                self.display_available_pet()
            elif choice == "2":
                self.check_pet_status()
            elif choice == "3":
                if self.adopted_pet:
                    print("You can only adopt one pet at a time") 
                else:
                    self.display_available_pet()
                    pet_choice = int(input("Enter the number of pet you want to adopt:"))
                    self.adopt_pet(pet_choice)
            elif choice == "4":
                if self.adopted_pet:
                    self.adopted_pet.play()
                    print("You played with the pet\n Happiness level increased\n Energy level increased\n Hunger level increased")
                else:
                    print("No pet to play with.")
            elif choice == "5":
                if self.adopted_pet:
                    self.adopted_pet.feed()
                    print("You fed your pet.\n Energy level increased.\n Hunger level decreased")
                else:
                    print("You dont have a pet to feed.")
            elif choice == "6":
                if self.adopted_pet:
                    self.adopted_pet.sleep()
                    print("Your pet slept.\n Energy level increased.")
                else:
                    print("You dont have a et to make it sleep.")
            elif choice == "7":
                print("Hope you enjoyed\n Bye! See you next time :)")
                break
            else:
                print("Invalid choice! Please try again.")
                
zoo = VPZ()
zoo.start()                                        
                    
                    
                                
            
                           
                                                                