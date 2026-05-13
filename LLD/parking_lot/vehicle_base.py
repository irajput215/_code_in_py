from enum import Enum
from abc import ABC,abstractmethod

class vehicleSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

# i wanna create the base vehicle class

class vehicle(ABC):
    def __init__(self, license_number: str, size: vehicleSize):
        self.license_number = license_number
        self.size = size

        
    def get_license_number(self):
        return self.license_number
    
    def get_size(self):
            return self.size

# create concrete vehicle classes    
class bike(vehicle):
    def __init__(self, license_number, size):
        super().__init__(license_number, vehicleSize.SMALL)

class car(vehicle):
    def __init__(self, license_number, size):
        super().__init__(license_number, vehicleSize.MEDIUM)

class bus(vehicle):
    def __init__(self, license_number, size):
        super().__init__(license_number, vehicleSize.LARGE)