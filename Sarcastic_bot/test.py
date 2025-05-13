import random
class Pet:
    def __init__(self,n,s,a):
        self.name= n
        self.species= s
        self.age= a
    def display_info(self):
        return f"Name:{self.name}, Species:{self.species}, Age:{self.age}"

class Dog(Pet):
    def __init__(self,n,s,a,b,c):
        self.name = n
        self.species = s
        self.age = a
        self.breed= b
        self.color= c
    def display_info(self):
        return f"Name:{self.name}, Species:{self.species}, Age:{self.age}, Breed:{self.breed}, Color:{self.color}"


class Cat(Pet):
    def __init__(self, n,s,a,b,c):
        self.name = n
        self.species = s
        self.age = a
        self.breed = b
        self.color = c

    def display_info(self):
        return f"{Cat.display_info()}, Breed:{self.breed}, Color:{self.color}"
class PetAdoptionSystem:
    def __init__(self):
        self.pet_dict={}



    def add_pets(self,pet):
        pet_id= random.randint(100,999)
        self.pet_dict[pet_id] = pet
        print(f"Pet added with ID: {pet_id}")




    def view_pets(self):
        for pet, pet_id in self.pet_dict:
            print(f"ID: {pet_id},{pet.display_info()}")






PAS = PetAdoptionSystem()
print('''--- Pet Adoption System ---
1. View Pets
2. Add Pet    
3. Adopt Pet
4. Exit
''')
choice = int(input("Enter your choice: "))
if choice == 1:
    PAS.view_pets()
elif choice == 2:
    species = input("Enter species (Dog/Cat): ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    breed = input("Enter breed: ")
    color = input("Enter color: ")

elif choice == 4:
    print("Thank you for using the Pet Adoption System!")
else:
    print("Invalid choice. Please try again.")

