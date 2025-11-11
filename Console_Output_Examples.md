# Console Output Examples

This document provides examples of console outputs from the YallaEat CLI application.

## Main Menu

```
============================================================
|        TALABAT CLI - FOOD ORDERING SYSTEM               |
============================================================
|       Welcome! Please choose an option below             |
============================================================

  [1] Login
  [2] Create New Account
  [3] Exit

------------------------------------------------------------
Choose an option (1-3): 
```

## User Registration

```
============================================================
|                Create New Account                       |
============================================================

Enter your name: John Doe
Enter password: ****

[1] User Account

[2] Admin Account
Select account type: 1

Account created! Your username is: user-JohnDoe

```

## Login Screen

```
============================================================
|                       Login                             |
============================================================

Enter username: user-JohnDoe
Enter password: ****

Login successful!

```

## User Menu

```
============================================================
|                     USER MENU                           |
============================================================
  [1] View Restaurants
  [2] Place Order
  [3] My Orders
  [4] Logout

------------------------------------------------------------
Choose an option (1-4): 
```

## View Restaurants

```
============================================================
|                    Restaurants                          |
============================================================

+------+---------------------+-------------+
|   ID | Restaurant Name     | Location    |
+======+=====================+=============+
|    1 | Pizza Palace        | Adliya      |
+------+---------------------+-------------+
|    2 | Burger King         | Manama      |
+------+---------------------+-------------+
|    3 | Sushi House         | Juffair     |
+------+---------------------+-------------+
|    4 | Taco Express        | Muharraq    |
+------+---------------------+-------------+

Press Enter to continue...
```

## Place Order Flow

### Step 1: Select Location

```
============================================================
|                     Place Order                         |
============================================================

Where are you located?
  [1] Adliya
  [2] Manama
  [3] Muharraq
  [4] Juffair
Choose your location (1-4): 1
```

### Step 2: Select Restaurant

```
============================================================
|                     Place Order                         |
============================================================

Your location: Adliya

+------+---------------------+-------------+
|   ID | Restaurant Name     | Location    |
+======+=====================+=============+
|    1 | Pizza Palace        | Adliya      |
+------+---------------------+-------------+
|    2 | Burger King         | Manama      |
+------+---------------------+-------------+

Enter restaurant ID: 1
```

### Step 3: Select Menu Item

```
============================================================
|                        Menu                             |
============================================================

+-----------+-------------------+---------+
|   Item ID | Item Name         |   Price |
+===========+===================+=========+
|         1 | Margherita Pizza  |    5.50 |
+-----------+-------------------+---------+
|         2 | Pepperoni Pizza   |    6.50 |
+-----------+-------------------+---------+
|         3 | Cheese Pizza      |    5.00 |
+-----------+-------------------+---------+

Enter menu item ID: 1
Enter quantity: 2
```

### Step 4: Order Summary

```
==================================================
                  ORDER SUMMARY                   
==================================================
Item Total:        11.0 BD
Delivery Charge:   0.1 BD
Total Amount:      11.1 BD
Estimated Time:    10 minutes
==================================================

Confirm order? (y/n): y

Order confirmed! Your food will arrive in 10 minutes.

```

## View My Orders

```
============================================================
|                     My Orders                           |
============================================================

+------+-------------------+-------+---------+------------+------------+-------------+---------------------+
|   ID | Item              |   Qty |   Total |   Delivery | Location   | Status      | Date                |
+======+===================+=======+=========+============+============+=============+=====================+
|    5 | Margherita Pizza  |     2 |    11.1 |        0.1 | Adliya     | Delivered   | 2025-11-11 14:30:45 |
+------+-------------------+-------+---------+------------+------------+-------------+---------------------+
|    3 | Pepperoni Pizza   |     1 |     6.8 |        0.3 | Manama     | Pending     | 2025-11-11 13:15:22 |
+------+-------------------+-------+---------+------------+------------+-------------+---------------------+
|    1 | Cheese Pizza      |     3 |    15.3 |        0.3 | Juffair    | Delivered   | 2025-11-11 10:00:10 |
+------+-------------------+-------+---------+------------+------------+-------------+---------------------+

Press Enter to continue...
```

