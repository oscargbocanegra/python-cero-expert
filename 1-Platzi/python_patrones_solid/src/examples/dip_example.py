"""
Dependency Inversion Principle (DIP) Examples

"High-level modules should not depend on low-level modules. 
Both should depend on abstractions. Abstractions should not depend on details. 
Details should depend on abstractions."

DIP promotes loose coupling by ensuring that high-level business logic
doesn't depend directly on low-level implementation details.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


# ========================================
# ❌ VIOLATES Dependency Inversion Principle
# ========================================

class MySQLDatabase:
    """❌ Low-level module - concrete database implementation."""
    
    def connect(self) -> None:
        print("Connecting to MySQL database")
    
    def execute_query(self, query: str) -> List[Dict]:
        print(f"Executing MySQL query: {query}")
        return [{"id": 1, "name": "John", "email": "john@example.com"}]
    
    def close(self) -> None:
        print("Closing MySQL connection")


class EmailService:
    """❌ Low-level module - concrete email implementation."""
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        print(f"Sending email via SMTP to {to}")
        print(f"Subject: {subject}")
        return True


class UserServiceViolatesDIP:
    """
    ❌ High-level module that violates DIP by depending directly 
    on low-level modules (concrete implementations).
    """
    
    def __init__(self):
        # ❌ Direct dependency on concrete classes
        self.database = MySQLDatabase()
        self.email_service = EmailService()
    
    def create_user(self, name: str, email: str) -> bool:
        """Create a new user - tightly coupled to MySQL and SMTP."""
        try:
            self.database.connect()
            
            # ❌ Directly using MySQL-specific implementation
            query = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')"
            result = self.database.execute_query(query)
            
            if result:
                # ❌ Directly using SMTP email service
                self.email_service.send_email(
                    email, 
                    "Welcome!", 
                    f"Welcome {name}!"
                )
                
                self.database.close()
                return True
            
            self.database.close()
            return False
            
        except Exception as e:
            print(f"Error creating user: {e}")
            return False


# ========================================
# ✅ FOLLOWS Dependency Inversion Principle
# ========================================

# ✅ Abstractions (interfaces) that both high and low-level modules depend on
class DatabaseRepository(ABC):
    """✅ Abstraction for database operations."""
    
    @abstractmethod
    def connect(self) -> None:
        pass
    
    @abstractmethod
    def save_user(self, name: str, email: str) -> bool:
        pass
    
    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        pass
    
    @abstractmethod
    def close(self) -> None:
        pass


class NotificationService(ABC):
    """✅ Abstraction for notification services."""
    
    @abstractmethod
    def send_notification(self, recipient: str, subject: str, message: str) -> bool:
        pass


# ✅ Low-level modules that depend on abstractions
class MySQLRepository(DatabaseRepository):
    """✅ MySQL implementation that depends on DatabaseRepository abstraction."""
    
    def connect(self) -> None:
        print("Connecting to MySQL database")
    
    def save_user(self, name: str, email: str) -> bool:
        print(f"Saving user to MySQL: {name} ({email})")
        # Simulate database save
        return True
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        print(f"Querying MySQL for user: {email}")
        return {"id": 1, "name": "John", "email": email}
    
    def close(self) -> None:
        print("Closing MySQL connection")


class PostgreSQLRepository(DatabaseRepository):
    """✅ PostgreSQL implementation - easily swappable."""
    
    def connect(self) -> None:
        print("Connecting to PostgreSQL database")
    
    def save_user(self, name: str, email: str) -> bool:
        print(f"Saving user to PostgreSQL: {name} ({email})")
        return True
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        print(f"Querying PostgreSQL for user: {email}")
        return {"id": 1, "name": "John", "email": email}
    
    def close(self) -> None:
        print("Closing PostgreSQL connection")


class MongoDBRepository(DatabaseRepository):
    """✅ MongoDB implementation - different database type, same interface."""
    
    def connect(self) -> None:
        print("Connecting to MongoDB")
    
    def save_user(self, name: str, email: str) -> bool:
        print(f"Saving user to MongoDB: {name} ({email})")
        return True
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        print(f"Querying MongoDB for user: {email}")
        return {"_id": "507f1f77bcf86cd799439011", "name": "John", "email": email}
    
    def close(self) -> None:
        print("Closing MongoDB connection")


class SMTPNotificationService(NotificationService):
    """✅ SMTP email implementation."""
    
    def send_notification(self, recipient: str, subject: str, message: str) -> bool:
        print(f"Sending email via SMTP to {recipient}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        return True


class SlackNotificationService(NotificationService):
    """✅ Slack notification implementation."""
    
    def send_notification(self, recipient: str, subject: str, message: str) -> bool:
        print(f"Sending Slack message to {recipient}")
        print(f"Title: {subject}")
        print(f"Message: {message}")
        return True


class SMSNotificationService(NotificationService):
    """✅ SMS notification implementation."""
    
    def send_notification(self, recipient: str, subject: str, message: str) -> bool:
        print(f"Sending SMS to {recipient}")
        print(f"Message: {subject} - {message}")
        return True


# ✅ High-level module that depends on abstractions
class UserService:
    """
    ✅ High-level module that follows DIP by depending on abstractions.
    Can work with any database and notification service implementation.
    """
    
    def __init__(self, database: DatabaseRepository, notifier: NotificationService):
        # ✅ Depends on abstractions, not concrete implementations
        self.database = database
        self.notifier = notifier
    
    def create_user(self, name: str, email: str) -> bool:
        """Create a new user using injected dependencies."""
        try:
            self.database.connect()
            
            # Check if user already exists
            existing_user = self.database.get_user_by_email(email)
            if existing_user:
                print(f"User with email {email} already exists")
                self.database.close()
                return False
            
            # Save new user
            success = self.database.save_user(name, email)
            
            if success:
                # Send welcome notification
                self.notifier.send_notification(
                    email,
                    "Welcome to our platform!",
                    f"Hello {name}, welcome to our platform!"
                )
                
                print(f"User {name} created successfully")
                self.database.close()
                return True
            
            self.database.close()
            return False
            
        except Exception as e:
            print(f"Error creating user: {e}")
            return False


# ========================================
# ADVANCED DIP EXAMPLE: Payment Processing
# ========================================

class PaymentGateway(ABC):
    """✅ Abstraction for payment processing."""
    
    @abstractmethod
    def process_payment(self, amount: float, payment_details: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        pass


class Logger(ABC):
    """✅ Abstraction for logging."""
    
    @abstractmethod
    def log_info(self, message: str) -> None:
        pass
    
    @abstractmethod
    def log_error(self, message: str) -> None:
        pass


class StripePaymentGateway(PaymentGateway):
    """✅ Stripe implementation."""
    
    def process_payment(self, amount: float, payment_details: Dict[str, Any]) -> Dict[str, Any]:
        print(f"Processing ${amount} payment via Stripe")
        return {
            "success": True,
            "transaction_id": f"stripe_txn_{amount}",
            "gateway": "stripe"
        }
    
    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        print(f"Refunding ${amount} via Stripe for transaction {transaction_id}")
        return {"success": True, "refund_id": f"stripe_ref_{transaction_id}"}


class PayPalPaymentGateway(PaymentGateway):
    """✅ PayPal implementation."""
    
    def process_payment(self, amount: float, payment_details: Dict[str, Any]) -> Dict[str, Any]:
        print(f"Processing ${amount} payment via PayPal")
        return {
            "success": True,
            "transaction_id": f"paypal_txn_{amount}",
            "gateway": "paypal"
        }
    
    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        print(f"Refunding ${amount} via PayPal for transaction {transaction_id}")
        return {"success": True, "refund_id": f"paypal_ref_{transaction_id}"}


class FileLogger(Logger):
    """✅ File-based logging implementation."""
    
    def log_info(self, message: str) -> None:
        print(f"[FILE LOG - INFO] {message}")
    
    def log_error(self, message: str) -> None:
        print(f"[FILE LOG - ERROR] {message}")


class DatabaseLogger(Logger):
    """✅ Database-based logging implementation."""
    
    def log_info(self, message: str) -> None:
        print(f"[DB LOG - INFO] {message}")
    
    def log_error(self, message: str) -> None:
        print(f"[DB LOG - ERROR] {message}")


class PaymentProcessor:
    """
    ✅ High-level payment processing logic that depends on abstractions.
    Can work with any payment gateway and logging implementation.
    """
    
    def __init__(self, gateway: PaymentGateway, logger: Logger):
        self.gateway = gateway
        self.logger = logger
    
    def process_order_payment(self, order_id: str, amount: float, 
                            payment_details: Dict[str, Any]) -> bool:
        """Process payment for an order."""
        try:
            self.logger.log_info(f"Processing payment for order {order_id}: ${amount}")
            
            result = self.gateway.process_payment(amount, payment_details)
            
            if result.get("success"):
                self.logger.log_info(
                    f"Payment successful for order {order_id}. "
                    f"Transaction ID: {result.get('transaction_id')}"
                )
                return True
            else:
                self.logger.log_error(f"Payment failed for order {order_id}")
                return False
                
        except Exception as e:
            self.logger.log_error(f"Payment processing error for order {order_id}: {str(e)}")
            return False
    
    def refund_order(self, order_id: str, transaction_id: str, amount: float) -> bool:
        """Refund payment for an order."""
        try:
            self.logger.log_info(f"Processing refund for order {order_id}: ${amount}")
            
            result = self.gateway.refund_payment(transaction_id, amount)
            
            if result.get("success"):
                self.logger.log_info(
                    f"Refund successful for order {order_id}. "
                    f"Refund ID: {result.get('refund_id')}"
                )
                return True
            else:
                self.logger.log_error(f"Refund failed for order {order_id}")
                return False
                
        except Exception as e:
            self.logger.log_error(f"Refund processing error for order {order_id}: {str(e)}")
            return False


def demonstrate_dip():
    """Demonstrate the Dependency Inversion Principle."""
    
    print("=== DIP Violation Example ===")
    # ❌ Tightly coupled to specific implementations
    user_service_bad = UserServiceViolatesDIP()
    user_service_bad.create_user("John Doe", "john@example.com")
    
    print("\n=== DIP Compliance Example ===")
    
    # ✅ Loose coupling through dependency injection
    print("--- Using MySQL + SMTP ---")
    mysql_db = MySQLRepository()
    smtp_notifier = SMTPNotificationService()
    user_service = UserService(mysql_db, smtp_notifier)
    user_service.create_user("Alice Smith", "alice@example.com")
    
    print("\n--- Using PostgreSQL + Slack ---")
    postgres_db = PostgreSQLRepository()
    slack_notifier = SlackNotificationService()
    user_service = UserService(postgres_db, slack_notifier)
    user_service.create_user("Bob Johnson", "bob@example.com")
    
    print("\n--- Using MongoDB + SMS ---")
    mongo_db = MongoDBRepository()
    sms_notifier = SMSNotificationService()
    user_service = UserService(mongo_db, sms_notifier)
    user_service.create_user("Carol Davis", "carol@example.com")
    
    print("\n=== Payment Processing DIP Example ===")
    
    # ✅ Different combinations of payment gateways and loggers
    print("--- Stripe + File Logging ---")
    stripe_gateway = StripePaymentGateway()
    file_logger = FileLogger()
    payment_processor = PaymentProcessor(stripe_gateway, file_logger)
    payment_processor.process_order_payment("ORDER-001", 99.99, {"card": "4111111111111111"})
    
    print("\n--- PayPal + Database Logging ---")
    paypal_gateway = PayPalPaymentGateway()
    db_logger = DatabaseLogger()
    payment_processor = PaymentProcessor(paypal_gateway, db_logger)
    payment_processor.process_order_payment("ORDER-002", 149.50, {"paypal_email": "user@example.com"})
    payment_processor.refund_order("ORDER-002", "paypal_txn_149.5", 149.50)


if __name__ == "__main__":
    demonstrate_dip()


"""
🔍 DIP BENEFITS SUMMARY:

