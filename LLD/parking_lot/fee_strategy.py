from abc import ABC, abstractmethod
from parking_ticket import ParkingTicket
from vehicle_base import vehicle, vehicleSize

class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, ticket: ParkingTicket) -> float:
        pass

class FlatRateStrategy(FeeStrategy):
    RATE_PER_HOUR = 10

    def calculate_fee(self, ticket :ParkingTicket) -> float:
        duration_hours = (ticket.get_exit_time() - ticket.get_entry_time()) / 3600

        return self.RATE_PER_HOUR * duration_hours

class VehicleBasedFeeStrategy(FeeStrategy):
    RATES = {
        vehicleSize.SMALL: 5,
        vehicleSize.MEDIUM: 10,
        vehicleSize.LARGE: 15
    }

    def calculate_fee(self, ticket: ParkingTicket) -> float:
        duration_hours = (ticket.get_exit_time() - ticket.get_entry_time()) / 3600
        vehicle_size = ticket.get_vehicle().get_size()

        return self.RATES[vehicle_size] * duration_hours

