from Database import DatabaseConnection
import re

db = DatabaseConnection()

def client_functions():
    print("  ")
    print("Do you want to:")
    print("- Buy a Vehicle (B / buy)")
    print("- Sell a Vehicle (S / sell)")
    print("- Rent a Vehicle (R / rent)")
    print("- Search a Vehicle (SRC / search)")
    print("- Browse all Vehicles (BRW / browse)")

    action = input().upper()

    if action in ['B', 'BUY']:
        buy_vehicle()
    elif action in ['S', 'SELL']:
        sell_vehicle()
    elif action in ['R', 'RENT']:
        rent_vehicle()
    elif action in ['SRC', 'SEARCH']:
        search_vehicle()
    elif action in ['BRW', 'BROWSE']:
        browse_vehicles()


def display_vehicles(vehicle_type=None):
    cursor = db.cursor

    if vehicle_type:
        cursor.execute("SELECT * FROM Vehicle WHERE VehicleType = ?", (vehicle_type,))
    else:
        cursor.execute("SELECT * FROM Vehicle")

    vehicles = cursor.fetchall()

    if vehicles:
        print("Available Vehicles:")
        for vehicle in vehicles:
            print(f"Number: {vehicle[0]},  Type: {vehicle[1]},  Brand: {vehicle[2]},  Model: {vehicle[3]},  Year: {vehicle[5]},  Price: {vehicle[4]}")
    else:
        print("No vehicles found.")


def process_card_payment(price):
    card_number_pattern = r"\d{16}"   # 16 digits
    name_pattern = r"[A-Za-z\s]+"     # Alphabets and spaces only
    exp_date_pattern = r"\d{2}/\d{4}" # MM/YYYY format
    cvv_pattern = r"\d{3}"            # 3 digits

    while True:
        card_number = input("Enter Card Number (16 digits): ")
        if re.match(card_number_pattern, card_number):
            break
        else:
            print("Invalid format! Please enter 16 digits.")

    while True:
        name = input("Enter Name: ")
        if re.match(name_pattern, name):
            break
        else:
            print("Invalid format! Please enter letters and spaces only.")

    while True:
        exp_date = input("Enter Expiration Date (MM/YYYY): ")
        if re.match(exp_date_pattern, exp_date):
            break
        else:
            print("Invalid format! Please enter in MM/YYYY format.")

    while True:
        cvv = input("Enter CVV (3 digits): ")
        if re.match(cvv_pattern, cvv):
            break
        else:
            print("Invalid format! Please enter 3 digits.")

    #print("Thank you for purchasing! Have a nice day :)")


# Devides price in monthly payments
def process_leasing_payment(price):
    months = int(input("Enter the number of Months you want the Amount to divide along: "))
    print(f"Your monthly payment will be {'{:.2f}'.format(((price * 0.8) * 1.05) / months)}")
    print(f"And you first payment will be {'{:.2f}'.format(price * 0.2)}")
    print("Pay by card:")
    process_card_payment(price)




# ------ BUY ------ 
def buy_vehicle():
    cursor = db.cursor
    print("Are you interested in a Car (C) / Motorbike (M) / Truck (T) / Boat (B) or would you like to browse them all (BRW)?")
    vehicle_type_input = input().upper()
    vehicle_type_map = {
        'C': 'Car',
        'M': 'Motorbike',
        'T': 'Truck',
        'B': 'Boat'
    }

    if vehicle_type_input in vehicle_type_map:
        vehicle_type = vehicle_type_map[vehicle_type_input]
        display_vehicles(vehicle_type)
    elif vehicle_type_input == 'BRW':
        display_vehicles()
    else:
        print("Invalid input. Please try again.")
        return

    choice = input("Did any catch your eye? (Yes: Input Number / No: N)  ").upper()
    if choice != 'N':
        cursor.execute("SELECT Price FROM Vehicle WHERE VehicleID = ?", (choice,))  
        result = cursor.fetchone()
        if result:
            price = result[0]
            decision = input(f"Would you be interested in buying this vehicle for {price} dollars? (Yes: Y / No: N / Negotiate: NEG)  ").upper()
            # Pay normally
            if decision == 'Y':
                pay_method = input("Perfect! How would you like to pay? (Card: C / Leasing: L)").upper()
                if pay_method == 'C':
                    process_card_payment(price)
                elif pay_method == 'L':
                    process_leasing_payment(price)
                else:
                    print("Invalid payment method.")

                cursor.execute("DELETE FROM Vehicle WHERE VehicleID = ?", (choice,))
                db.connection.commit()

                print("Thank you for your purchase!")
                client_functions()
            
            # Negotiate the price
            elif decision == 'NEG':
                offer_price = float(input("Make your price offer: "))
                price_difference = offer_price - price
                if abs(price_difference / price) <= 0.05:
                    print("We accept this new offer. You are a good Salesman, congratulations!")

                    payment_method = input("How would you like to pay? (Card: C / Leasing: L)").upper()
                    if payment_method == 'C':
                        process_card_payment(offer_price)
                    elif payment_method == 'L':
                        process_leasing_payment(offer_price)
                    else:
                        print("Invalid payment method.")

                    cursor.execute("DELETE FROM Vehicle WHERE VehicleID = ?", (choice,))
                    db.connection.commit()
                    print("Thank you for your purchase!")
                    client_functions()

                else:
                    print("We are deeply sorry, but we cannot accept this offer.")
                    buy_vehicle()
            elif decision == 'N':
                print("We are sorry that nothing interested you.")
                client_functions()
            else:
                print("Invalid input.")
                buy_vehicle()
        else:
            print("Invalid vehicle number.")
            buy_vehicle()
    else:
        print("We are sorry!")
        client_functions()

    client_functions()



