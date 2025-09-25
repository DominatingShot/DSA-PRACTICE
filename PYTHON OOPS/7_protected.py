class Car:  
    def __init__(self, brand, model, engine):  
        self.brand = brand  # Public attribute  
        self._model = model  # Protected attribute  
        self._engine = engine  # Protected attribute  
  
    def _show_details(self):  # Protected method  
        print(f"Brand: {self.brand}, Model: {self._model}, Engine: {self._engine}")  
  
class ElectricCar(Car):  
    def __init__(self, brand, model, battery_capacity):  
        super().__init__(brand, model, "Electric")  
        self.battery_capacity = battery_capacity  
  
    def show_info(self):  
        self._show_details()  # Accessing protected method from subclass  
        print(f"Battery: {self.battery_capacity} kWh")  
  
# Creating an object of ElectricCar  
tesla = ElectricCar("Tesla", "Model S", 100)  
  
# Accessing protected members from subclass  
tesla.show_info()  
  
# Accessing protected members outside the class (not recommended)  
print(tesla._model)  # Works, but not recommended  