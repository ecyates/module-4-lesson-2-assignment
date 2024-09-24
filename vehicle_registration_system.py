# Vehicle Registration System
# Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner. 

# Expected Outcome: Completion of the Vehicle class with the update_owner method 
# and a demonstration script showing the creation of Vehicle objects and updating their owners.


class Vehicle:
    '''Each vehicle has a registration number, vehicle type, and owner'''
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        '''This function updates the Vehicle object's owner to the new owner.'''
        self.owner = new_owner
        
    def display_vehicle(self):
        '''This function displays the Vehicle object's registration number, type, and owner.'''
        print(f"Registration #: {self.reg_num}, Type: {self.type}, Owner: {self.owner}")

vehicles = {}

while True: 
    # Prompt user for action
    action = input("Enter action (register, update, remove, display, exit): ").lower()
    # If user wants to exit, exit
    if action == "exit":
        print("The Vehicle Registration System has closed.")
        break
    try: 
        # If action is register a new vehicle
        if action == "register":
            # Prompt for registration number
            reg_num = input("Enter vehicle registration number: ").upper()
            # If that registration number already exists, alert user
            if reg_num in vehicles:
                print(f"The registration number '{reg_num}' already exists.")
            else: 
                # Prompt user for vehicle type
                type = input("Enter the type of vehicle you're registering (car, bike, motorcycle): ").lower()
                # If type is invalid, alert user
                if type != "car" and type != "bike" and type != "motorcycle": 
                    print("Invalid vehicle type.")
                else: 
                    # Prompt vehicle's owner
                    owner = input("Enter the owner's name: ")
                    # Add vehicle to the dictionary
                    vehicles[reg_num] = Vehicle(reg_num, type, owner)
        # If action is update
        elif action == "update":
            # Prompt registration number to update
            reg_num = input("Enter registration number you'd like to update: ")
            if reg_num in vehicles: 
                # Prompt new owner's name
                new_owner = input("Enter the new owner's name: ")
                # Update the vehicle in the list
                vehicles[reg_num].update_owner(new_owner)
                print(f"Registration number '{reg_num}' was updated to new owner: {new_owner}")
            # If registration number not in list, alert user
            else: 
                print(f"Registration number '{reg_num}' does not exist.")
        # If action is display
        elif action == "display":
            # Iterate over vehicles
            for v in vehicles.keys():
                # Display the vehicle
                vehicles[v].display_vehicle()
        # If action is remove
        elif action == "remove":
            # Prompt the user for the registration number to be removed
            reg_num = input("Enter registration number of vehicle you'd like to remove: ")
            # If the registration number exists, remove it
            if reg_num in vehicles: 
                vehicles.pop(reg_num)
                print(f"Registration number {reg_num} was removed.")
            # Otherwise, alert user
            else: 
                print(f"Registration number {reg_num} not in list, no change made.")
        else: 
            raise ValueError()
    except ValueError:
        print("Invalid input.")
    except Exception as e: 
        print(f"An error occurred: {e}.")