## Admin Menu

```
============================================================
|                     ADMIN MENU                          |
============================================================
 [1] Add Restaurant
 [2] Add Menu Item
 [3] View All Orders
 [4] Update Order Status
 [5] Delete Menu Item
 [6] View All Users
 [7] Logout

------------------------------------------------------------
Choose an option (1-7): 
```

## Add Restaurant (Admin)

```
============================================================
|                   Add Restaurant                        |
============================================================

Enter restaurant name: Thai Garden

Select restaurant location:
  [1] Adliya
  [2] Manama
  [3] Muharraq
  [4] Juffair
Choose location (1-4): 2

Restaurant added successfully in Manama!

```

## Add Menu Item (Admin)

```
============================================================
|                   Add Menu Item                         |
============================================================

+------+---------------------+-------------+
|   ID | Restaurant Name     | Location    |
+======+=====================+=============+
|    1 | Pizza Palace        | Adliya      |
+------+---------------------+-------------+
|    2 | Burger King         | Manama      |
+------+---------------------+-------------+

Enter restaurant ID: 1
Enter item name: Hawaiian Pizza
Enter price: 7.50

Menu item added successfully!

```

## View All Orders (Admin)

```
============================================================
|                     All Orders                          |
============================================================

+------+----------------+-------------------+-------+---------+------------+------------+-------------+---------------------+
|   ID | User           | Item              |   Qty |   Total |   Delivery | Location   | Status      | Date                |
+======+================+===================+=======+=========+============+============+=============+=====================+
|    8 | user-JohnDoe   | Margherita Pizza  |     2 |    11.1 |        0.1 | Adliya     | Delivered   | 2025-11-11 14:30:45 |
+------+----------------+-------------------+-------+---------+------------+------------+-------------+---------------------+
|    7 | user-Sarah     | Burger Deluxe     |     1 |     5.5 |        0.3 | Manama     | Pending     | 2025-11-11 13:45:30 |
+------+----------------+-------------------+-------+---------+------------+------------+-------------+---------------------+
|    6 | user-Mike      | Sushi Combo       |     2 |    16.3 |        0.1 | Juffair    | Delivered   | 2025-11-11 12:20:15 |
+------+----------------+-------------------+-------+---------+------------+------------+-------------+---------------------+

Press Enter to continue...
```

## Update Order Status (Admin)

```
============================================================
|                Update Order Status                      |
============================================================

+------------+------------------+
|   Order ID | Current Status   |
+============+==================+
|          8 | Delivered        |
+------------+------------------+
|          7 | Pending          |
+------------+------------------+
|          6 | Delivered        |
+------------+------------------+

Enter order ID: 7

[1] Pending
[2] Delivered
[3] Cancelled
Select new status (1-3): 2

Order status updated!

```

## View All Users (Admin)

```
============================================================
|                     All Users                           |
============================================================

+------+------------------+--------+
|   ID | Username         | Role   |
+======+==================+========+
|    1 | admin-Admin      | admin  |
+------+------------------+--------+
|    2 | user-JohnDoe     | user   |
+------+------------------+--------+
|    3 | user-Sarah       | user   |
+------+------------------+--------+
|    4 | user-Mike        | user   |
+------+------------------+--------+

Press Enter to continue...
```

## Database Connection

```
Connecting to database.
Connecting to database..
Connecting to database...
Connecting to database... Done!

Database initialized successfully

```

## Error Messages

### Invalid Login

```
============================================================
|                       Login                             |
============================================================

Enter username: wronguser
Enter password: ****

Invalid username or password

```

### Empty Input

```
Name cannot be empty

```

### Invalid Choice

```
Invalid choice. Please enter 1-3

```

### Database Error

```
Database error: Access denied for user 'root'@'localhost'

Please check your database settings

```

---

*These examples represent typical interactions with the YallaEat CLI system.*
