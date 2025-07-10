#class that represents a flight with a certain capacity
class Flight():
    # __init__ method to initialize the flight with a given capacity
    def __init__(self,capacity): # Constructor
        # Initialize the flight with a given capacity
        self.capacity = capacity
        self.passengers = []      # List to store passengers
    
    def is_full(self):  # Method to check if the flight is full
        # Check if the number of passengers is equal to the capacity
        return len(self.passengers) == self.capacity
    
    def add_passenger(self, name):    # Method to add a passenger to the flight
        # Add a passenger to the flight if there is space available
        if self.is_full():      #check if the flight is full
            # If the flight is full, print a message and return
            print(f"Sorry, the flight is full. {name} cannot be added.")
            return
            
        if name in self.passengers:    # Check if the passenger is already registered
            print(f"{name} is already registered in the flight")
        else:    
            self.passengers.append(name)
            print(f"{name} has been added to the flight.")
    
    def open_seats(self):     # Method to check how many seats are open
        # Calculate the number of open seats by subtracting the number of passengers from the capacity
        return self.capacity - len(self.passengers)
    
    
        

# Main program to create a flight and add passengers
flight_capacity = int(input("Enter the flight capacity: "))  # Get flight capacity from user
flight = Flight(flight_capacity)

while not flight.is_full():
    
    passenger_name = input("Enter the passenger name or enter 'exit' to stop adding passengers: ")
    if passenger_name.lower() == "exit":
        break

    flight.add_passenger(passenger_name) # Add the passenger to the flight

# Print the list of passengers in the flight
    print("_______________________________________________________________________________")
    print("| List of passengers in the flight:  | Flight Capacity =", flight.capacity, " | Open Seats =", flight.open_seats(), "|")
    print("_______________________________________________________________________________")
    for j in range(len(flight.passengers)):
        
        print("|", (j +1), "- |", flight.passengers[j], "|")  # Print the list of passengers in the flight
        print("_____________________________________________")

