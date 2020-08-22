class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers =  []

# Adding passenger
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

# Checking for seats availability
    def open_seats(self):
        return self.capacity - len(self.passengers)

# Object of class Flight
flight  = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny", "Luna"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to the flight successfully.")
    else:
        print(f"No seats available for {person}")