class Employer:
  x = 0  
  def __init__(self, name, industry):  
    self.name = name          # attribute  
    self.industry = industry  # attribute  
  
  @classmethod
  def display_info(cls,self):     # method  
    print(f"Employer: {self.name} - {self.industry} , {cls.x}") 

  @staticmethod
  def add():
    return 5+6 
  
# # Creating an object  
# employer_one = Employer("Tpoint Tech", "Education")  
# employer_one.display_info(employer_one)  

# class Employer:
#     x = 0  
#     def __init__(self, name, industry):  
#         self.name = name          
#         self.industry = industry  
    
#     def display_info(self):     
#         print(f"Employer: {self.name} - {self.industry} , {self.__class__.x}")  

# # Creating an object  
# employer_one = Employer("Tpoint Tech", "Education")  
# employer_one.display_info()   
