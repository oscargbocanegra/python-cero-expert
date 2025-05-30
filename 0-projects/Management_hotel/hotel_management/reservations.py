from collections import defaultdict
from datetime import datetime

class Reservation:
    def __init__(self, reservation_id, customer_name, room_number, check_in, check_out):
        self.reservation_id = reservation_id
        self.customer_name = customer_name
        self.room_number = room_number
        self.check_in = check_in
        self.check_out = check_out

class ReservationSystem:
    def __init__(self):
        # Utilizamos defaultdict para gestionar las reservas
        self.reservations = defaultdict(list)

    def add_reservation(self, reservation):
        """Agrega una nueva reserva al sistema."""
        self.reservations[reservation.room_number].append(reservation)
        print(f"Reserva creada para {reservation.customer_name} en la habitación {reservation.room_number}")

    def cancel_reservation(self, reservation_id):
        """Cancela una reserva existente por ID."""
        for room, reservations in self.reservations.items():
            for r in reservations:
                if r.reservation_id == reservation_id:
                    reservations.remove(r)
                    print(f"Reserva {reservation_id} cancelada")
                    return
        print("Reserva no encontrada")