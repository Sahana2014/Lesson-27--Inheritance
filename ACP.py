class Vehicle:
    def __init__(self, fare_per_km):
        self.fare_per_km = fare_per_km
    def calculate_fare(self, distance):
        return self.fare_per_km * distance
class Bus(Vehicle):
    def __init__(self, fare_per_km):
        super().__init__(fare_per_km)
    def total_fare(self, distance):
        return self.calculate_fare(distance)
fare_per_km = 3
distance = int(input("Enter the distance to travel in km: "))
bus = Bus(fare_per_km)
total_fare = bus.total_fare(distance)
print("The total fare for" ,distance, "km is: ",total_fare)