# ------ SELL ------ 
def sell_vehicle():
    print("We are happy that you have decided to sell your vehicle with us.")
    print("Enter the parameters of the vehicle below:")

    vehicle_type_map = {
        'C': 'Car',
        'M': 'Motorbike',
        'T': 'Truck',
        'B': 'Boat'
    }

    vehicle_type_input = input("Vehicle Type (Car/Motorbike/Truck/Boat): ").upper()

    if vehicle_type_input in vehicle_type_map:
        vehicle_type = vehicle_type_map[vehicle_type_input]
    else:
        print("Invalid vehicle type. Please try again.")
        return sell_vehicle()

    brand = input("Brand: ")
    model = input("Model: ")
    year = input("Year: ")
    price = input("Price: ")
    specifications = input("Specifications: ")

    cursor = db.cursor

    cursor.execute("INSERT INTO Vehicle (VehicleType, Brand, Model, Price, Year, Specifications, Status) VALUES (?, ?, ?, ?, ?, ?, 'Available')",
                   (vehicle_type, brand, model, price, year, specifications))
    print("Your vehicle has been added to our inventory. You will be notified when someone purchases it.")
    db.connection.commit()
    client_functions()



# ------ RENT ------ 
def rent_vehicle():
    print("Choose from the Vehicles available for rent below.")
    cursor = db.cursor
    cursor.execute("SELECT * FROM Vehicle WHERE Status = 'Available'")
    vehicles = cursor.fetchall()

    if vehicles:
        for vehicle in vehicles:
            print(f"Number: {vehicle[0]},  Type: {vehicle[1]},  Brand: {vehicle[2]},  Model: {vehicle[3]},  Year: {vehicle[5]},  Price: {vehicle[4]}")
    else:
        print("No vehicles found.")
        client_functions()
        return

    vehicle_id = input("Enter ID of the vehicle you want to rent: ")
    cursor.execute("SELECT * FROM Vehicle WHERE VehicleID = ? AND Status = 'Available'", (vehicle_id,))
    vehicle = cursor.fetchone()

    if vehicle:
        rent_type = input("Are you interested in Short-Term Rent (S) or Long-Term Rent (L)?").upper()
        if rent_type == 'S':
            num_days = int(input("For how many days would you like to rent this vehicle? Enter the number of days: "))
            price = vehicle[4] * 0.003 * num_days
            print(f"The price will be around {price:.2f} dollars.")
        elif rent_type == 'L':
            num_months = int(input("For how many months would you like to rent this vehicle? Enter the number of months: "))
            price = vehicle[4] * 0.05 * num_months
            print(f"The price will be around {price:.2f} dollars.")
        else:
            print("Invalid choice.")
            client_functions()
            return

        age_confirmation = input("Are you at least 20 years old? (Y/N): ").upper()

        if age_confirmation == 'Y':
            payment_choice = input("How would you like to pay the deposit? at Pick up (P) / Credit Card (C): ").upper()

            if payment_choice == 'C':
                process_card_payment(price)
            elif payment_choice == 'P':
                print("Payment at pickup. Thank you!")
                client_functions()
            else:
                print("Invalid payment choice.")
                client_functions()
                return

            cursor.execute("UPDATE Vehicle SET Status = 'Unavailable' WHERE VehicleID = ?", (vehicle_id,))
            db.connection.commit()
            print("The vehicle has been reserved for you. Enjoy your rental!")

        elif age_confirmation == 'N':
            print("We are sorry, but if you are under 20 years old we cannot rent you this Vehicle.")
        else:
            print("Invalid choice.")
    else:
        print("Invalid vehicle ID or the vehicle is not available.")

    client_functions()



# ------ SEARCH --------
def search_vehicle():
    cursor = db.cursor
    brand = input("Input the Brand you want to search for: ").strip()
    cursor.execute("SELECT * FROM Vehicle WHERE Brand = ? AND Status = 'Available'", (brand,))
    vehicles = cursor.fetchall()
   
    if vehicles:
        print(f"Below is a list of all available vehicles for brand '{brand}':")
        for vehicle in vehicles:
            print(f"Number: {vehicle[0]},  Type: {vehicle[1]},  Brand: {vehicle[2]},  Model: {vehicle[3]},  Year: {vehicle[5]},  Price: {vehicle[4]}")
    else:
        print(f"No available vehicles found for brand '{brand}'.")
 
    client_functions()


# ------ BROWSE ------ 
def browse_vehicles():
    cursor = db.cursor
    cursor.execute("SELECT * FROM Vehicle WHERE Status = 'Available'")
    vehicles = cursor.fetchall()

    if vehicles:
        print("Below is a list of all available vehicles: ")
        for vehicle in vehicles:
            print(f"Number: {vehicle[0]},  Type: {vehicle[1]},  Brand: {vehicle[2]},  Model: {vehicle[3]},  Year: {vehicle[5]},  Price: {vehicle[4]}")
    else:
        print("No vehicles found.")

    client_functions()

