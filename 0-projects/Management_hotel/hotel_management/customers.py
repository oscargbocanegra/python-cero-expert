class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        """Agrega un nuevo cliente al sistema."""
        self.customers[customer.customer_id] = customer
        print(f"Cliente {customer.name} agregado.")

    def get_customer(self, customer_id):
        """Obtiene la información de un cliente por ID."""
        return self.customers.get(customer_id, "Cliente no encontrado.")

