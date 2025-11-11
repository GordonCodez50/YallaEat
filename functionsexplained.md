# Functions Explained - Talabat CLI

This document provides detailed explanations of all functions in the `talabat-cli.py` application, organized by category.

## Table of Contents
1. [UI Helper Functions](#ui-helper-functions)
2. [Database Functions](#database-functions)
3. [Authentication Functions](#authentication-functions)
4. [Admin Functions](#admin-functions)
5. [User Functions](#user-functions)
6. [Delivery Functions](#delivery-functions)
7. [Main Function](#main-function)

---

## UI Helper Functions

### `clear_screen()`
**Purpose:** Clears the terminal screen for better user experience

**Parameters:** None

**Returns:** None

**Details:**
- Uses `os.system("cls")` to execute the Windows clear screen command
- Should be modified to `os.system("clear")` for Linux/Mac compatibility
- Called before displaying new menus to keep the interface clean

---

### `print_header(title)`
**Purpose:** Displays a formatted header box with a title

**Parameters:**
- `title` (string): The text to display in the header

**Returns:** None

**Details:**
- Creates a 60-character wide box using `=` and `|` characters
- Centers the title within the box
- Used to create visual separation between different sections
- Example output:
  ```
  ============================================================
  |                      ADMIN MENU                          |
  ============================================================
  ```

---

### `print_message(message)`
**Purpose:** Displays a message with line spacing

**Parameters:**
- `message` (string): The message to display

**Returns:** None

**Details:**
- Adds newline characters before and after the message
- Provides consistent message formatting throughout the application
- Used for success messages, errors, and notifications

---

### `show_loading(message)`
**Purpose:** Creates a loading animation with dots

**Parameters:**
- `message` (string): The base message to display

**Returns:** None

**Details:**
- Displays progressive dots (., .., ..., ... Done!)
- Uses 0.3-second delays between each step
- Creates a visual indication that a process is running
- Currently used only during database initialization

---

## Database Functions

### `init_db()`
**Purpose:** Initializes the database and creates all required tables

**Parameters:** None

**Returns:** None

**Details:**
- Creates the `talabat_db` database if it doesn't exist
- Creates four tables: `users`, `restaurants`, `menu`, and `orders`
- Shows a loading animation during connection
- Handles exceptions and displays appropriate error messages
- Only needs to be run once, but safe to run multiple times (uses `IF NOT EXISTS`)

**Tables Created:**
1. **users**: Stores user credentials and roles
   - `id` (INT, AUTO_INCREMENT, PRIMARY KEY)
   - `username` (VARCHAR(255), UNIQUE)
   - `password` (VARCHAR(255))
   - `role` (VARCHAR(20))

2. **restaurants**: Stores restaurant information
   - `id` (INT, AUTO_INCREMENT, PRIMARY KEY)
   - `name` (VARCHAR(255))
   - `location` (VARCHAR(50))

3. **menu**: Stores menu items for each restaurant
   - `id` (INT, AUTO_INCREMENT, PRIMARY KEY)
   - `restaurant_id` (INT, FOREIGN KEY → restaurants.id)
   - `item_name` (VARCHAR(255))
   - `price` (DECIMAL(10, 2))

4. **orders**: Stores order information
   - `id` (INT, AUTO_INCREMENT, PRIMARY KEY)
   - `user_id` (INT, FOREIGN KEY → users.id)
   - `menu_id` (INT, FOREIGN KEY → menu.id)
   - `quantity` (INT)
   - `total_price` (DECIMAL(10, 2))
   - `delivery_charge` (DECIMAL(10, 3))
   - `delivery_time` (INT)
   - `user_location` (VARCHAR(50))
   - `status` (VARCHAR(20), DEFAULT 'Pending')
   - `order_date` (DATETIME)

---

### `get_db_connection()`
**Purpose:** Creates and returns a database connection

**Parameters:** None

**Returns:** MySQL connection object

**Details:**
- Connects to the `talabat_db` database
- Uses global variables: DB_HOST, DB_USER, DB_PASSWORD
- Called by other database functions to establish connections
- Connection should be closed after use to prevent resource leaks

---

### `execute_query(query, params=None)`
**Purpose:** Executes SQL queries that modify data (INSERT, UPDATE, DELETE)

**Parameters:**
- `query` (string): The SQL query to execute
- `params` (tuple, optional): Parameters for parameterized queries

**Returns:** 
- `True` if successful
- `False` if an error occurs

**Details:**
- Creates a new database connection
- Executes the query with optional parameters (prevents SQL injection)
- Commits the transaction
- Closes cursor and connection
- Handles exceptions by displaying "Error" message
- Used for all data modification operations

**Example Usage:**
```python
execute_query(
    "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
    (username, password, role)
)
```

---

### `fetch_all(query, params=None)`
**Purpose:** Retrieves data from the database

**Parameters:**
- `query` (string): The SQL SELECT query to execute
- `params` (tuple, optional): Parameters for parameterized queries

**Returns:**
- List of tuples containing query results
- `False` if an error occurs

**Details:**
- Creates a database connection
- Executes the query and fetches all results
- Closes cursor and connection
- Returns results as a list of tuples
- Used for all data retrieval operations

**Example Usage:**
```python
users = fetch_all("SELECT id, username, role FROM users")
```

---

## Authentication Functions

### `register_user()`
**Purpose:** Handles new user account creation

**Parameters:** None

**Returns:** None

**Details:**
- Prompts for name and password (validates not empty)
- Offers choice between user and admin account
- Generates username automatically:
  - User accounts: `user-<name>` (spaces removed)
  - Admin accounts: `admin-<name>` (spaces removed)
- Checks if username already exists
- Inserts new user into database
- Displays generated username to user

**Validation:**
- Name cannot be empty
- Password cannot be empty
- Username must be unique

---

### `login()`
**Purpose:** Authenticates users and retrieves their information

**Parameters:** None

**Returns:**
- Tuple of `(user_id, username, role)` if successful
- `None` if login fails

**Details:**
- Prompts for username and password
- Queries database for matching credentials
- Returns user information on successful authentication
- Routes users to appropriate menu based on role
- Uses plain text password comparison (not secure for production)

**Security Note:** Passwords are stored and compared in plain text. For production use, implement password hashing (e.g., bcrypt).

---

## Admin Functions

### `admin_menu()`
**Purpose:** Displays and handles the main admin menu

**Parameters:** None

**Returns:** None

**Details:**
- Loops continuously until user logs out
- Presents 7 options:
  1. Add Restaurant
  2. Add Menu Item
  3. View All Orders
  4. Update Order Status
  5. Delete Menu Item
  6. View All Users
  7. Logout
- Validates input and calls appropriate function
- Clears screen before each menu display

---

### `add_restaurant()`
**Purpose:** Allows admins to add new restaurants

**Parameters:** None

**Returns:** None

**Details:**
- Prompts for restaurant name (validates not empty)
- Presents 4 location choices:
  1. Adliya
  2. Manama
  3. Muharraq
  4. Juffair
- Inserts restaurant into database with selected location
- Displays success message

---

### `add_menu_item()`
**Purpose:** Allows admins to add menu items to restaurants

**Parameters:** None

**Returns:** None

**Details:**
- Displays all existing restaurants in a table
- Returns if no restaurants exist (prompts to add restaurant first)
- Prompts for:
  - Restaurant ID
  - Item name
  - Price
- Validates that price is positive
- Inserts menu item into database
- Links menu item to restaurant via `restaurant_id` foreign key

**Validation:**
- Restaurant ID must be valid integer
- Item name cannot be empty
- Price must be positive number

---

### `view_all_orders()`
**Purpose:** Displays all orders in the system

**Parameters:** None

**Returns:** None

**Details:**
- Calls `update_delivery_status()` first to refresh order statuses
- Joins three tables: orders, users, and menu
- Displays comprehensive order information:
  - Order ID
  - Username
  - Item name
  - Quantity
  - Total price
  - Delivery charge
  - User location
  - Status
  - Order date
- Orders sorted by date (newest first)
- Uses tabulate for formatted table display
- Waits for Enter key before returning to menu

---

### `update_order_status()`
**Purpose:** Allows admins to manually change order status

**Parameters:** None

**Returns:** None

**Details:**
- Updates delivery statuses first
- Displays last 10 orders with current status
- Prompts for order ID
- Offers 3 status options:
  1. Pending
  2. Delivered
  3. Cancelled
- Updates database with new status
- Validates order ID and status choice

---

### `delete_menu_item()`
**Purpose:** Allows admins to remove menu items

**Parameters:** None

**Returns:** None

**Details:**
- Displays all menu items with restaurant information
- Joins menu and restaurants tables
- Prompts for menu item ID
- Requires confirmation (y/n) before deletion
- Deletes item from database if confirmed
- Handles invalid input gracefully

**Note:** Deleting a menu item that has associated orders may cause foreign key constraint issues. Consider adding cascade delete or preventing deletion of items with orders.

---

### `view_all_users()`
**Purpose:** Displays all registered users in the system

**Parameters:** None

**Returns:** None

**Details:**
- Queries all users from database
- Displays user ID, username, and role
- Uses tabulate for formatted output
- Waits for Enter key before returning

---

## User Functions

### `user_menu(user_id)`
**Purpose:** Displays and handles the main user menu

**Parameters:**
- `user_id` (int): The ID of the logged-in user

**Returns:** None

**Details:**
- Loops continuously until user logs out
- Presents 4 options:
  1. View Restaurants
  2. Place Order
  3. My Orders
  4. Logout
- Passes user_id to functions that need it
- Validates input and routes to appropriate function

---

### `view_restaurants()`
**Purpose:** Displays all available restaurants

**Parameters:** None

**Returns:** None

**Details:**
- Queries all restaurants from database
- Displays restaurant ID, name, and location in a table
- Simple read-only view for users to browse options
- Waits for Enter key before returning

---

### `view_menu(restaurant_id)`
**Purpose:** Displays menu items for a specific restaurant

**Parameters:**
- `restaurant_id` (int): The ID of the restaurant

**Returns:** None

**Details:**
- Queries menu items filtered by restaurant_id
- Displays item ID, name, and price
- Currently not used in main flow (users see menu during order placement)
- Could be useful for browsing without ordering

---

### `place_order(user_id)`
**Purpose:** Handles the complete order placement process

**Parameters:**
- `user_id` (int): The ID of the user placing the order

**Returns:** None

**Details:**
This is the most complex user function with multiple steps:

1. **Location Selection:**
   - Prompts user for their location
   - 4 options: Adliya, Manama, Muharraq, Juffair

2. **Restaurant Selection:**
   - Displays all restaurants with their locations
   - User enters restaurant ID
   - Retrieves restaurant location for delivery calculation

3. **Menu Item Selection:**
   - Displays menu items for selected restaurant
   - User enters menu item ID and quantity
   - Validates quantity > 0

4. **Price Calculation:**
   - Retrieves item price from database
   - Calculates item total: `price × quantity`
   - Calculates delivery charge using `calculate_delivery()`
   - Calculates total: `item total + delivery charge`

5. **Order Summary:**
   - Displays formatted summary with:
     - Item total
     - Delivery charge
     - Total amount
     - Estimated delivery time

6. **Confirmation:**
   - Prompts for confirmation (y/n)
   - If confirmed:
     - Records current timestamp
     - Inserts order into database with status "Pending"
     - Displays success message with delivery time
   - If cancelled: aborts order

**Error Handling:**
- Invalid restaurant/menu ID
- Non-numeric input
- Zero or negative quantity

---

### `view_my_orders(user_id)`
**Purpose:** Displays all orders for the logged-in user

**Parameters:**
- `user_id` (int): The ID of the user

**Returns:** None

**Details:**
- Updates delivery statuses first
- Joins orders and menu tables
- Filters orders by user_id
- Displays:
  - Order ID
  - Item name
  - Quantity
  - Total price
  - Delivery charge
  - User location
  - Status
  - Order date
- Orders sorted by date (newest first)
- Shows message if no orders exist
- Waits for Enter key before returning

---

## Delivery Functions

### `calculate_delivery(restaurant_location, user_location)`
**Purpose:** Calculates delivery charge and time based on locations

**Parameters:**
- `restaurant_location` (string): The location of the restaurant
- `user_location` (string): The location of the user

**Returns:** 
- Tuple of `(delivery_charge, delivery_time)`

**Details:**
- Same location: 0.100 BD, 10 minutes
- Different location: 0.300 BD, 15 minutes
- Simple distance-based pricing model
- Uses string comparison (case-sensitive)

**Pricing Logic:**
```python
if restaurant_location == user_location:
    return 0.100, 10  # Same area
else:
    return 0.300, 15  # Different area
```

---

### `update_delivery_status()`
**Purpose:** Automatically updates order status based on delivery time

**Parameters:** None

**Returns:** None

**Details:**
- Queries all orders with "Pending" status
- For each order:
  - Calculates time elapsed since order_date
  - Compares elapsed time with delivery_time
  - Updates status to "Delivered" if delivery time has passed
- Runs silently in the background
- Called before displaying orders to ensure current status

**Time Calculation:**
```python
time_elapsed = (current_time - order_date).total_seconds() / 60  # minutes
if time_elapsed >= delivery_time:
    # Mark as delivered
```

**Note:** This simulates automatic delivery completion. In a real system, this would be handled by delivery personnel or integration with a tracking system.

---

## Main Function

### `main()`
**Purpose:** Entry point of the application; main program loop

**Parameters:** None

**Returns:** None

**Details:**
The main function orchestrates the entire application flow:

1. **Database Initialization:**
   - Calls `init_db()` to ensure database and tables exist

2. **Main Menu Loop:**
   - Displays welcome header with ASCII box design
   - Presents 3 options:
     1. Login
     2. Create New Account
     3. Exit

3. **Login Flow:**
   - Calls `login()` function
   - If successful, routes to appropriate menu based on role:
     - Admin → `admin_menu()`
     - User → `user_menu(user_id)`
   - After logout, returns to main menu

4. **Registration Flow:**
   - Calls `register_user()` function
   - Returns to main menu after completion

5. **Exit:**
   - Displays goodbye message
   - Breaks loop and terminates program

6. **Input Validation:**
   - Validates menu choices (1-3)
   - Displays error for invalid input
   - Loops continuously until user chooses to exit

**Execution:**
The script automatically runs `main()` at the bottom:
```python
main()
```

---

## Function Call Hierarchy

### Startup Flow
```
main()
  └─> init_db()
```

### Admin Flow
```
main()
  └─> login()
      └─> admin_menu()
          ├─> add_restaurant()
          ├─> add_menu_item()
          ├─> view_all_orders()
          │   └─> update_delivery_status()
          ├─> update_order_status()
          │   └─> update_delivery_status()
          ├─> delete_menu_item()
          └─> view_all_users()
```

### User Flow
```
main()
  └─> login()
      └─> user_menu(user_id)
          ├─> view_restaurants()
          ├─> place_order(user_id)
          │   └─> calculate_delivery()
          └─> view_my_orders(user_id)
              └─> update_delivery_status()
```

### Registration Flow
```
main()
  └─> register_user()
```

---

## Database Query Patterns

### Common Patterns Used

1. **Insert with Parameters:**
```python
execute_query(
    "INSERT INTO table (col1, col2) VALUES (%s, %s)",
    (value1, value2)
)
```

2. **Select with Join:**
```python
fetch_all("""
    SELECT o.id, u.username
    FROM orders o
    JOIN users u ON o.user_id = u.id
""")
```

3. **Update with Condition:**
```python
execute_query(
    "UPDATE orders SET status = %s WHERE id = %s",
    (new_status, order_id)
)
```

4. **Delete with Condition:**
```python
execute_query("DELETE FROM menu WHERE id = %s", (menu_id,))
```

---

## Error Handling

The application uses basic error handling:

1. **Database Errors:**
   - Caught in `init_db()`, `execute_query()`, and `fetch_all()`
   - Generic "Error" message displayed
   - Could be improved with specific error messages

2. **Input Validation:**
   - Empty string checks
   - Numeric input validation using try-except with ValueError
   - Positive number validation for prices and quantities

3. **Missing Data:**
   - Checks if queries return empty results
   - Displays appropriate messages (e.g., "No restaurants found")

**Improvements Needed:**
- More specific error messages
- Logging for debugging
- SQL injection prevention (currently uses parameterized queries, which is good)
- Password security (hashing instead of plain text)

---

## Performance Considerations

1. **Database Connections:**
   - New connection created for each query
   - Connections properly closed after use
   - For high-volume applications, consider connection pooling

2. **Query Optimization:**
   - Indexes on foreign keys would improve join performance
   - No pagination implemented (could be slow with many records)

3. **Delivery Status Updates:**
   - Updates all pending orders each time
   - Could be optimized with batch updates or scheduled tasks

---

## Security Considerations

**Current Vulnerabilities:**
1. **Plain Text Passwords:** Passwords stored without hashing
2. **No Input Sanitization:** Beyond parameterized queries
3. **No Session Management:** Simple pass-through of user_id
4. **Database Credentials:** Hard-coded in source file

**Recommended Improvements:**
1. Use bcrypt or similar for password hashing
2. Store database credentials in environment variables
3. Add rate limiting for login attempts
4. Implement proper session management
5. Add input length limits and validation
6. Use HTTPS for any network communication (if extended to web)

---

## Extension Points

The codebase is well-structured for future enhancements:

1. **Multiple Items per Order:**
   - Create an `order_items` junction table
   - Modify `place_order()` to handle multiple items

2. **Order Cancellation:**
   - Add function to update order status to "Cancelled"
   - Add time limit (e.g., can't cancel after 5 minutes)

3. **Reviews and Ratings:**
   - Add `reviews` table
   - Allow users to rate restaurants/items after delivery

4. **Search and Filter:**
   - Add restaurant search by name
   - Filter menu items by price range or category

5. **Admin Dashboard:**
   - Add statistics (total orders, revenue, popular items)
   - Export functionality for reports

---

This documentation covers all functions in the Talabat CLI application. Each function is designed to be modular and focused on a single responsibility, making the codebase maintainable and extensible.
