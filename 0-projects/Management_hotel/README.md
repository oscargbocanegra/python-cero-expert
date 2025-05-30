# Hotel Management System

A comprehensive hotel management system built with Python, featuring asynchronous payment processing and modular architecture for managing customers, rooms, reservations, and payments.

## 🏨 Features

- **Customer Management**: Add and retrieve customer information
- **Room Management**: Manage hotel rooms with availability tracking
- **Reservation System**: Handle room reservations with check-in/check-out dates
- **Asynchronous Payment Processing**: Process payments with simulated async operations
- **Modular Architecture**: Clean separation of concerns with dedicated modules

## 📁 Project Structure

```
Management_hotel/
├── README.md
├── main.py                    # Main application entry point
└── hotel_management/          # Core hotel management package
    ├── __init__.py
    ├── customers.py           # Customer and CustomerManagement classes
    ├── rooms.py              # Room and RoomManagement classes
    ├── reservations.py       # Reservation and ReservationSystem classes
    └── payments.py           # Asynchronous payment processing
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher (required for asyncio support)

### Installation

1. Clone the repository or download the project files
2. Navigate to the project directory:
   ```bash
   cd Management_hotel
   ```

### Running the Application

Execute the main application:

```bash
python main.py
```

## 📋 Module Overview

### 1. Customer Management (`customers.py`)

- **Customer Class**: Represents a hotel customer with ID, name, and email
- **CustomerManagement Class**: Manages customer operations
  - `add_customer(customer)`: Add a new customer to the system
  - `get_customer(customer_id)`: Retrieve customer information by ID

### 2. Room Management (`rooms.py`)

- **Room Class**: Represents a hotel room with number, type, price, and availability
- **RoomManagement Class**: Handles room operations
  - `add_room(room)`: Add a new room to the hotel inventory
  - `check_availability(room_number)`: Check if a room is available for booking

### 3. Reservation System (`reservations.py`)

- **Reservation Class**: Represents a booking with customer details and dates
- **ReservationSystem Class**: Manages reservation operations using `defaultdict`
  - `add_reservation(reservation)`: Create a new reservation
  - `cancel_reservation(reservation_id)`: Cancel an existing reservation

### 4. Payment Processing (`payments.py`)

- **Asynchronous Payment Function**: `process_payment(customer_name, amount)`
  - Simulates real-world payment processing with random delay
  - Returns payment completion status


## 🔧 Technical Details

### Key Technologies Used

- **Python 3.7+**: Core programming language
- **asyncio**: Asynchronous programming for payment processing
- **collections.defaultdict**: Efficient data structure for managing reservations
- **datetime**: Date and time handling for reservations

### Design Patterns

- **Modular Architecture**: Each functionality is separated into dedicated modules
- **Class-based Design**: Object-oriented approach for better code organization
- **Asynchronous Processing**: Non-blocking payment operations
