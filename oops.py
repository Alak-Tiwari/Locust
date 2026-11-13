#from abc import ABC,abstractmethod 
class Vehicle():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    #@abstractmethod
    def display_info(self):
        print(f"Vehicle:{self.brand} : {self.model}")

class Car(Vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color=color

    def display_info(self):
         super().display_info()
         print(f"color:{self.color}")


car=Car("Honda","City 91X0","Black")
car.display_info()


    