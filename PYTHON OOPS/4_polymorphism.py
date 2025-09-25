# creating a base class  
class Vertebrate:  
    def __init__(self, name):  
        self.name = name  
  
    def move(self):  
        print(f"{self.name} moves in a generic way.")  
  
# creating a child class  
class Mammal(Vertebrate):  
    def move(self):   # method overriding  
        print(f"{self.name} walks.")  
  
# creating a child class  
class Bird(Vertebrate):  
    def move(self):   # method overriding  
        print(f"{self.name} flies.")  
  
# creating object as a list  
animals = [Vertebrate("Generic Vertebrate"), Mammal("Dog"), Bird("Eagle")]  
  
for animal in animals:  
    animal.move()  