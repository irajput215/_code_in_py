from abc import ABC, abstractmethod
from parking_floor import ParkingFloor
from vehicle_base import vehicle, vehicleSize
from parking_spot import ParkingSpot
from typing import Optional, List, Dict

class ParkingStrategy(ABC):
    @abstractmethod
    def find_spot(self, parking_floors: List[ParkingFloor], vehicle: vehicle) -> Optional[ParkingSpot]:
        pass

class NearestFirstStrategy(ParkingStrategy):
    def find_spot(self, parking_floors: List[ParkingFloor], vehicle: vehicle) -> Optional[ParkingSpot]:
        for floor in parking_floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                return spot
        return None

class FarthestFirstStrategy(ParkingStrategy):
    def find_spot(self, parking_floors: List[ParkingFloor], vehicle: vehicle) -> Optional[ParkingSpot]:
        for floor in reversed(parking_floors):
            spot = floor.find_available_spot(vehicle)
            if spot:
                return spot
        return None
    
class BestFitStrategy(ParkingStrategy):
    def find_spot(self, parking_floors: List[ParkingFloor], vehicle: vehicle) -> Optional[ParkingSpot]:
        best_spot = None
        for floor in parking_floors:
            for spot in floor.spots.values():
                if spot.is_available() and vehicle.size.value <= spot.get_spot_size().value:
                    if not best_spot or spot.get_spot_size().value < best_spot.get_spot_size().value:
                        best_spot = spot
        return best_spot