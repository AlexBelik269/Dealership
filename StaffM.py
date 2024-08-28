from Database import DatabaseConnection

db = DatabaseConnection()

def staff_functions():
    print(" ")
    print("Choose Action:  Add (A) / Delete (D) / Configure a Vehicle (C) / List (L) / Exit (E)")

    action = input().upper()

    if action == 'A':
        add_action = input("Do you want to add a Vehicle (V) or a Staff Member (S): ").upper()
        if add_action == 'V':
            add_vehicle()
        elif add_action == 'S':
            add_staff()

    elif action == 'D':
        add_action = input("Do you want to delete a Vehicle (V) a Staff Member (S) or a Client (C): ").upper()
        if add_action == 'V':
            delete_vehicle()
        elif add_action == 'S':
            delete_staff()
        elif add_action == 'C':
            delete_client()

    elif action == 'C':
            configure_vehicle()
    
    elif action == 'L':
        add_action = input("Do you want to list the Clients (C) the Staff Members (S) or the Vehicles (V): ").upper()
        if add_action == 'C':
            list_client()
        elif add_action == 'S':
            list_staff()
        elif add_action == 'V':
            list_vehicle()

# ------ ADD ------ 
def add_vehicle():
    print("Enter below the parameters of the vehicle:")
    vehicle_type_map = { 'C': 'Car', 'M': 'Motorbike', 'T': 'Truck', 'B': 'Boat'}
    vehicle_type_input = input("Vehicle Type (Car/Motorbike/Truck/Boat): ").upper()
    if vehicle_type_input in vehicle_type_map:
        vehicle_type = vehicle_type_map[vehicle_type_input]
    else:
        print("Invalid vehicle type. Please try again.")
        return add_vehicle()
    brand = input("Brand: ")
    model = input("Model: ")
    year = input("Year: ")
    price = input("Price: ")
    specifications = input("Specifications: ")
    cursor = db.cursor
    cursor.execute("INSERT INTO Vehicle (VehicleType, Brand, Model, Price, Year, Specifications) VALUES (?, ?, ?, ?, ?, ?)",
                   (vehicle_type, brand, model, price, year, specifications))
    print("Your vehicle has been added to the inventory.")
    db.connection.commit()
    staff_functions()

def add_staff():
    username = input("Input Username: ")
    password = input("Input Password: ")

    cursor = db.cursor()

    cursor.execute('SELECT COUNT(*) FROM User WHERE Username = ?', (username,))
    result = cursor.fetchone()

    if result[0] > 0:
        print("Username already exists!")
        add_staff()
    else:
        cursor.execute('INSERT INTO User (Username, Password, Is_Staff) VALUES (?, ?, ?)', (username, password, 1))
        db.connection.commit()
        print("Staff member added successfully!")

    staff_functions()



# ------ LIST ------ 
def list_client():
    cursor = db.cursor
    cursor.execute("SELECT * FROM User WHERE Is_Staff = 0")
    clients = cursor.fetchall()

    if clients:
        print("Registered Clients:")
        for client in clients:
            print(f"Number: {client[0]},  Username: {client[1]},  Password: {client[2]}")
    else:
        print("No registered clients found.")

    staff_functions()

def list_staff():
    cursor = db.cursor 
    cursor.execute("SELECT * FROM User WHERE Is_Staff = 1")
    staffM = cursor.fetchall()

    if staffM:
        print("Registered Staff Members:")
        for staff in staffM:
            print(f"Number: {staff[0]},  Username: {staff[1]},  Password: {staff[2]}")
    else:
        print("No registered staff members found.")

    staff_functions()

def list_vehicle():
    cursor = db.cursor 
    cursor.execute("SELECT * FROM Vehicle")
    vehicles = cursor.fetchall()

    if vehicles:
        print("Registered Vehicles:")
        for vehicle in vehicles:
            print(f"Number: {vehicle[0]},  Type: {vehicle[1]},  Brand: {vehicle[2]},  Model: {vehicle[3]},  Year: {vehicle[5]},  Price: {vehicle[4]}, Specifications: {vehicle[6]}, Status: {vehicle[7]}")
    else:
        print("No vehicles found.")

    staff_functions()

