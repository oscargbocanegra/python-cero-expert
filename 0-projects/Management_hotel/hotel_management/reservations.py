from collections import defaultdict
from datetime import datetime
from typing import Dict, List


class Reservation:
    def __init__(self, reservation_id: int, customer_name: str, room_number: int, check_in: datetime, check_out: datetime) -> None:
        self.reservation_id: int = reservation_id
        self.customer_name: str = customer_name
        self.room_number: int = room_number
        self.check_in: datetime = check_in
        self.check_out: datetime = check_out

class ReservationSystem:
    def __init__(self) -> None:
        # Utilizamos defaultdict para gestionar las reservas
        self.reservations: Dict[int, List[Reservation]] = defaultdict(list)

    def add_reservation(self, reservation: Reservation) -> None:
        """Agrega una nueva reserva al sistema."""
        self.reservations[reservation.room_number].append(reservation)
        print(f"Reserva creada para {reservation.customer_name} en la habitación {reservation.room_number}")

    def cancel_reservation(self, reservation_id: int) -> None:
        """Cancela una reserva existente por ID."""
        for room, reservations in self.reservations.items():
            for r in reservations:
                if r.reservation_id == reservation_id:
                    reservations.remove(r)
                    print(f"Reserva {reservation_id} cancelada")
                    return
        print("Reserva no encontrada")