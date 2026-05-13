import threading
from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket
from fee_strategy import FeeStrategy, FlatRateStrategy, VehicleBasedFeeStrategy
from parking_strategy import ParkingStrategy, NearestFirstStrategy, FarthestFirstStrategy, BestFitStrategy
from typing import List, Dict
import time

class ParkingLot:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if self._instance is not None:
            raise Exception("This class is a singleton!")
        self.floors : List[ParkingFloor] = []
        self.active_tickets: Dict[str, ParkingTicket] = {}
        self.fee_strategy: FeeStrategy = FlatRateStrategy()
        self.parking_strategy = NearestFirstStrategy()
        self._main_lock = threading.Lock()

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance
    
    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)
    
    def set_fee_strategy(self, strategy: FeeStrategy):
        self.fee_strategy = strategy
    
    def set_parking_strategy(self, strategy: ParkingStrategy):
        self.parking_strategy = strategy
    
    def park_vehicle(self, vehicle) -> ParkingTicket:
        with self._main_lock:
            spot = self.parking_strategy.find_spot(self.floors, vehicle)
            if not spot:
                raise Exception("No available parking spots for this vehicle.")
            
            spot.park_vehicle(vehicle)
            ticket = ParkingTicket(vehicle, spot)
            self.active_tickets[ticket.get_ticket_id()] = ticket
            return ticket
    
    def unpark_vehicle(self, ticket_id: str) -> float:
        with self._main_lock:
            if ticket_id not in self.active_tickets:
                raise Exception("Invalid ticket ID.")
            
            ticket = self.active_tickets.pop(ticket_id)
            ticket.set_exit_time(time.time())
            fee = self.fee_strategy.calculate_fee(ticket)
            ticket.get_spot().unpark_vehicle()
            return fee
        

