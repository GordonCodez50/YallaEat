import mysql.connector
import os
import time
from datetime import datetime
from tabulate import tabulate

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '1234'

# Clear terminal screen
def clear_screen():
    os.system("cls")

#box type header
def print_header(title):
    width = 60
    print("\n" + "=" * width)
    print("|" + title.center(width -2) + "|")
    print("=" * width + "\n")

#message box
def print_message(message):
    print("\n" + message + "\n")

#loading animation
def show_loading(message):
    print(message + ".")
    time.sleep(0.3)
    print(message + "..")
    time.sleep(0.3)
    print(message + "...")
    time.sleep(0.3)
    print(message + "... Done!")

def init_db():
    try:
        show_loading("Connecting to database")
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS yallaeat_db")
        cursor.execute("USE yallaeat_db")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE,
                password VARCHAR(255),
                role VARCHAR(20)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS restaurants (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                location VARCHAR(50)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu (
                id INT AUTO_INCREMENT PRIMARY KEY,
                restaurant_id INT,
                item_name VARCHAR(255),
                price DECIMAL(10, 2),
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                menu_id INT,
                quantity INT,
                total_price DECIMAL(10, 2),
                delivery_charge DECIMAL(10, 3),
                delivery_time INT,
                user_location VARCHAR(50),
                status VARCHAR(20) DEFAULT 'Pending',
                order_date DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (menu_id) REFERENCES menu(id)
            )
        """)
        
        cursor.close()
        conn.close()
        print_message("Database initialized successfully")
        
    except Exception as e:
        print_message(f"Database error: {str(e)}")
        print_message("Please check your database settings")

def get_db_connection():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database='yallaeat_db'
    )
    return conn

def execute_query(query, params=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except:
        print_message("Error")
        return False

def fetch_all(query, params=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except:
        print_message("Error")
        return False

def register_user():
    print_header("Create New Account")
    
    name = input("Enter your name: ").strip()
    if not name:
        print_message("Name cannot be empty")
        return
    
    password = input("Enter password: ").strip()
    if not password:
        print_message("Password cannot be empty")
        return
    
    print("\n[1] User Account")
    print("\n[2] Admin Account")
    role_choice = input("Select account type: ").strip()
    
    if role_choice == "1":
        role = "user"
        username = "user-" + name.replace(" ", "")
    elif role_choice == "2":
        role = "admin"
        username = "admin-" + name.replace(" ", "")
    else:
        print_message("Invalid choice")
        return
    
    # Check if username already exists
    existing = fetch_all("SELECT id FROM users WHERE username = %s", (username,))
    if existing:
        message = "Username '" + username + "' already exists. Try a different name."
        print_message(message)
        return
    
    success = execute_query(
        "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
        (username, password, role)
    )
    
    if success:
        message = "Account created! Your username is: " + username
        print_message(message)
    time.sleep(3)

def login():
    print_header("Login")
    
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    user = fetch_all(
        "SELECT id, username, role FROM users WHERE username = %s AND password = %s",
        (username, password)
    )
    
    if user:
        print_message("Login successful!")
        time.sleep(0.5)
        user_id = user[0][0]
        username = user[0][1]
        role = user[0][2]
        return user_id, username, role
    else:
        print_message("Invalid username or password")
        time.sleep(1)
        return None

def admin_menu():
    while True:
        clear_screen()
        print_header("ADMIN MENU")
        print(" [1] Add Restaurant")
        print(" [2] Add Menu Item")
        print(" [3] View All Orders")
        print(" [4] Update Order Status")
        print(" [5] Delete Menu Item")
        print(" [6] View All Users")
        print(" [7] Logout")
        print("\n" + "-" * 60)
        
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == '1':
            add_restaurant()
        elif choice == '2':
            add_menu_item()
        elif choice == '3':
            view_all_orders()
        elif choice == '4':
            update_order_status()
        elif choice == '5':
            delete_menu_item()
        elif choice == '6':
            view_all_users()
        elif choice == '7':
            print_message("Logging out...")
            break
        else:
            print_message("Invalid choice. Please enter 1-7")
            time.sleep(1)

def add_restaurant():
    clear_screen()
    print_header("Add Restaurant")
    
    name = input("Enter restaurant name: ").strip()
    if not name:
        print_message("Restaurant name cannot be empty")
        time.sleep(1.5)
        return
    
    print("\nSelect restaurant location:")
    print("  [1] Adliya")
    print("  [2] Manama")
    print("  [3] Muharraq")
    print("  [4] Juffair")
    location_choice = input("Choose location (1-4): ").strip()
    
    if location_choice == "1":
        location = "Adliya"
    elif location_choice == "2":
        location = "Manama"
    elif location_choice == "3":
        location = "Muharraq"
    elif location_choice == "4":
        location = "Juffair"
    else:
        print_message("Invalid location choice")
        time.sleep(1.5)
        return
    success = execute_query("INSERT INTO restaurants (name, location) VALUES (%s, %s)", (name, location))
    if success:
        message = "Restaurant added successfully in " + location + "!"
        print_message(message)
    time.sleep(1)

def add_menu_item():
    clear_screen()
    print_header("Add Menu Item")
    
    # Show restaurants
    restaurants = fetch_all("SELECT id, name, location FROM restaurants")
    if not restaurants:
        print_message("No restaurants found. Add a restaurant first.")
        time.sleep(1.5)
        return
    
    print(tabulate(restaurants, headers=["ID", "Restaurant Name", "Location"], tablefmt="grid"))
    
    try:
        restaurant_id = int(input("\nEnter restaurant ID: "))
        item_name = input("Enter item name: ").strip()
        price = float(input("Enter price: "))
        
        if not item_name or price <= 0:
            print_message("Invalid input")
            time.sleep(1.5)
            return
        
        success = execute_query(
            "INSERT INTO menu (restaurant_id, item_name, price) VALUES (%s, %s, %s)",
            (restaurant_id, item_name, price)
        )
        if success:
            print_message("Menu item added successfully!")
        time.sleep(1)
        
    except ValueError:
        print_message("Please enter valid numbers")
        time.sleep(1.5)

def view_all_orders():
    clear_screen()
    print_header("All Orders")
    
    # Update statuses before showing
    update_delivery_status()
    
    orders = fetch_all("""
        SELECT order.id, user.username, menu.item_name, order.quantity, order.total_price, order.delivery_charge, order.user_location, order.status, order.order_date
        FROM orders order
        JOIN users user ON order.user_id = user.id
        JOIN menu menu ON order.menu_id = menu.id
        ORDER BY order.order_date DESC
    """)
    
    if not orders:
        print_message("No orders found")
    else:
        print(tabulate(orders, 
                      headers=["ID", "User", "Item", "Qty", "Total", "Delivery", "Location", "Status", "Date"],
                      tablefmt="grid"))
    
    input("\nPress Enter to continue...")

def update_order_status():
    clear_screen()
    print_header("Update Order Status")
    
    # Update statuses before showing
    update_delivery_status()
    
    # Show current orders
    orders = fetch_all("SELECT id, status FROM orders ORDER BY id DESC LIMIT 10")
    if not orders:
        print_message("No orders found")
        time.sleep(1)
        return
    
    print(tabulate(orders, headers=["Order ID", "Current Status"], tablefmt="grid"))
    
    try:
        order_id = int(input("\nEnter order ID: "))
        print("\n[1] Pending")
        print("[2] Delivered")
        print("[3] Cancelled")
        status_choice = input("Select new status (1-3): ").strip()
        
        if status_choice == "1":
            new_status = "Pending"
        elif status_choice == "2":
            new_status = "Delivered"
        elif status_choice == "3":
            new_status = "Cancelled"
        else:
            print_message("Invalid choice")
            time.sleep(1)
            return
        
        success = execute_query(
            "UPDATE orders SET status = %s WHERE id = %s",
            (new_status, order_id)
        )
        if success:
            print_message("Order status updated!")
        time.sleep(1)
        
    except ValueError:
        print_message("Please enter a valid order ID")
        time.sleep(1.5)

def delete_menu_item():
    clear_screen()
    print_header("Delete Menu Item")
    
    # Show all menu items
    menu_items = fetch_all("""
        SELECT m.id, r.name, m.item_name, m.price
        FROM menu m
        JOIN restaurants r ON m.restaurant_id = r.id
    """)
    
    if not menu_items:
        print_message("No menu items found")
        time.sleep(1)
        return
    
    print(tabulate(menu_items, headers=["ID", "Restaurant", "Item", "Price"], tablefmt="grid"))
    
    try:
        menu_id = int(input("\nEnter menu item ID to delete: "))
        confirm = input("Are you sure? (y/n): ").strip().lower()
        
        if confirm == "y":
            success = execute_query("DELETE FROM menu WHERE id = %s", (menu_id,))
            if success:
                print_message("Menu item deleted!")
        elif confirm == "n":
            print_message("Cancelled")
        else:
            print_message("Invalid input. Cancelled")
        time.sleep(1)
        
    except ValueError:
        print_message("Please enter a valid menu item ID")
        time.sleep(1.5)

def view_all_users():
    clear_screen()
    print_header("All Users")
    
    users = fetch_all("SELECT id, username, role FROM users")
    if not users:
        print_message("No users found")
    else:
        print(tabulate(users, headers=["ID", "Username", "Role"], tablefmt="grid"))
    
    input("\nPress Enter to continue...")

def user_menu(user_id):
    while True:
        clear_screen()
        print_header("USER MENU")
        print("  [1] View Restaurants")
        print("  [2] Place Order")
        print("  [3] My Orders")
        print("  [4] Logout")
        print("\n" + "-" * 60)
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            view_restaurants()
        elif choice == '2':
            place_order(user_id)
        elif choice == '3':
            view_my_orders(user_id)
        elif choice == '4':
            print_message("Logging out...")
            break
        else:
            print_message("Invalid choice. Please enter 1-4")
            time.sleep(1)

def calculate_delivery(restaurant_location, user_location):
    if restaurant_location == user_location:
        return 0.100, 10
    else:
        return 0.300, 15

def view_restaurants():
    clear_screen()
    print_header("Restaurants")
    
    restaurants = fetch_all("SELECT id, name, location FROM restaurants")
    if not restaurants:
        print_message("No restaurants available")
    else:
        print(tabulate(restaurants, headers=["ID", "Restaurant Name", "Location"], tablefmt="grid"))
    
    input("\nPress Enter to continue...")

def view_menu(restaurant_id):
    clear_screen()
    print_header("Menu")
    
    menu = fetch_all(
        "SELECT id, item_name, price FROM menu WHERE restaurant_id = %s",
        (restaurant_id,)
    )
    
    if not menu:
        print_message("No menu items found for this restaurant")
    else:
        print(tabulate(menu, headers=["Item ID", "Item Name", "Price"], tablefmt="grid"))
    
    input("\nPress Enter to continue...")

def place_order(user_id):
    clear_screen()
    print_header("Place Order")
    
    print("Where are you located?")
    print("  [1] Adliya")
    print("  [2] Manama")
    print("  [3] Muharraq")
    print("  [4] Juffair")
    user_loc_choice = input("Choose your location (1-4): ").strip()
    
    if user_loc_choice == "1":
        user_location = "Adliya"
    elif user_loc_choice == "2":
        user_location = "Manama"
    elif user_loc_choice == "3":
        user_location = "Muharraq"
    elif user_loc_choice == "4":
        user_location = "Juffair"
    else:
        print_message("Invalid location choice")
        time.sleep(1)
        return
    
    clear_screen()
    print_header("Place Order")
    print("Your location: " + user_location + "\n")
    
    restaurants = fetch_all("SELECT id, name, location FROM restaurants")
    if not restaurants:
        print_message("No restaurants available")
        time.sleep(1)
        return
    
    print(tabulate(restaurants, headers=["ID", "Restaurant Name", "Location"], tablefmt="grid"))
    
    try:
        restaurant_id = int(input("\nEnter restaurant ID: "))
        
        rest_data = fetch_all("SELECT location FROM restaurants WHERE id = %s", (restaurant_id,))
        if not rest_data:
            print_message("Restaurant not found")
            time.sleep(1)
            return
        
        restaurant_location = rest_data[0][0]
        
    except ValueError:
        print_message("Invalid restaurant ID")
        time.sleep(1)
        return
    
    clear_screen()
    print_header("Menu")
    
    menu_items = fetch_all(
        "SELECT id, item_name, price FROM menu WHERE restaurant_id = %s",
        (restaurant_id,)
    )
    
    if not menu_items:
        print_message("No menu items found for this restaurant")
        time.sleep(1)
        return
    
    print(tabulate(menu_items, headers=["Item ID", "Item Name", "Price"], tablefmt="grid"))
    
    try:
        menu_id = int(input("\nEnter menu item ID: "))
        quantity = int(input("Enter quantity: "))
        
        if quantity <= 0:
            print_message("Quantity must be greater than 0")
            time.sleep(1)
            return
        
        price_result = fetch_all("SELECT price FROM menu WHERE id = %s", (menu_id,))
        if not price_result:
            print_message("Menu item not found")
            time.sleep(1)
            return
        
        price = float(price_result[0][0])
        item_total = price * quantity
        
        result = calculate_delivery(restaurant_location, user_location)
        delivery_charge = result[0]
        delivery_time = result[1]
        total_price = item_total + delivery_charge
        
        print("\n" + "=" * 50)
        print("ORDER SUMMARY".center(50))
        print("=" * 50)
        print("Item Total:        " + str(item_total) + " BD")
        print("Delivery Charge:   " + str(delivery_charge) + " BD")
        print("Total Amount:      " + str(total_price) + " BD")
        print("Estimated Time:    " + str(delivery_time) + " minutes")
        print("=" * 50)
        
        confirm = input("\nConfirm order? (y/n): ").strip().lower()
        
        if confirm == "y":
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            success = execute_query(
                "INSERT INTO orders (user_id, menu_id, quantity, total_price, delivery_charge, delivery_time, user_location, status, order_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (user_id, menu_id, quantity, total_price, delivery_charge, delivery_time, user_location, "Pending", order_date)
            )
            
            if success:
                message = "Order confirmed! Your food will arrive in " + str(delivery_time) + " minutes."
                print_message(message)
            time.sleep(2)
        elif confirm == "n":
            print_message("Order cancelled")
            time.sleep(1)
        else:
            print_message("Invalid input. Order cancelled")
            time.sleep(1)
        
    except ValueError:
        print_message("Please enter valid numbers")
        time.sleep(1)

def update_delivery_status():
    orders = fetch_all("""
        SELECT id, order_date, delivery_time, status
        FROM orders
        WHERE status = 'Pending'
    """)
    
    if orders:
        current_time = datetime.now()
        for order in orders:
            order_id = order[0]
            order_date = order[1]
            delivery_time = order[2]
            
            # Calculate time elapsed since order was placed
            time_elapsed = (current_time - order_date).total_seconds() / 60  # in minutes
            
            # Only mark as delivered if delivery time has passed
            if time_elapsed >= delivery_time:
                execute_query(
                    "UPDATE orders SET status = 'Delivered' WHERE id = %s",
                    (order_id,)
                )

def view_my_orders(user_id):
    clear_screen()
    print_header("My Orders")
    
    update_delivery_status()
    
    orders = fetch_all("""
        SELECT o.id, m.item_name, o.quantity, o.total_price, o.delivery_charge, o.user_location, o.status, o.order_date
        FROM orders o
        JOIN menu m ON o.menu_id = m.id
        WHERE o.user_id = %s
        ORDER BY o.order_date DESC
    """, (user_id,))
    
    if not orders:
        print_message("You have no orders yet")
    else:
        print(tabulate(orders,
                      headers=["ID", "Item", "Qty", "Total", "Delivery", "Location", "Status", "Date"],
                      tablefmt="grid"))
    
    input("\nPress Enter to continue...")

def main():
    init_db()
    
    while True:
        clear_screen()
        print("\n" + "=" * 60)
        print("|" + "YALLAEAT CLI - FOOD ORDERING SYSTEM".center(58) + "|")
        print("=" * 60)
        print("|" + "Welcome! Please choose an option below".center(58) + "|")
        print("=" * 60 + "\n")
        
        print("  [1] Login")
        print("  [2] Create New Account")
        print("  [3] Exit")
        print("\n" + "-" * 60)
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            user_info = login()
            if user_info:
                user_id, username, role = user_info
                if role == 'admin':
                    admin_menu()
                else:
                    user_menu(user_id)
                    
        elif choice == '2':
            register_user()
            
        elif choice == '3':
            print_message("Thank you for using YallaEat CLI. Goodbye!")
            break
            
        else:
            print_message("Invalid choice. Please enter 1-3")
            time.sleep(1)

main()