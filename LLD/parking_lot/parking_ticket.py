import uuid
import time
from vehicle_base import vehicle
from parking_spot import ParkingSpot

class ParkingTicket:
    def __init__(self, vehicle: vehicle, spot: ParkingSpot):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = time.time()
        self.exit_time = None

    def get_ticket_id(self):
        return self.ticket_id
    
    def get_vehicle(self):
        return self.vehicle
    
    def get_spot(self):
        return self.spot

    def get_entry_time(self):
        return self.entry_time
    
    def get_exit_time(self):
        return self.exit_time
    
    def set_exit_time(self, exit_time):
        self.exit_time = exit_time
        