# ------ DELETE ------ 
def delete_vehicle():
    cursor = db.cursor
    cursor.execute("SELECT * FROM Vehicle")
    vehicles = cursor.fetchall()

    if vehicles: 
        print("Registered Vehicles:")
        for vehicle in vehicles: 
            print(f"Number: {vehicle[0]},  Type: {vehicle[1]},  Brand: {vehicle[2]},  Model: {vehicle[3]},  Year: {vehicle[5]},  Price: {vehicle[4]}")
    else: 
        print("No vehicles found.")

    vehicle_id = input("Input Vehicle ID to delete: ")
    cursor.execute("DELETE FROM Vehicle WHERE VehicleID = ?", (vehicle_id,))
    db.connection.commit()
    print(f"Vehicle with ID {vehicle_id} has been deleted.")
    staff_functions()

def delete_staff():
    cursor = db.cursor
    cursor.execute("SELECT * FROM User WHERE Is_Staff = 1")
    staffM = cursor.fetchall()

    if staffM:
        print("Registered Staff Members:")
        for staff in staffM: 
            print(f"Number: {staff[0]},  Username: {staff[1]},  Password: {staff[2]}")
    else: 
        print("No registered staff members found.")

    staff_id = input("Input Staff ID to delete: ")
    cursor.execute("DELETE FROM User WHERE UserID = ?", (staff_id,))
    db.connection.commit()
    print(f"Staff with ID {staff_id} has been deleted.")
    staff_functions()

def delete_client():
    cursor = db.cursor
    cursor.execute("SELECT * FROM User WHERE Is_Staff = 0")
    clients = cursor.fetchall()

    if clients:
        print("Registered Clients:")
        for client in clients: 
            print(f"Number: {client[0]},  Username: {client[1]},  Password: {client[2]}")
    else: 
        print("No registered clients found.")

    client_id = input("Input Client ID to delete: ")
    cursor.execute("DELETE FROM User WHERE UserID = ?", (client_id,))
    db.connection.commit()
    print(f"Client with ID {client_id} has been deleted.")
    staff_functions()



# ------ CONFIGURE ------
def configure_vehicle():
    cursor = db.cursor
    cursor.execute("SELECT * FROM Vehicle")
    vehicles = cursor.fetchall()

    if vehicles: 
        print("Registered Vehicles:")
        for vehicle in vehicles: 
            print(f"Number: {vehicle[0]}, Type: {vehicle[1]}, Brand: {vehicle[2]}, Model: {vehicle[3]}, Price: {vehicle[4]}, Year: {vehicle[5]}, Specifications: {vehicle[6]}, Status: {vehicle[7]}")
    else: 
        print("No vehicles found.")
        return

    vehicle_id = input("Input Vehicle ID to configure: ")

    changes = {}
    while True:
        print("Which parameter do you want to change?")
        print("1. Vehicle Type")
        print("2. Brand")
        print("3. Model")
        print("4. Price")
        print("5. Year")
        print("6. Specifications")
        print("7. Status")
        print("8. Save changes and exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            changes['VehicleType'] = input("Enter Vehicle Type: ")
        elif choice == '2':
            changes['Brand'] = input("Enter Brand: ")
        elif choice == '3':
            changes['Model'] = input("Enter Model: ")
        elif choice == '4':
            changes['Price'] = input("Enter Price: ")
        elif choice == '5':
            changes['Year'] = input("Enter Year: ")
        elif choice == '6':
            changes['Specifications'] = input("Enter Specifications: ")
        elif choice == '7':
            changes['Status'] = input("Enter Status: ")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

        more_changes = input("Do you want to change something more? (yes/no): ")
        if more_changes.lower() != 'yes':
            break

    set_clause = ', '.join([f"{key} = ?" for key in changes.keys()])
    values = list(changes.values()) + [vehicle_id]

    cursor.execute(f'''
        UPDATE Vehicle 
        SET {set_clause}
        WHERE VehicleID = ?
    ''', values)

    db.connection.commit()
    print(f"Vehicle with ID {vehicle_id} has been updated.")
    staff_functions()

