class Animal:
    def __init__(self, name, age , species):
        self.name = name
        self.age = age
        self.species = species
        
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Species: {self.species}")
        
class Lion(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        
    def make_sound(self):
        return "Roar!"
    
    def info(self):
        super().info()
        print("I am the king of the Jungle")
    
        
class Parrot(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        
    def make_sound(self):
        return "Squawk!"
    
    def info(self):
        super().info()
        print("I can mimic human speech")
        
class Snake(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)
        
    def make_sound(self):
        return "Hiss!"
    
    def info(self):
        super().info()
        print("I slither silently")
        
class Zoo(Animal):
    def __init__(self):
        self.list_animals = []
        
    def add_animal(self, animal):
        self.list_animals.append(animal)
        
    def make_all_sound(self):
        for animal in self.list_animals:
            animal.info()
            print(animal.make_sound())
            print()

def main():
    my_zoo = Zoo()

    my_zoo.add_animal(Lion("Leo", 5, "Lion"))
    my_zoo.add_animal(Parrot("Polly", 2, "Parrot"))
    my_zoo.add_animal(Snake("Slither", 4, "Snake"))

    my_zoo.make_all_sound()
    
if __name__ == '__main__':
    main()
