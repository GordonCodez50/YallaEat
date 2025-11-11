# YallaEat (Talabat CLI)

A command-line interface (CLI) food ordering system inspired by Talabat, built with Python and MySQL. This application allows users to browse restaurants, place orders, and track deliveries, while administrators can manage restaurants, menu items, and orders.

## Features

### User Features
- 🔐 User account registration and login
- 🍽️ Browse restaurants by location
- 📋 View restaurant menus with prices
- 🛒 Place food orders with delivery tracking
- 📦 View order history and status
- 💰 Automatic delivery charge calculation based on location
- ⏱️ Estimated delivery time display

### Admin Features
- 🏪 Add and manage restaurants
- 📝 Add and delete menu items
- 👀 View all orders across the system
- ✏️ Update order status (Pending, Delivered, Cancelled)
- 👥 View all registered users
- 🔄 Automatic order status updates based on delivery time

## Prerequisites

Before running this application, ensure you have the following installed:

- **Python 3.x** (Python 3.6 or higher recommended)
- **MySQL Server** (version 5.7 or higher)
- **pip** (Python package manager)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/GordonCodez50/YallaEat.git
cd YallaEat
```

### 2. Install Required Python Packages

```bash
pip install mysql-connector-python tabulate
```

The application requires the following Python packages:
- `mysql-connector-python` - For MySQL database connectivity
- `tabulate` - For formatting tables in the CLI

### 3. Configure MySQL Database

Before running the application, configure your MySQL database connection:

1. Open `talabat-cli.py` in a text editor
2. Update the database credentials (lines 7-9):

```python
DB_HOST = 'localhost'      # Your MySQL host
DB_USER = 'root'           # Your MySQL username
DB_PASSWORD = '1234'       # Your MySQL password
```

### 4. Start MySQL Service

Ensure your MySQL service is running:

**Windows:**
```bash
net start MySQL
```

**Linux/Mac:**
```bash
sudo service mysql start
# or
sudo systemctl start mysql
```

## Database Setup

The application automatically creates the required database and tables on first run. It creates:

- **Database:** `talabat_db`
- **Tables:**
  - `users` - Stores user accounts (username, password, role)
  - `restaurants` - Restaurant information (name, location)
  - `menu` - Menu items linked to restaurants
  - `orders` - Order records with delivery details

No manual database setup is required!

## Usage

### Running the Application

```bash
python talabat-cli.py
```

### First Time Setup

1. **Create an Admin Account:**
   - Select option `[2] Create New Account`
   - Enter your name and password
   - Choose `[2] Admin Account`
   - Note your generated username (e.g., `admin-YourName`)

2. **Add Restaurants and Menu Items:**
   - Login with your admin account
   - Add restaurants in different locations
   - Add menu items for each restaurant

3. **Create User Accounts:**
   - Regular users can create accounts by selecting `[2] Create New Account`
   - Choose `[1] User Account`

### User Workflow

1. **Login** with your user credentials
2. **View Restaurants** to see available options
3. **Place Order:**
   - Select your location (Adliya, Manama, Muharraq, or Juffair)
   - Choose a restaurant
   - Select menu items and quantity
   - Review order summary with delivery charges
   - Confirm order
4. **Track Orders** in "My Orders" section

### Admin Workflow

1. **Login** with admin credentials
2. **Manage Restaurants:**
   - Add new restaurants with locations
3. **Manage Menu:**
   - Add menu items to restaurants
   - Delete menu items
4. **Monitor Orders:**
   - View all orders system-wide
   - Update order status manually
   - Orders auto-update to "Delivered" after delivery time

## Locations

The system supports four locations in Bahrain:
- **Adliya**
- **Manama**
- **Muharraq**
- **Juffair**

### Delivery Charges
- Same location (restaurant and user): **0.100 BD** (10 minutes)
- Different location: **0.300 BD** (15 minutes)

## User Roles

### User (Regular Account)
- Username format: `user-<name>`
- Can browse restaurants
- Can place and track orders
- Can view personal order history

### Admin (Administrator Account)
- Username format: `admin-<name>`
- Full system access
- Can manage restaurants and menus
- Can view and update all orders
- Can view all users

## Project Structure

```
YallaEat/
├── talabat-cli.py          # Main application file
├── README.md               # This file
└── functionsexplained.md   # Detailed function documentation
```

## Troubleshooting

### Database Connection Error
- Verify MySQL service is running
- Check database credentials in `talabat-cli.py`
- Ensure MySQL user has proper permissions

### Import Error (Module Not Found)
- Install required packages: `pip install mysql-connector-python tabulate`

### Screen Clearing Issues
- The `clear_screen()` function uses `cls` (Windows command)
- For Linux/Mac, modify line 13 to: `os.system("clear")`

## Future Enhancements

Potential features for future versions:
- Password hashing for security
- Payment integration
- Order rating and reviews
- Restaurant search and filtering
- Multiple item ordering in one transaction
- Order cancellation by users
- Real-time order tracking
- Email/SMS notifications

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available for educational purposes.

## Contact

For questions or support, please open an issue on the GitHub repository.

---

**Note:** This is a learning project demonstrating CLI application development with Python and MySQL. It is not intended for production use without additional security enhancements (password hashing, SQL injection prevention, etc.).
