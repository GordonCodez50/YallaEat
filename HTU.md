# HTU (How To Use) - YallaEat CLI

This guide provides detailed step-by-step instructions on how to use the YallaEat CLI Food Ordering System.

## Table of Contents

1. [Getting Started](#getting-started)
2. [First Time Setup](#first-time-setup)
3. [User Guide](#user-guide)
4. [Admin Guide](#admin-guide)
5. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Prerequisites Check

Before starting, ensure you have:

1. **MySQL Server Running**
   ```bash
   # Check if MySQL is running (Linux/Mac)
   sudo systemctl status mysql
   
   # Check if MySQL is running (Windows)
   # Open Services and look for MySQL
   ```

2. **Python 3 Installed**
   ```bash
   python --version
   # Should show Python 3.x.x
   ```

3. **Required Packages Installed**
   ```bash
   pip install mysql-connector-python tabulate
   ```

### Launch the Application

```bash
cd /path/to/YallaEat
python yallaeat-cli.py
```

On first launch, the application will:
- Connect to MySQL database
- Create the `talabat_db` database automatically
- Create all necessary tables (users, restaurants, menu, orders)

---

## First Time Setup

### Step 1: Create an Admin Account

1. From the main menu, select `[2] Create New Account`
2. Enter your name (e.g., "Admin")
3. Enter a password
4. Select `[2] Admin Account`
5. Note your username (e.g., "admin-Admin")

### Step 2: Create a User Account

1. From the main menu, select `[2] Create New Account`
2. Enter your name (e.g., "John")
3. Enter a password
4. Select `[1] User Account`
5. Note your username (e.g., "user-John")

---

## User Guide

### Logging In as a User

1. From main menu, select `[1] Login`
2. Enter your username (starts with "user-")
3. Enter your password
4. You'll be redirected to the User Menu

### Viewing Restaurants

**Purpose**: Browse available restaurants and their locations

1. From User Menu, select `[1] View Restaurants`
2. You'll see a table with:
   - Restaurant ID
   - Restaurant Name
   - Location (Adliya, Manama, Muharraq, or Juffair)
3. Press Enter to return to User Menu

### Placing an Order

**Purpose**: Order food from a restaurant

1. From User Menu, select `[2] Place Order`

2. **Choose Your Location**:
   - Select from: Adliya [1], Manama [2], Muharraq [3], or Juffair [4]
   - This affects delivery charge and time

3. **Select a Restaurant**:
   - View the list of available restaurants
   - Enter the Restaurant ID number

4. **Choose Menu Item**:
   - View the restaurant's menu with prices
   - Enter the Menu Item ID
   - Enter the quantity you want

5. **Review Order Summary**:
   - Item Total: Price × Quantity
   - Delivery Charge: 
     - 0.100 BD (10 min) if same location
     - 0.300 BD (15 min) if different location
   - Total Amount: Item Total + Delivery Charge
   - Estimated Delivery Time

6. **Confirm Order**:
   - Type `y` to confirm and place order
   - Type `n` to cancel

7. You'll receive confirmation with estimated delivery time

### Viewing Your Orders

**Purpose**: Check order history and delivery status

1. From User Menu, select `[3] My Orders`
2. You'll see a table with all your orders:
   - Order ID
   - Item Name
   - Quantity
   - Total Price
   - Delivery Charge
   - Location
   - **Status**: Pending, Delivered, or Cancelled
   - Order Date and Time
3. Press Enter to return to User Menu

**Note**: Orders automatically update to "Delivered" after the estimated delivery time passes.

### Logging Out

1. From User Menu, select `[4] Logout`
2. You'll return to the main menu

---

## Admin Guide

### Logging In as Admin

1. From main menu, select `[1] Login`
2. Enter your admin username (starts with "admin-")
3. Enter your password
4. You'll be redirected to the Admin Menu

### Adding a Restaurant

**Purpose**: Add new restaurants to the system

1. From Admin Menu, select `[1] Add Restaurant`
2. Enter restaurant name (e.g., "Pizza Palace")
3. Select location:
   - [1] Adliya
   - [2] Manama
   - [3] Muharraq
   - [4] Juffair
4. Confirm success message
5. Restaurant is now available for users

### Adding Menu Items

**Purpose**: Add food items to restaurant menus

1. From Admin Menu, select `[2] Add Menu Item`
2. View the list of existing restaurants
3. Enter the Restaurant ID
4. Enter the item name (e.g., "Margherita Pizza")
5. Enter the price (e.g., 5.50)
6. Confirm success message
7. Menu item is now available for ordering

**Best Practices**:
- Add multiple items to give users variety
- Use clear, descriptive names
- Set reasonable prices

### Viewing All Orders

**Purpose**: Monitor all orders in the system

1. From Admin Menu, select `[3] View All Orders`
2. You'll see a comprehensive table with:
   - Order ID
   - Username (who ordered)
   - Item Name
   - Quantity
   - Total Price
   - Delivery Charge
   - User Location
   - Status
   - Order Date/Time
3. Orders are sorted by most recent first
4. Press Enter to return to Admin Menu

### Updating Order Status

**Purpose**: Manually change order status

1. From Admin Menu, select `[4] Update Order Status`
2. View the list of recent orders
3. Enter the Order ID you want to update
4. Select new status:
   - [1] Pending
   - [2] Delivered
   - [3] Cancelled
5. Confirm success message

**Use Cases**:
- Mark order as Cancelled if customer requested cancellation
- Manually mark as Delivered if needed
- Reset to Pending if there was an error

### Deleting Menu Items

**Purpose**: Remove items from restaurant menus

1. From Admin Menu, select `[5] Delete Menu Item`
2. View all menu items across all restaurants
3. Enter the Menu Item ID to delete
4. Confirm deletion:
   - Type `y` to delete
   - Type `n` to cancel
5. Menu item is permanently removed

**Warning**: This action cannot be undone!

### Viewing All Users

**Purpose**: See all registered users in the system

1. From Admin Menu, select `[6] View All Users`
2. You'll see a table with:
   - User ID
   - Username
   - Role (admin or user)
3. Press Enter to return to Admin Menu

### Logging Out

1. From Admin Menu, select `[7] Logout`
2. You'll return to the main menu

---

## Troubleshooting

### Database Connection Issues

**Problem**: "Database error: Access denied"

**Solutions**:
1. Check MySQL is running
2. Verify credentials in `yallaeat-cli.py`:
   ```python
   DB_HOST = 'localhost'
   DB_USER = 'root'
   DB_PASSWORD = '1234'  # Update with your password
   ```
3. Ensure MySQL user has proper permissions

### Username Already Exists

**Problem**: "Username already exists"

**Solutions**:
1. Choose a different name
2. Username format is: `user-YourName` or `admin-YourName`
3. Names are case-sensitive

### No Restaurants Available

**Problem**: Can't place order, no restaurants shown

**Solutions**:
1. Ask admin to add restaurants
2. If you're admin, use `[1] Add Restaurant`

### No Menu Items Found

**Problem**: Restaurant has no menu items

**Solutions**:
1. Ask admin to add menu items for that restaurant
2. If you're admin, use `[2] Add Menu Item`

### Invalid Input Errors

**Problem**: "Invalid choice" or "Please enter valid numbers"

**Solutions**:
1. Ensure you're entering numbers only (not letters)
2. Enter choices within the valid range
3. Don't include spaces or special characters

### Order Status Not Updating

**Problem**: Order still shows "Pending" after delivery time

**Solutions**:
1. Status updates automatically when viewing orders
2. Refresh by going to "My Orders" again
3. Admin can manually update using `[4] Update Order Status`

---

## Tips and Best Practices

### For Users:
- Choose restaurants in the same location to save on delivery charges (0.100 BD vs 0.300 BD)
- Check your orders regularly to see when they're delivered
- Note your username after registration - you'll need it to login

### For Admins:
- Add restaurants before adding menu items
- Create a variety of menu items for each restaurant
- Monitor orders regularly
- Keep menu prices reasonable and consistent

### General Tips:
- The application clears the screen between operations for better readability
- All monetary values are in BD (Bahraini Dinar)
- Order dates use 24-hour format
- You can have multiple admin and user accounts

---

## Quick Reference

### Main Menu Options
| Option | Action |
|--------|--------|
| 1 | Login |
| 2 | Create New Account |
| 3 | Exit Application |

### User Menu Options
| Option | Action |
|--------|--------|
| 1 | View Restaurants |
| 2 | Place Order |
| 3 | My Orders |
| 4 | Logout |

### Admin Menu Options
| Option | Action |
|--------|--------|
| 1 | Add Restaurant |
| 2 | Add Menu Item |
| 3 | View All Orders |
| 4 | Update Order Status |
| 5 | Delete Menu Item |
| 6 | View All Users |
| 7 | Logout |

### Delivery Charges
| Scenario | Charge | Time |
|----------|--------|------|
| Same Location | 0.100 BD | 10 minutes |
| Different Location | 0.300 BD | 15 minutes |

### Available Locations
- Adliya
- Manama
- Muharraq
- Juffair

---

## Support

If you encounter issues not covered in this guide:
1. Check the `Console_Output_Examples.md` for expected output
2. Review the `README.md` for technical details
3. Open an issue on the GitHub repository

---

*Happy Ordering with YallaEat CLI!* 🍕🚀