✅ BENEFITS OF FOLLOWING DIP:
1. LOOSE COUPLING: High-level modules aren't tied to specific implementations
2. TESTABILITY: Easy to mock dependencies for unit testing
3. FLEXIBILITY: Easy to swap implementations without changing high-level code
4. MAINTAINABILITY: Changes to low-level modules don't affect high-level modules
5. REUSABILITY: High-level modules can work with different implementations
6. DEPENDENCY INJECTION: Enables IoC containers and dependency injection frameworks

❌ PROBLEMS WITH VIOLATING DIP:
1. TIGHT COUPLING: High-level modules tied to specific implementations
2. HARD TO TEST: Difficult to mock concrete dependencies
3. INFLEXIBLE: Hard to change implementations
4. FRAGILE: Changes to low-level modules break high-level modules
5. DUPLICATE CODE: Similar high-level logic repeated for different implementations

💡 DIP IMPLEMENTATION PATTERNS:
- Constructor injection (pass dependencies through constructor)
- Setter injection (set dependencies through properties)
- Interface injection (dependencies provide injection method)
- Service locator pattern
- Dependency injection containers

🔧 DIP BEST PRACTICES:
- Define clear abstractions (interfaces) for all external dependencies
- Use dependency injection frameworks when appropriate
- Keep abstractions focused and stable
- Don't depend on concrete classes in high-level modules
- Use factory patterns when object creation is complex
- Consider using IoC containers for complex dependency graphs
"""
