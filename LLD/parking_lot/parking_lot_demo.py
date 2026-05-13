from parking_floor import ParkingFloor
from parking_lot import ParkingLot
from parking_strategy import NearestFirstStrategy, BestFitStrategy
from vehicle_base import vehicleSize, bike, car, bus
from parking_spot import ParkingSpot

class ParkingLotDemo:

    @staticmethod
    def main():

        parking_lot = ParkingLot.get_instance()

        # Create parking floors and spots
        floor1 = ParkingFloor(1)
        floor1.add_spots(ParkingSpot("F1S1", vehicleSize.SMALL))
        floor1.add_spots(ParkingSpot("F1S2", vehicleSize.MEDIUM))
        floor1.add_spots(ParkingSpot("F1S3", vehicleSize.LARGE))

        floor2 = ParkingFloor(2)
        floor2.add_spots(ParkingSpot("F2S1", vehicleSize.SMALL))
        floor2.add_spots(ParkingSpot("F2S2", vehicleSize.MEDIUM))
        floor2.add_spots(ParkingSpot("F2S3", vehicleSize.LARGE))

        parking_lot.add_floor(floor1)
        parking_lot.add_floor(floor2)

        # Set parking strategy
        parking_lot.set_parking_strategy(NearestFirstStrategy())

        # Park vehicles
        bike1 = bike("BIKE123", vehicleSize.SMALL)
        car1 = car("CAR456", vehicleSize.MEDIUM)
        bus1 = bus("BUS789", vehicleSize.LARGE)

        ticket1 = parking_lot.park_vehicle(bike1)
        print(f"Parked {bike1.get_license_number()} at spot {ticket1.get_spot().get_spot_id()}")

        ticket2 = parking_lot.park_vehicle(car1)
        print(f"Parked {car1.get_license_number()} at spot {ticket2.get_spot().get_spot_id()}")

        ticket3 = parking_lot.park_vehicle(bus1)
        print(f"Parked {bus1.get_license_number()} at spot {ticket3.get_spot().get_spot_id()}")

        # Display parking floor availability

        floor1.display_availability()
        floor2.display_availability()

        #5 simulate unparking
        print("Unparking vehicles...")

        if ticket2:
            fee = parking_lot.unpark_vehicle(ticket2.get_ticket_id())
            print(f"Unparked {car1.get_license_number()} with fee: ${fee:.2f}")

        # availabilty after one car leaves
        floor1.display_availability()
        floor2.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.main()
