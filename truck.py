class Truck:
    # Complexity O(1)
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.packages = []
        self.mileage = 0.0
        self.current_location = "HUB"


