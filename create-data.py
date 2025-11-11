import mysql.connector
import time
import subprocess
import sys

# List of required packages
required_packages = ["mysql-connector-python", "tabulate"]

# Function to install a package via pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try importing packages, install if missing
for package in required_packages:
    try:
        __import__(package.split("-")[0])  # mysql-connector-python -> mysql
    except ImportError:
        print(f"Package '{package}' not found. Installing...")
        install_package(package)

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '1234'

# Loading animation
def show_loading(message):
    print(message + ".")

# Message box
def print_message(message):
    print("\n" + message + "\n")

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
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id) ON DELETE CASCADE
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
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
            FOREIGN KEY (menu_id) REFERENCES menu(id) ON DELETE SET NULL
        )
    """)

    print_message("Database and tables created successfully!")

    # Preset restaurants (ordered — IDs will be 1..N)
    restaurants = [
        ("Papa John's", "Adliya"),
        ("KFC", "Manama"),
        ("McDonald's", "Muharraq"),
        ("Burger King", "Juffair"),
        ("Subway", "Adliya"),
        ("Pizza Hut", "Seef"),
        ("Lebanese Restaurant", "Adliya"),
        ("Indian Delights", "Manama"),
        ("Apple Restaurant", "Juffair"),
        ("Tim Hortons", "Seef"),
        ("Costa Coffee", "Manama"),
        ("Starbucks", "Seef"),
        ("Domino's", "Muharraq")
    ]

    # Only insert restaurants if table is empty (prevents duplicates)
    cursor.execute("SELECT COUNT(*) FROM restaurants")
    rest_count = cursor.fetchone()[0]
    if rest_count == 0:
        show_loading("Adding restaurants")
        cursor.executemany(
            "INSERT INTO restaurants (name, location) VALUES (%s, %s)",
            restaurants
        )
        conn.commit()
        print_message(f"{len(restaurants)} restaurants added!")
    else:
        print_message(f"Restaurants table already has {rest_count} entries — skipping insert.")

    # Preset menu items (restaurant_id, item_name, price in BHD)
    menu_items = [
        # Papa John's (ID: 1)
        (1, "Medium Pepperoni Pizza", 2.50),
        (1, "Large Supreme Pizza", 3.50),
        (1, "Margherita Pizza (Medium)", 2.00),
        (1, "BBQ Chicken Pizza (Medium)", 3.00),
        (1, "Stuffed Cheesy Bread", 1.00),
        (1, "Garlic Bread", 0.60),
        (1, "Chicken Wings (6pcs)", 1.20),
        (1, "Garden Salad", 0.90),
        (1, "Soft Drink (Can)", 0.30),
        (1, "Chocolate Brownie", 0.60),

        # KFC (ID: 2)
        (2, "Zinger Burger", 1.00),
        (2, "Original Recipe Bucket (8pcs)", 3.00),
        (2, "Hot Wings (6pcs)", 1.20),
        (2, "Popcorn Chicken (Small)", 0.80),
        (2, "Twister Wrap", 0.90),
        (2, "Mashed Potatoes (Side)", 0.40),
        (2, "Coleslaw (Side)", 0.35),
        (2, "Chicken Tenders (3pcs)", 0.95),
        (2, "Buttermilk Biscuit", 0.25),
        (2, "Soft Drink (Can)", 0.25),

        # McDonald's (ID: 3)
        (3, "Big Mac", 1.00),
        (3, "McChicken", 0.80),
        (3, "Cheeseburger", 0.50),
        (3, "Quarter Pounder", 1.30),
        (3, "Filet-O-Fish", 1.10),
        (3, "Large Fries", 0.50),
        (3, "6pc Nuggets", 0.70),
        (3, "McFlurry", 0.60),
        (3, "Apple Pie", 0.35),
        (3, "Filter Coffee", 0.30),

        # Burger King (ID: 4)
        (4, "Whopper", 1.20),
        (4, "Chicken Royale", 1.00),
        (4, "BK Double", 1.60),
        (4, "Large Fries", 0.45),
        (4, "Onion Rings", 0.50),
        (4, "Chicken Nuggets", 0.80),
        (4, "King Shake (Chocolate)", 0.90),
        (4, "Fish Burger", 0.95),
        (4, "Garden Salad", 0.70),
        (4, "Pancakes (2pc)", 0.65),

        # Subway (ID: 5)
        (5, "Footlong Italian BMT", 1.20),
        (5, "Footlong Chicken Teriyaki", 1.20),
        (5, "6\" Veggie Delite", 0.70),
        (5, "6\" Turkey Breast", 0.90),
        (5, "Club Sandwich", 1.30),
        (5, "Meatball Marinara", 1.10),
        (5, "Cookies (3pcs)", 0.30),
        (5, "Chips (Bag)", 0.20),
        (5, "Bottle Drink (500ml)", 0.35),
        (5, "Oven Baked Fries", 0.40),

        # Pizza Hut (ID: 6)
        (6, "Personal Margherita", 1.50),
        (6, "Medium Supreme", 3.20),
        (6, "Large Pepperoni", 3.80),
        (6, "Family Cheesy Bites", 4.50),
        (6, "Chicken Lovers", 3.30),
        (6, "Veggie Feast", 2.80),
        (6, "Garlic Bread", 0.70),
        (6, "Breadsticks", 0.70),
        (6, "Chocolate Lava Cake", 0.90),
        (6, "Soft Drink (2L)", 0.90),

        # Lebanese Restaurant (ID: 7)
        (7, "Mixed Grill Platter", 3.50),
        (7, "Shawarma Plate (Chicken)", 1.20),
        (7, "Falafel Plate", 0.80),
        (7, "Hummus (Large)", 0.50),
        (7, "Tabbouleh Salad", 0.60),
        (7, "Fattoush Salad", 0.60),
        (7, "Kibbeh (3pcs)", 1.10),
        (7, "Manakish Zaatar", 0.40),
        (7, "Grilled Halloumi", 1.00),
        (7, "Lebanese Sweets Plate", 1.00),

        # Indian Delights (ID: 8)
        (8, "Chicken Biryani", 1.20),
        (8, "Butter Chicken (Medium)", 1.50),
        (8, "Paneer Makhani", 1.30),
        (8, "Lamb Curry (Medium)", 2.20),
        (8, "Garlic Naan", 0.20),
        (8, "Samosa (2pcs)", 0.30),
        (8, "Vegetable Pulao", 1.00),
        (8, "Tandoori Chicken (Half)", 2.00),
        (8, "Masala Dosa", 0.90),
        (8, "Gulab Jamun (2pcs)", 0.25),

        # Apple Restaurant (ID: 9)
        (9, "Grilled Chicken Salad", 1.00),
        (9, "Signature Apple Pie", 0.40),
        (9, "Beef Steak (200g)", 3.50),
        (9, "Seafood Platter (For 1)", 4.00),
        (9, "Club Sandwich", 1.20),
        (9, "Fish & Chips", 1.80),
        (9, "Caesar Salad", 0.90),
        (9, "Veggie Pasta", 1.30),
        (9, "Fruit Smoothie (300ml)", 0.70),
        (9, "Fresh Juice (Orange)", 0.40),

        # Tim Hortons (ID: 10)
        (10, "Original Blend Coffee (Small)", 0.30),
        (10, "Iced Capp (Regular)", 0.80),
        (10, "Timbits (6pcs)", 0.50),
        (10, "Breakfast Sandwich", 0.90),
        (10, "Classic Donut", 0.25),
        (10, "Bagel with Cream Cheese", 0.40),
        (10, "Hot Chocolate", 0.35),
        (10, "Wrap (Chicken)", 0.85),
        (10, "Muffin (Blueberry)", 0.45),
        (10, "Tea (Small)", 0.25),

        # Costa Coffee (ID: 11)
        (11, "Flat White", 0.45),
        (11, "Cappuccino", 0.45),
        (11, "Latte", 0.45),
        (11, "Americano", 0.35),
        (11, "Mocha", 0.55),
        (11, "Butter Croissant", 0.40),
        (11, "Panini (Ham & Cheese)", 0.90),
        (11, "Cake Slice", 0.70),
        (11, "Iced Latte", 0.60),
        (11, "Bottled Water (500ml)", 0.20),

        # Starbucks (ID: 12)
        (12, "Caffè Americano", 0.45),
        (12, "Caffè Latte", 0.55),
        (12, "Cappuccino", 0.55),
        (12, "Caramel Macchiato", 0.70),
        (12, "Frappuccino (Regular)", 0.90),
        (12, "Seasonal Special", 0.90),
        (12, "Blueberry Muffin", 0.45),
        (12, "Chicken Panini", 0.95),
        (12, "Protein Box", 1.80),
        (12, "Cold Brew (Bottle)", 0.80),

        # Domino's (ID: 13)
        (13, "Margherita (Medium)", 1.40),
        (13, "Pepperoni Feast (Large)", 3.50),
        (13, "Veggie Supreme (Medium)", 2.80),
        (13, "Chicken BBQ (Large)", 3.20),
        (13, "Cheese Burst (Family)", 4.00),
        (13, "Garlic Bread", 0.60),
        (13, "Cheesy Dip", 0.20),
        (13, "Chicken Strips (5pcs)", 1.20),
        (13, "Potato Wedges", 0.70),
        (13, "Choco Lava Cake", 0.90)
    ]

    # Only insert menu items if table is empty
    cursor.execute("SELECT COUNT(*) FROM menu")
    menu_count = cursor.fetchone()[0]
    if menu_count == 0:
        show_loading("Adding menu items")
        cursor.executemany(
            "INSERT INTO menu (restaurant_id, item_name, price) VALUES (%s, %s, %s)",
            menu_items
        )
        conn.commit()
        print_message(f"{len(menu_items)} menu items added!")
    else:
        print_message(f"Menu table already has {menu_count} entries — skipping insert.")

    cursor.close()
    conn.close()

    print("="*60)
    print("DATABASE SETUP COMPLETE!".center(60))
    print("="*60)
    print(f"Total Restaurants: {len(restaurants)}")
    print(f"Total Menu Items: {len(menu_items)}")
    print("\nYou can now run yallaeat-cli.py to start the application.")
    print("="*60)

except Exception as e:
    print_message(f"Database error: {str(e)}")
    print_message("Please check your database settings")
