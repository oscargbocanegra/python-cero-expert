"""
Refactored version following Single Responsibility Principle (SRP)

Each class has a single responsibility:
- CustomerValidator: Validates customer data
- PaymentValidator: Validates payment data
- PaymentProcessor: Processes payments through Stripe
- NotificationService: Handles all types of notifications
- EmailNotifier: Specifically handles email notifications
- SMSNotifier: Specifically handles SMS notifications
- TransactionLogger: Logs transaction information
- PaymentOrchestrator: Coordinates the entire payment process
"""

import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any, Optional
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@dataclass
class Customer:
    """Data class representing a customer."""
    name: str
    contact_info: Dict[str, str]


@dataclass
class PaymentData:
    """Data class representing payment information."""
    amount: int
    source: str
    currency: str = "usd"


@dataclass
class TransactionResult:
    """Data class representing the result of a transaction."""
    success: bool
    charge_id: Optional[str] = None
    error_message: Optional[str] = None
    status: Optional[str] = None


class CustomerValidator:
    """Handles validation of customer data."""
    
    def validate(self, customer: Customer) -> tuple[bool, str]:
        """
        Validate customer data.
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not customer.name:
            return False, "Invalid customer data: missing name"
        
        if not customer.contact_info:
            return False, "Invalid customer data: missing contact info"
        
        return True, ""


class PaymentValidator:
    """Handles validation of payment data."""
    
    def validate(self, payment_data: PaymentData) -> tuple[bool, str]:
        """
        Validate payment data.
        
        Returns:
            tuple: (is_valid, error_message)
        """
        if not payment_data.source:
            return False, "Invalid payment data: missing source"
        
        if payment_data.amount <= 0:
            return False, "Invalid payment data: amount must be positive"
        
        return True, ""


class PaymentProcessor:
    """Handles payment processing through Stripe (simulated for demo)."""
    
    def __init__(self):
        # Simulate Stripe configuration
        self.api_key = os.getenv("STRIPE_API_KEY", "demo_key")
    
    def process_payment(self, customer: Customer, payment_data: PaymentData) -> TransactionResult:
        """
        Process payment through Stripe (simulated).
        
        Returns:
            TransactionResult: Result of the payment processing
        """
        try:
            # Simulate payment processing
            if payment_data.amount <= 0:
                raise ValueError("Amount must be positive")
            
            if not payment_data.source:
                raise ValueError("Payment source is required")
            
            # Simulate successful payment
            charge_id = f"ch_sim_{payment_data.amount}_{payment_data.source[:8]}"
            
            return TransactionResult(
                success=True,
                charge_id=charge_id,
                status="succeeded"
            )
            
        except Exception as e:
            return TransactionResult(
                success=False,
                error_message=str(e)
            )


class NotificationStrategy(ABC):
    """Abstract base class for notification strategies."""
    
    @abstractmethod
    def send_notification(self, customer: Customer, message: str) -> bool:
        """Send notification to customer."""
        pass


class EmailNotifier(NotificationStrategy):
    """Handles email notifications."""
    
    def send_notification(self, customer: Customer, message: str) -> bool:
        """
        Send email notification.
        
        Returns:
            bool: True if notification was sent successfully
        """
        email = customer.contact_info.get("email")
        if not email:
            return False
        
        try:
            msg = MIMEText(message)
            msg["Subject"] = "Payment Confirmation"
            msg["From"] = "no-reply@example.com"
            msg["To"] = email
            
            # In a real implementation, you would actually send the email
            # server = smtplib.SMTP("localhost")
            # server.send_message(msg)
            # server.quit()
            
            print(f"Email sent to {email}")
            return True
            
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False


class SMSNotifier(NotificationStrategy):
    """Handles SMS notifications."""
    
    def __init__(self, sms_gateway: str = "Custom SMS Gateway"):
        self.sms_gateway = sms_gateway
    
    def send_notification(self, customer: Customer, message: str) -> bool:
        """
        Send SMS notification.
        
        Returns:
            bool: True if notification was sent successfully
        """
        phone = customer.contact_info.get("phone")
        if not phone:
            return False
        
        try:
            # In a real implementation, you would integrate with an SMS service
            print(f"SMS sent via {self.sms_gateway} to {phone}: {message}")
            return True
            
        except Exception as e:
            print(f"Failed to send SMS: {e}")
            return False


class NotificationService:
    """Manages notification delivery using appropriate strategy."""
    
    def __init__(self):
        self.email_notifier = EmailNotifier()
        self.sms_notifier = SMSNotifier()
    
    def send_payment_confirmation(self, customer: Customer) -> bool:
        """
        Send payment confirmation using the appropriate method.
        
        Returns:
            bool: True if notification was sent successfully
        """
        message = "Thank you for your payment."
        
        # Try email first, then SMS
        if "email" in customer.contact_info:
            return self.email_notifier.send_notification(customer, message)
        elif "phone" in customer.contact_info:
            return self.sms_notifier.send_notification(customer, message)
        else:
            print("No valid contact information for notification")
            return False


class TransactionLogger:
    """Handles logging of transaction information."""
    
    def __init__(self, log_file: str = "transactions.log"):
        self.log_file = log_file
    
    def log_transaction(self, customer: Customer, payment_data: PaymentData, 
                       result: TransactionResult) -> None:
        """Log transaction details to file."""
        try:
            with open(self.log_file, "a") as log_file:
                log_file.write(f"{customer.name} paid {payment_data.amount}\n")
                if result.success:
                    log_file.write(f"Payment status: {result.status}\n")
                    log_file.write(f"Charge ID: {result.charge_id}\n")
                else:
                    log_file.write(f"Payment failed: {result.error_message}\n")
                log_file.write("---\n")
        except Exception as e:
            print(f"Failed to log transaction: {e}")


class PaymentOrchestrator:
    """
    Orchestrates the entire payment process.
    
    This class coordinates all the other services but doesn't handle
    the specific logic of validation, payment processing, notification, or logging.
    """
    
    def __init__(self):
        self.customer_validator = CustomerValidator()
        self.payment_validator = PaymentValidator()
        self.payment_processor = PaymentProcessor()
        self.notification_service = NotificationService()
        self.transaction_logger = TransactionLogger()
    
    def process_transaction(self, customer_data: Dict[str, Any], 
                          payment_data_dict: Dict[str, Any]) -> bool:
        """
        Process a complete transaction.
        
        Returns:
            bool: True if transaction was successful
        """
        # Create data objects
        customer = Customer(
            name=customer_data.get("name", ""),
            contact_info=customer_data.get("contact_info", {})
        )
        
        payment_data = PaymentData(
            amount=payment_data_dict.get("amount", 0),
            source=payment_data_dict.get("source", ""),
            currency=payment_data_dict.get("currency", "usd")
        )
        
        # Validate customer data
        customer_valid, customer_error = self.customer_validator.validate(customer)
        if not customer_valid:
            print(customer_error)
            return False
        
        # Validate payment data
        payment_valid, payment_error = self.payment_validator.validate(payment_data)
        if not payment_valid:
            print(payment_error)
            return False
        
        # Process payment
        result = self.payment_processor.process_payment(customer, payment_data)
        
        if result.success:
            print("Payment successful")
            
            # Send notification
            self.notification_service.send_payment_confirmation(customer)
            
            # Log transaction
            self.transaction_logger.log_transaction(customer, payment_data, result)
            
            return True
        else:
            print(f"Payment failed: {result.error_message}")
            
            # Log failed transaction
            self.transaction_logger.log_transaction(customer, payment_data, result)
            
            return False


def main():
    """Demonstrate the refactored payment system."""
    payment_orchestrator = PaymentOrchestrator()
    
    # Test data
    customer_data_with_email = {
        "name": "John Doe",
        "contact_info": {"email": "e@mail.com"},
    }
    
    customer_data_with_phone = {
        "name": "Platzi Python",
        "contact_info": {"phone": "1234567890"},
    }
    
    payment_data = {
        "amount": 500,
        "source": "tok_mastercard",
        "currency": "usd"
    }
    
    print("=== Processing payment with email notification ===")
    payment_orchestrator.process_transaction(customer_data_with_email, payment_data)
    
    print("\n=== Processing payment with SMS notification ===")
    payment_orchestrator.process_transaction(customer_data_with_phone, payment_data)


if __name__ == "__main__":
    main()
