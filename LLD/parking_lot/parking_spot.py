from abc import ABC, abstractmethod
from vehicle_base import vehicleSize
import threading

"""The ParkingSpot class you've provided is best categorized as an entity.

Explanation:
Entity: In software design, an entity represents a distinct object or concept within the domain of the application. 
In this case, ParkingSpot represents a specific parking spot in a parking lot, encapsulating its properties 
(like spot_id, spot_size, and is_occupied) and behaviors (like park_vehicle and unpark_vehicle).
Why Not Controller or Service?

Controller: Typically handles user input and interacts with the service layer. It would manage the flow of 
data between the user interface and the business logic but does not contain business logic itself.

Service: Contains business logic and operations that can be reused across different parts of the application. 
It usually orchestrates the interaction between entities and may perform operations involving multiple entities.

In summary, ParkingSpot is an entity because it models a specific concept in your application related to parking management."""

class ParkingSpot:
    def __init__(self, spot_id:str, spot_size: vehicleSize):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.is_occupied = False
        self.parked_vehicle = None
        self._lock = threading.Lock()
    
    def __repr__(self):
        return f"ParkingSpot(ID: {self.spot_id}, Size: {self.spot_size.name}, Occupied: {self.is_occupied})"
    
    def get_spot_id(self):
        return self.spot_id
    
    def get_spot_size(self):
        return self.spot_size
    
    def is_available(self):
        return not self.is_occupied
    
    def is_occupied(self):
        return self.is_occupied
    
    def get_parked_vehicle(self):
        return self.parked_vehicle

    def park_vehicle(self, vehicle):
        with self._lock:
            if self.is_occupied:
                raise Exception(f"Spot {self.spot_id} is already occupied.")
            if vehicle.size.value > self.spot_size.value:
                raise Exception(f"Vehicle size {vehicle.size} cannot fit in spot size {self.spot_size}.")
            self.parked_vehicle = vehicle
            self.is_occupied = True
            print(f"Vehicle {vehicle.get_license_number} parked in spot {self.spot_id}.")
    
    def unpark_vehicle(self):
        with self._lock:
            if not self.is_occupied:
                raise Exception(f"Spot {self.spot_id} is already empty.")
            print(f"Vehicle {self.parked_vehicle.get_license_number} leaving spot {self.spot_id}.")
            self.parked_vehicle = None
            self.is_occupied = False
    
    def can_fit_vehicle(self, vehicle):
        return vehicle.size.value <= self.spot_size.value and not self.is_occupied 