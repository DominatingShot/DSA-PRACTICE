# importing the ABC class and abstractmethod decorator from abc module  
from abc import ABC, abstractmethod  
  
# creating a class  
class Three_Dimensional_Shapes(ABC):  
  @abstractmethod  
  def calc_volume(self):  
    pass  
  
# creating another class to implement abstraction  
class Cube(Three_Dimensional_Shapes):  
  def __init__(self, side_length):  
    self.side_length = side_length  
  
  def calc_volume(self):  
    return self.side_length ** 3  
  
# creating an object of Cube class  
side_length = 6  
cube = Cube(side_length)  
  
# printing the results  
print("Cube's Side:", side_length)  
print("Cube's Volume:", cube.calc_volume())  