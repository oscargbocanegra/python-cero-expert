import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime

async def main():
    # Inicializar sistemas
    reservation_system = ReservationSystem()
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()

    # Crear habitaciones
    room_mgmt.add_room(Room(101, "Single", 100))
    room_mgmt.add_room(Room(102, "Double", 150))

    # Agregar clientes
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer_mgmt.add_customer(customer1)

    customer2 = Customer(2, "Bob", "bob@example.com")
    customer_mgmt.add_customer(customer2)

    # Verificar disponibilidad de habitaciones
    if room_mgmt.check_availability(101):
        reservation = Reservation(1, "Alice", 101, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)

        # Procesar pago asincrónicamente
        await process_payment("Alice", 100)

    if room_mgmt.check_availability(102):
        reservation = Reservation(2, "Bob", 102, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)

        # Procesar pago asincrónicamente
        await process_payment("Bob", 150)

if __name__ == "__main__":
    asyncio.run(main())

