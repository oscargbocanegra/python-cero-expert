from typing import Dict, Union


class Customer:
    def __init__(self, customer_id: int, name: str, email: str) -> None:
        self.customer_id: int = customer_id
        self.name: str = name
        self.email: str = email

class CustomerManagement:
    def __init__(self) -> None:
        self.customers: Dict[int, Customer] = {}

    def add_customer(self, customer: Customer) -> None:
        """Agrega un nuevo cliente al sistema."""
        self.customers[customer.customer_id] = customer
        print(f"Cliente {customer.name} agregado.")

    def get_customer(self, customer_id: int) -> Union[Customer, str]:
        """Obtiene la información de un cliente por ID."""
        return self.customers.get(customer_id, "Cliente no encontrado.")

