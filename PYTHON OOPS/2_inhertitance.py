# creating a class (parent class)  
class Vertebrate:  
    def __init__(self, name):  
        self.name = name  
        self.spine = True  
  
    def move(self):  
        print(f"{self.name} is moving.")  
  
# creating another class (child class)  
class Mammal(Vertebrate):  
    def __init__(self, name, fur_color):  
        super().__init__(name)  
        self.fur_color = fur_color  
  
    def nurse(self):  
        print(f"{self.name} is nursing its young.")  
  
# creating another class (child class)  
class Bird(Vertebrate):  
    def __init__(self, name, wingspan):  
        super().__init__(name)  
        self.wingspan = wingspan  
    def fly(self):  
        print(f"{self.name} is soaring through the air.")  
  
# creating an object of Mammal class  
dog = Mammal("Bear", "brown")  
dog.move()  
dog.nurse()  
print("Spine Exist?:", dog.spine)  
  
# creating an object of Bird class  
eagle = Bird("Eagle", 2)  
eagle.move()  
eagle.fly()  
print("Spine Exist?:", eagle.spine)  