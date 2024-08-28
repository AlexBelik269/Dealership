import sqlite3
class DatabaseConnection:
    _instance = None

    def __new__(cls, database_path='databank.db'):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(database_path)
            cls._instance.cursor = cls._instance.connection.cursor()
        return cls._instance

    def close(self):
        self.connection.close()
        DatabaseConnection._instance = None


def initialize_database():
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute('DROP TABLE IF EXISTS User;')
    cursor.execute('DROP TABLE IF EXISTS Vehicle;')

    cursor.execute('''CREATE TABLE User
                  (UserID INTEGER PRIMARY KEY, 
                   Username TEXT, 
                   Password TEXT,
                   Is_Staff INTEGER DEFAULT 0)
               ''')

    cursor.execute('''CREATE TABLE Vehicle 
                  (VehicleID INTEGER PRIMARY KEY, 
                   VehicleType TEXT, 
                   Brand TEXT, 
                   Model TEXT, 
                   Price INTEGER,
                   Year INTEGER, 
                   Specifications TEXT, 
                   Status TEXT DEFAULT "Available")
               ''')

    Users = [
        # Staff
        ('Manager', '1234', 1),
        ('Salesperson', '5678', 1),
        ('Mechanic', '9012', 1),
        ('Store', '3333', 1),
        ('Boss', '5678', 1),
        ('staff_01', 'pass', 1),
        ('staff_02', '1234', 1),
        ('staff_03', '2024', 1),
        ('staff', '123', 1),

        # Clients
        ('John', 'pass', 0),
        ('Alex', 'hello', 0),
        ('Jane', '12345', 0),
        ('Robert', 'word', 0),
        ('Max', 'qwe', 0),
        ('client_01', '5678', 0),
        ('client_02', 'user2', 0),
        ('client_03', 'XYZ', 0),
        ('client', '123', 0)
    ]
    cursor.executemany("INSERT INTO User (Username, Password, Is_Staff) VALUES (?, ?, ?)", Users)

    Vehicles = [
        ('Car', 'Toyota', 'Camry', 25000, 2021, 'Automatic transmission, Leather seats', 'Available'),
        ('Motorbike', 'Honda', 'CBR600RR', 10000, 2020, '600cc engine, Red color', 'Available'),
        ('Truck', 'Ford', 'F-150', 35000, 2019, '4x4, Extended cab', 'Available'),
        ('Boat', 'Bayliner', '175 Bowrider', 30000, 2018, '17.5 feet length, 135hp engine', 'Available'),
        ('Car', 'BMW', 'X5', 60000, 2023, 'Automatic transmission, All-wheel drive, Leather seats', 'Available'),
        ('Motorbike', 'Ducati', 'Monster 821', 15000, 2022, '821cc engine, Red color', 'Available'),
        ('Truck', 'Chevrolet', 'Silverado 2500', 45000, 2020, '4x4, Crew cab, Diesel engine', 'Available'),
        ('Boat', 'Sea Ray', 'SPX 210', 50000, 2019, '21 feet length, 200hp engine', 'Available'),
        ('Car', 'Mercedes', 'C-Class', 42000, 2021, 'Automatic transmission, Sunroof, Leather seats', 'Available'),
        ('Car', 'Audi', 'Q7', 70000, 2023, 'Automatic transmission, All-wheel drive, Third-row seating', 'Available'),
        ('Motorbike', 'Yamaha', 'MT-09', 12000, 2021, '900cc engine, Black color', 'Available'),
        ('Car', 'BMW', '3 Series', 45000, 2022, 'Automatic transmission, Sunroof, Leather seats', 'Available'),
        ('Truck', 'Ram', '2500', 55000, 2021, '4x4, Mega cab, Diesel engine', 'Unavailable'),
        ('Car', 'Ferrari', '488 Spider', 280000, 2022, 'Automatic transmission, Convertible, V8 engine', 'Unavailable'),
        ('Boat', 'Chaparral', 'H2O Sport', 40000, 2018, '19 feet length, 220hp engine', 'Available'),
        ('Car', 'Tesla', 'Model S', 80000, 2023, 'Electric, Autopilot, Full Self-Driving', 'Unavailable'),
        ('Car', 'Chevrolet', 'Corvette', 70000, 2022, 'Automatic transmission, V8 engine, Convertible', 'Available'),
        ('Car', 'BMW', 'X7', 90000, 2023, 'Automatic transmission, All-wheel drive, Third-row seating', 'Available'),
        ('Car', 'Ford', 'Explorer', 35000, 2021, 'Automatic transmission, All-wheel drive, Third-row seating', 'Available'),
        ('Truck', 'Ram', '3500', 65000, 2020, '4x4, Mega cab, Diesel engine', 'Available'),
        ('Car', 'Honda', 'Civic', 22000, 2022, 'Automatic transmission, Apple CarPlay, Backup camera', 'Available'),
        ('Car', 'Hyundai', 'Tucson', 28000, 2023, 'Automatic transmission, All-wheel drive, Sunroof', 'Available'),
        ('Car', 'BMW', 'i8', 140000, 2021, 'Automatic transmission, Hybrid, Leather seats', 'Available'),
        ('Motorbike', 'Suzuki', 'GSX-R1000', 15000, 2021, '1000cc engine, Blue/White color', 'Available'),
        ('Car', 'Maserati', 'Ghibli', 85000, 2023, 'Automatic transmission, Rear-wheel drive, Sunroof', 'Available'),
        ('Motorbike', 'Kawasaki', 'Z650', 8000, 2022, '650cc engine, Green color', 'Available'),
        ('Truck', 'GMC', 'Sierra 1500', 42000, 2021, '4x4, Crew cab, V8 engine', 'Available'),
        ('Car', 'Porsche', '911', 120000, 2022, 'Automatic transmission, Rear-wheel drive, Leather seats', 'Available'),
        ('Boat', 'Yamaha', '212X', 55000, 2020, '21 feet length, Twin 1.8L engines', 'Available'),
        ('Car', 'Mazda', 'CX-5', 31000, 2022, 'Automatic transmission, All-wheel drive, Sunroof', 'Available'),
        ('Car', 'Nissan', 'Altima', 24000, 2021, 'Automatic transmission, Bluetooth, Backup camera', 'Unavailable'),
        ('Motorbike', 'Harley-Davidson', 'Iron 883', 10000, 2020, '883cc engine, Black color', 'Available'),
        ('Car', 'Volkswagen', 'Golf GTI', 35000, 2022, 'Automatic transmission, Turbocharged, Sunroof', 'Available'),
        ('Car', 'Ferrari', 'F8 Tributo', 270000, 2023, 'Automatic transmission, Coupe, V8 engine', 'Available'),
        ('Truck', 'Toyota', 'Tacoma', 36000, 2021, '4x4, Double cab, V6 engine', 'Available'),
        ('Car', 'Subaru', 'Outback', 33000, 2023, 'Automatic transmission, All-wheel drive, Roof rails', 'Unavailable'),
        ('Boat', 'Bayliner', 'VR6', 45000, 2020, '22 feet length, 200hp engine', 'Available'),
        ('Car', 'BMW', 'Z4', 65000, 2022, 'Automatic transmission, Convertible, Sport package', 'Available'),
        ('Car', 'Bentley', 'Continental GT', 220000, 2021, 'Automatic transmission, All-wheel drive, Leather seats', 'Available'),
        ('Motorbike', 'Triumph', 'Street Triple', 12000, 2021, '765cc engine, Silver color', 'Available')
    ]

    cursor.executemany("INSERT INTO Vehicle (VehicleType, Brand, Model, Price, Year, Specifications, Status)VALUES (?, ?, ?, ?, ?, ?, ?)", Vehicles)

    db.connection.commit()
    db.close()

#initialize_database()
