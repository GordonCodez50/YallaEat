# YallaEat CLI - Food Ordering System

YallaEat is a command-line interface (CLI) based food ordering system built with Python and MySQL. It simulates a food delivery platform where users can browse restaurants, place orders, and track their delivery status.

## Features

### For Users:
- **Account Registration**: Create a user account with username and password
- **Browse Restaurants**: View available restaurants by location (Adliya, Manama, Muharraq, Juffair)
- **View Menus**: Browse menu items and prices for each restaurant
- **Place Orders**: Order food with automatic delivery charge calculation
- **Track Orders**: View order history and real-time delivery status
- **Delivery Time Estimation**: Get estimated delivery times based on location

### For Admins:
- **Restaurant Management**: Add new restaurants and specify locations
- **Menu Management**: Add and delete menu items for restaurants
- **Order Management**: View all orders and update order status
- **User Management**: View all registered users
- **Order Status Updates**: Mark orders as Pending, Delivered, or Cancelled

## Technology Stack

- **Language**: Python 3
- **Database**: MySQL
- **Libraries**: 
  - `mysql-connector-python` - MySQL database connectivity
  - `tabulate` - Beautiful table formatting for CLI output

## Prerequisites

Before running YallaEat CLI, ensure you have the following installed:

1. **Python 3.x** - [Download Python](https://www.python.org/downloads/)
2. **MySQL Server** - [Download MySQL](https://dev.mysql.com/downloads/mysql/)
3. **pip** - Python package installer (usually comes with Python)

## Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone https://github.com/GordonCodez50/YallaEat.git
   cd YallaEat
   ```

2. **Install required Python packages**:
   ```bash
   pip install mysql-connector-python tabulate
   ```

3. **Configure MySQL Database**:
   - Ensure MySQL server is running
   - Update database credentials in `yallaeat-cli.py` if needed:
     ```python
     DB_HOST = 'localhost'
     DB_USER = 'root'
     DB_PASSWORD = '1234'  # Change to your MySQL password
     ```

4. **Run the application**:
   ```bash
   python yallaeat-cli.py
   ```

   The application will automatically create the required database (`talabat_db`) and tables on first run.

## Database Schema

The system uses four main tables:

- **users**: Stores user accounts (username, password, role)
- **restaurants**: Restaurant information (name, location)
- **menu**: Menu items linked to restaurants (item name, price)
- **orders**: Order details (user, menu item, quantity, delivery info, status)

## Features Overview

### Delivery Charge Calculation
- **Same location**: 0.100 BD, 10 minutes delivery
- **Different location**: 0.300 BD, 15 minutes delivery

### Order Status
Orders automatically update from "Pending" to "Delivered" after the estimated delivery time passes.

### Locations Supported
- Adliya
- Manama
- Muharraq
- Juffair

## Project Structure

```
YallaEat/
├── yallaeat-cli.py          # Main application file
├── README.md                # This file
├── Console_Output_Examples.md   # Console output examples
└── HTU.md                   # How to use guide
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please open an issue on the GitHub repository.

## Author

GordonCodez50

---

*YallaEat - Bringing food to your terminal!* 🍕🚀
