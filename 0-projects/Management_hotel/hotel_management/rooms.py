from typing import Dict, Optional


class Room:
    def __init__(self, room_number: int, room_type: str, price: float) -> None:
        self.room_number: int = room_number
        self.room_type: str = room_type
        self.price: float = price
        self.available: bool = True

class RoomManagement:
    def __init__(self) -> None:
        self.rooms: Dict[int, Room] = {}

    def add_room(self, room: Room) -> None:
        """Agrega una nueva habitación al sistema."""
        self.rooms[room.room_number] = room
        print(f"Habitación {room.room_number} agregada.")

    def check_availability(self, room_number: int) -> bool:
        """Verifica si una habitación está disponible."""
        room: Optional[Room] = self.rooms.get(room_number)
        if room and room.available:
            print(f"Habitación {room_number} está disponible.")
            return True
        print(f"Habitación {room_number} no está disponible.")
        return False

