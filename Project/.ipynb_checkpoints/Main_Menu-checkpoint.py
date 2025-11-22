import pymysql
from datetime import datetime

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root@1234",
    database="python"
)

# Setup Database
def setup_database():
    # Create the Vehicles table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Vehicles (
            vehicle_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            model VARCHAR(255) NOT NULL,
            make VARCHAR(255) NOT NULL,
            year INTEGER NOT NULL,
            status ENUM('Available', 'Rented') NOT NULL
        )
    """)

    # Create the Customers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            phone VARCHAR(20)
        )
    """)

    # Create the Rentals table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Rentals (
            rental_id INTEGER PRIMARY KEY AUTO_INCREMENT,
            customer_id INTEGER NOT NULL,
            vehicle_id INTEGER NOT NULL,
            start_date DATE,
            end_date DATE,
            status ENUM('Pending', 'Approved', 'Denied', 'Returned') NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
            FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id)
        )
    """)

    conn.commit()

setup_database()



# Menu
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Vehicle")
        print("2. View All Rentals")
        print("9. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            add_vehicle()
        elif choice == '2':
            view_all_rentals()
        elif choice == '9':
            break
        else:
            print("Invalid choice.")

def customer_menu(customer_id):
    while True:
        print("\nCustomer Menu:")
        print("1. View Available Vehicles")
        print("2. Request Vehicle Rental")
        print("4. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            view_available_vehicles()
        elif choice == '2':
            request_vehicle_rental(customer_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")


# Admin Functions
def add_vehicle():
    model = input("Enter model: ")
    make = input("Enter make: ")
    year = input("Enter year: ")
    cursor.execute("INSERT INTO Vehicles (model, make, year, status) VALUES (%s, %s, %s,'Available')", (model, make, year))
    conn.commit()
    print("Vehicle added successfully.")

def view_all_rentals():
    cursor.execute("SELECT * FROM Rentals")
    for row in cursor.fetchall():
        print(row)

# Customer Functions
def view_available_vehicles():
    cursor.execute("SELECT * FROM Vehicles WHERE status = 'Available'")
    for row in cursor.fetchall():
        print(row)

# def request_vehicle_rental(customer_id):
#     vehicle_id = int(input("Enter vehicle ID to rent: "))
#     cursor.execute("INSERT INTO Rentals (customer_id, vehicle_id, start_date, status) VALUES (%s, %s, %s, 'Pending')",
#                    (customer_id, vehicle_id, datetime.now().strftime('%Y-%m-%d')))
#     conn.commit()
#     print("Rental request submitted.")


def request_vehicle_rental(customer_id):
    vehicle_id = int(input("Enter vehicle ID to rent: "))
    start_date = datetime.now().strftime('%Y-%m-%d')  # Assuming rental starts now
    
    # Ensure the database connection is active
    # connect_to_database()
    
    # Step 1: Check if customer exists
    cursor.execute("SELECT customer_id FROM Customers WHERE customer_id = %s", (customer_id,))
    customer = cursor.fetchone()
    
    if not customer:
        print("Error: Customer ID does not exist.")
        return  # Exit the function if customer ID is invalid

    # Step 2: Proceed with rental insertion if customer exists
    try:
        cursor.execute(
            "INSERT INTO Rentals (customer_id, vehicle_id, start_date, status) VALUES (%s, %s, %s, 'Pending')",
            (customer_id, vehicle_id, start_date)
        )
        conn.commit()  # Commit the transaction to save changes
        print("Vehicle rental request submitted successfully!")
    except pymysql.MySQLError as e:
        print("Error adding rental request:", e)


# Main Login System
def main():
    # setup_database()
    print("Welcome to the Vehicle Rental System!")
    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            admin_menu()
        elif choice == '2':
            customer_id = int(input("Enter your customer ID: "))
            setup_database()
            customer_menu(customer_id)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
