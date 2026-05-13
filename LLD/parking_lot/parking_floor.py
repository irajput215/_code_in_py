import threading
from parking_spot import ParkingSpot
from vehicle_base import vehicleSize, vehicle, bike, car, bus
from typing import Dict, Optional
from collections import defaultdict

class ParkingFloor:
    
    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.spots: Dict[str, ParkingSpot] = {}
        self._lock = threading.Lock()

    def add_spots(self, spot: ParkingSpot):
        self.spots[spot.get_spot_id()] = spot
        # print(f"Added {spot} to floor {self.floor_number}.")

    
    def find_available_spot(self, vehicle: vehicle) -> Optional[ParkingSpot]:
        with self._lock:
            available_spots = [
                spot for spot in self.spots.values() 
                if spot.is_available() and vehicle.size.value <= spot.get_spot_size().value
            ]

            if available_spots:
                # Sort available spots by size (smallest first) to optimize space usage
                available_spots.sort(key=lambda s: s.get_spot_size().value)
                return available_spots[0]
        return None

    def display_availability(self):
        print(f"Parking Floor {self.floor_number} Availability:")
        # available_count = defaultdict(int)
        for spot in self.spots.values():
            status = "Available" if spot.is_available() else "Occupied"
            print(f"  - Spot ID: {spot.get_spot_id()}, Size: {spot.get_spot_size().name}, Status: {status}")

