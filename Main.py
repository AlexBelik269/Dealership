from Database import DatabaseConnection
from StaffM import staff_functions
from Client import client_functions

def main():
    while True:
        print(" ")
        print("Welcome to the Royal Ride Dealership Centre!")
        print("Login (L) / Register (R) / Exit (E)")

        choice = input("Enter your choice: ").upper()

        if choice == 'L':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == 'R':
            username = input("Enter username: ")
            password = input("Enter password: ")
            is_staff = int(input("Enter 1 for staff, 0 for client: "))
            register(username, password, is_staff)
        elif choice == 'E':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# ------ LOGIN ------ 
def login(username, password):
    db = DatabaseConnection()
    cursor = db.cursor

    cursor.execute("SELECT Is_Staff FROM User WHERE Username=? AND Password=?", (username, password))
    result = cursor.fetchone()

    if result:
        is_staff = result[0]
        if is_staff == 1:
            print("Welcome Staff!")
            staff_functions()
        else:
            print("Welcome Client!")
            client_functions()
    else:
        print("Invalid username or password")


# ------ REGISTER ------ 
def register(username, password, is_staff):
    db = DatabaseConnection()
    cursor = db.cursor

    cursor.execute("SELECT * FROM User WHERE Username=?", (username,))
    if cursor.fetchone():
        print("Username already exists. Please choose a different username.")
    else:
        cursor.execute("INSERT INTO User (Username, Password, Is_Staff) VALUES (?, ?, ?)", (username, password, is_staff))
        db.connection.commit()
        print("Registration successful!")

if __name__ == "__main__":
    main()
