"""
SOLID Principles Demonstration

This file demonstrates all five SOLID principles working together
in a cohesive example: an e-commerce order processing system.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import json


# ========================================
# DATA MODELS
# ========================================

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


@dataclass
class Product:
    id: str
    name: str
    price: float
    category: str


@dataclass
class OrderItem:
    product: Product
    quantity: int
    
    @property
    def total_price(self) -> float:
        return self.product.price * self.quantity


@dataclass
class Customer:
    id: str
    name: str
    email: str
    customer_type: str  # regular, premium, vip


@dataclass
class Order:
    id: str
    customer: Customer
    items: List[OrderItem]
    status: OrderStatus = OrderStatus.PENDING
    
    @property
    def subtotal(self) -> float:
        return sum(item.total_price for item in self.items)


# ========================================
# SRP: SINGLE RESPONSIBILITY PRINCIPLE
# Each class has one reason to change
# ========================================

class OrderValidator:
    """SRP: Only responsible for validating orders."""
    
    def validate_order(self, order: Order) -> tuple[bool, str]:
        if not order.items:
            return False, "Order must have at least one item"
        
        if order.subtotal <= 0:
            return False, "Order total must be positive"
        
        if not order.customer.email:
            return False, "Customer must have a valid email"
        
        return True, ""


class TaxCalculator:
    """SRP: Only responsible for calculating taxes."""
    
    def __init__(self, tax_rate: float = 0.08):
        self.tax_rate = tax_rate
    
    def calculate_tax(self, subtotal: float) -> float:
        return subtotal * self.tax_rate


class OrderRepository:
    """SRP: Only responsible for order data persistence."""
    
    def __init__(self):
        self.orders: Dict[str, Order] = {}
    
    def save_order(self, order: Order) -> bool:
        self.orders[order.id] = order
        print(f"Order {order.id} saved to repository")
        return True
    
    def get_order(self, order_id: str) -> Optional[Order]:
        return self.orders.get(order_id)
    
    def update_order_status(self, order_id: str, status: OrderStatus) -> bool:
        if order_id in self.orders:
            self.orders[order_id].status = status
            print(f"Order {order_id} status updated to {status.value}")
            return True
        return False


# ========================================
# OCP: OPEN/CLOSED PRINCIPLE
# Open for extension, closed for modification
# ========================================

class DiscountStrategy(ABC):
    """OCP: Abstract discount strategy - open for extension."""
    
    @abstractmethod
    def calculate_discount(self, order: Order) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass


class NoDiscountStrategy(DiscountStrategy):
    """OCP: No discount implementation."""
    
    def calculate_discount(self, order: Order) -> float:
        return 0.0
    
    def get_description(self) -> str:
        return "No discount"


class PercentageDiscountStrategy(DiscountStrategy):
    """OCP: Percentage-based discount."""
    
    def __init__(self, percentage: float):
        self.percentage = percentage
    
    def calculate_discount(self, order: Order) -> float:
        return order.subtotal * (self.percentage / 100)
    
    def get_description(self) -> str:
        return f"{self.percentage}% discount"


class CustomerTypeDiscountStrategy(DiscountStrategy):
    """OCP: Customer type-based discount."""
    
    def __init__(self):
        self.discounts = {
            "regular": 0.0,
            "premium": 0.1,
            "vip": 0.15
        }
    
    def calculate_discount(self, order: Order) -> float:
        discount_rate = self.discounts.get(order.customer.customer_type, 0.0)
        return order.subtotal * discount_rate
    
    def get_description(self) -> str:
        return "Customer loyalty discount"


class BulkOrderDiscountStrategy(DiscountStrategy):
    """OCP: New discount strategy - extends without modifying existing code."""
    
    def __init__(self, min_items: int = 10, discount_rate: float = 0.05):
        self.min_items = min_items
        self.discount_rate = discount_rate
    
    def calculate_discount(self, order: Order) -> float:
        total_items = sum(item.quantity for item in order.items)
        if total_items >= self.min_items:
            return order.subtotal * self.discount_rate
        return 0.0
    
    def get_description(self) -> str:
        return f"Bulk order discount ({self.min_items}+ items)"


# ========================================
# LSP: LISKOV SUBSTITUTION PRINCIPLE
# Subtypes must be substitutable for their base types
# ========================================

class PaymentMethod(ABC):
    """LSP: Base payment method that defines the contract."""
    
    @abstractmethod
    def process_payment(self, amount: float) -> Dict[str, Any]:
        """Process payment and return result with consistent structure."""
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if payment method is available."""
        pass


class CreditCardPayment(PaymentMethod):
    """LSP: Credit card payment - substitutable for PaymentMethod."""
    
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    def process_payment(self, amount: float) -> Dict[str, Any]:
        # All payment methods return the same structure
        if amount <= 0:
            return {"success": False, "error": "Invalid amount"}
        
        print(f"Processing credit card payment: ${amount}")
        return {
            "success": True,
            "transaction_id": f"cc_{self.card_number[-4:]}_{amount}",
            "method": "credit_card"
        }
    
    def is_available(self) -> bool:
        return len(self.card_number) >= 16


class PayPalPayment(PaymentMethod):
    """LSP: PayPal payment - substitutable for PaymentMethod."""
    
    def __init__(self, email: str):
        self.email = email
    
    def process_payment(self, amount: float) -> Dict[str, Any]:
        # Same contract as base class
        if amount <= 0:
            return {"success": False, "error": "Invalid amount"}
        
        print(f"Processing PayPal payment: ${amount}")
        return {
            "success": True,
            "transaction_id": f"pp_{self.email}_{amount}",
            "method": "paypal"
        }
    
    def is_available(self) -> bool:
        return "@" in self.email


class BankTransferPayment(PaymentMethod):
    """LSP: Bank transfer - new payment method that's fully substitutable."""
    
    def __init__(self, account_number: str):
        self.account_number = account_number
    
    def process_payment(self, amount: float) -> Dict[str, Any]:
        # Follows the same contract
        if amount <= 0:
            return {"success": False, "error": "Invalid amount"}
        
        print(f"Processing bank transfer: ${amount}")
        return {
            "success": True,
            "transaction_id": f"bt_{self.account_number}_{amount}",
            "method": "bank_transfer"
        }
    
    def is_available(self) -> bool:
        return len(self.account_number) >= 10


# ========================================
# ISP: INTERFACE SEGREGATION PRINCIPLE
# Clients shouldn't depend on interfaces they don't use
# ========================================

class OrderNotifiable(ABC):
    """ISP: Interface for order notifications."""
    
    @abstractmethod
    def send_order_confirmation(self, order: Order) -> bool:
        pass


class ShippingNotifiable(ABC):
    """ISP: Interface for shipping notifications."""
    
    @abstractmethod
    def send_shipping_notification(self, order: Order, tracking_number: str) -> bool:
        pass


class PromotionalNotifiable(ABC):
    """ISP: Interface for promotional notifications."""
    
    @abstractmethod
    def send_promotion(self, customer: Customer, promotion: str) -> bool:
        pass


class EmailNotificationService(OrderNotifiable, ShippingNotifiable, PromotionalNotifiable):
    """ISP: Email service implements all notification interfaces it supports."""
    
    def send_order_confirmation(self, order: Order) -> bool:
        print(f"Email: Order confirmation sent to {order.customer.email}")
        return True
    
    def send_shipping_notification(self, order: Order, tracking_number: str) -> bool:
        print(f"Email: Shipping notification sent to {order.customer.email}")
        print(f"Tracking number: {tracking_number}")
        return True
    
    def send_promotion(self, customer: Customer, promotion: str) -> bool:
        print(f"Email: Promotion sent to {customer.email}: {promotion}")
        return True


class SMSNotificationService(OrderNotifiable):
    """ISP: SMS service only implements order notifications (not all interfaces)."""
    
    def send_order_confirmation(self, order: Order) -> bool:
        # Assuming we have phone number in a real implementation
        print(f"SMS: Order confirmation sent to customer {order.customer.name}")
        return True


class PushNotificationService(PromotionalNotifiable):
    """ISP: Push notifications only for promotions."""
    
    def send_promotion(self, customer: Customer, promotion: str) -> bool:
        print(f"Push: Promotion sent to {customer.name}: {promotion}")
        return True


# ========================================
# DIP: DEPENDENCY INVERSION PRINCIPLE
# Depend on abstractions, not concretions
# ========================================

class Logger(ABC):
    """DIP: Abstraction for logging."""
    
    @abstractmethod
    def log(self, level: str, message: str) -> None:
        pass


class FileLogger(Logger):
    """DIP: Concrete file logger implementation."""
    
    def log(self, level: str, message: str) -> None:
        print(f"[FILE-{level}] {message}")


class DatabaseLogger(Logger):
    """DIP: Concrete database logger implementation."""
    
    def log(self, level: str, message: str) -> None:
        print(f"[DB-{level}] {message}")


class PaymentGateway(ABC):
    """DIP: Abstraction for payment processing."""
    
    @abstractmethod
    def charge(self, payment_method: PaymentMethod, amount: float) -> Dict[str, Any]:
        pass


class StripePaymentGateway(PaymentGateway):
    """DIP: Stripe implementation."""
    
    def charge(self, payment_method: PaymentMethod, amount: float) -> Dict[str, Any]:
        if not payment_method.is_available():
            return {"success": False, "error": "Payment method not available"}
        
        return payment_method.process_payment(amount)


# ========================================
# MAIN ORDER PROCESSING SERVICE
# Demonstrates all SOLID principles working together
# ========================================

class OrderProcessingService:
    """
    Main service that demonstrates all SOLID principles:
    - SRP: Only responsible for orchestrating order processing
    - OCP: Can work with any discount strategy
    - LSP: Can work with any payment method
    - ISP: Uses only the notification interfaces it needs
    - DIP: Depends on abstractions, not concrete implementations
    """
    
    def __init__(self, 
                 validator: OrderValidator,
                 tax_calculator: TaxCalculator,
                 repository: OrderRepository,
                 payment_gateway: PaymentGateway,
                 logger: Logger,
                 order_notifier: OrderNotifiable,
                 shipping_notifier: Optional[ShippingNotifiable] = None):
        # DIP: All dependencies are abstractions
        self.validator = validator
        self.tax_calculator = tax_calculator
        self.repository = repository
        self.payment_gateway = payment_gateway
        self.logger = logger
        self.order_notifier = order_notifier
        self.shipping_notifier = shipping_notifier
        
        # OCP: Default discount strategy (can be changed)
        self.discount_strategy = NoDiscountStrategy()
    
    def set_discount_strategy(self, strategy: DiscountStrategy) -> None:
        """OCP: Set discount strategy without modifying the class."""
        self.discount_strategy = strategy
    
    def process_order(self, order: Order, payment_method: PaymentMethod) -> bool:
        """Process an order through the complete workflow."""
        
        try:
            # SRP: Validate using dedicated validator
            is_valid, error_message = self.validator.validate_order(order)
            if not is_valid:
                self.logger.log("ERROR", f"Order validation failed: {error_message}")
                return False
            
            # OCP: Apply discount using strategy pattern
            discount = self.discount_strategy.calculate_discount(order)
            subtotal = order.subtotal
            discounted_subtotal = subtotal - discount
            
            # SRP: Calculate tax using dedicated calculator
            tax = self.tax_calculator.calculate_tax(discounted_subtotal)
            total = discounted_subtotal + tax
            
            self.logger.log("INFO", f"Order {order.id} - Subtotal: ${subtotal}, "
                                  f"Discount: ${discount}, Tax: ${tax}, Total: ${total}")
            
            # DIP: Process payment through injected gateway
            # LSP: Payment method is substitutable
            payment_result = self.payment_gateway.charge(payment_method, total)
            
            if not payment_result.get("success"):
                self.logger.log("ERROR", f"Payment failed: {payment_result.get('error')}")
                return False
            
            # SRP: Save order using dedicated repository
            order.status = OrderStatus.PROCESSING
            self.repository.save_order(order)
            
            # ISP: Use only the notification interface we need
            self.order_notifier.send_order_confirmation(order)
            
            self.logger.log("INFO", f"Order {order.id} processed successfully")
            return True
            
        except Exception as e:
            self.logger.log("ERROR", f"Order processing failed: {str(e)}")
            return False
    
    def ship_order(self, order_id: str, tracking_number: str) -> bool:
        """Ship an order and send notifications."""
        
        try:
            # Update order status
            success = self.repository.update_order_status(order_id, OrderStatus.SHIPPED)
            
            if success and self.shipping_notifier:
                # ISP: Use shipping notification interface if available
                order = self.repository.get_order(order_id)
                if order:
                    self.shipping_notifier.send_shipping_notification(order, tracking_number)
            
            self.logger.log("INFO", f"Order {order_id} shipped with tracking {tracking_number}")
            return success
            
        except Exception as e:
            self.logger.log("ERROR", f"Shipping failed: {str(e)}")
            return False


def demonstrate_solid_principles():
    """Demonstrate all SOLID principles working together."""
    
    print("=== SOLID Principles E-commerce Demo ===\n")
    
    # Create sample data
    products = [
        Product("1", "Laptop", 999.99, "Electronics"),
        Product("2", "Mouse", 29.99, "Electronics"),
        Product("3", "Book", 19.99, "Books"),
    ]
    
    customer = Customer("C001", "Alice Johnson", "alice@example.com", "premium")
    
    order_items = [
        OrderItem(products[0], 1),
        OrderItem(products[1], 2),
        OrderItem(products[2], 3),
    ]
    
    order = Order("ORDER-001", customer, order_items)
    
    # DIP: Create dependencies (abstractions)
    validator = OrderValidator()
    tax_calculator = TaxCalculator(0.08)  # 8% tax rate
    repository = OrderRepository()
    payment_gateway = StripePaymentGateway()
    logger = FileLogger()
    email_notifier = EmailNotificationService()
    
    # Create order processing service
    order_service = OrderProcessingService(
        validator=validator,
        tax_calculator=tax_calculator,
        repository=repository,
        payment_gateway=payment_gateway,
        logger=logger,
        order_notifier=email_notifier,
        shipping_notifier=email_notifier
    )
    
    # OCP: Test different discount strategies
    print("--- Testing No Discount ---")
    order_service.set_discount_strategy(NoDiscountStrategy())
    
    # LSP: Test different payment methods
    credit_card = CreditCardPayment("1234567890123456")
    success = order_service.process_order(order, credit_card)
    print(f"Order processing result: {success}\n")
    
    print("--- Testing Customer Type Discount ---")
    order_service.set_discount_strategy(CustomerTypeDiscountStrategy())
    
    paypal = PayPalPayment("alice@example.com")
    success = order_service.process_order(order, paypal)
    print(f"Order processing result: {success}\n")
    
    print("--- Testing Bulk Order Discount ---")
    # Create a bulk order
    bulk_items = [OrderItem(products[1], 15)]  # 15 mice
    bulk_order = Order("ORDER-002", customer, bulk_items)
    
    order_service.set_discount_strategy(BulkOrderDiscountStrategy(min_items=10))
    
    bank_transfer = BankTransferPayment("1234567890")
    success = order_service.process_order(bulk_order, bank_transfer)
    print(f"Bulk order processing result: {success}\n")
    
    # Test shipping
    print("--- Testing Shipping ---")
    order_service.ship_order("ORDER-001", "TRACK123456")
    order_service.ship_order("ORDER-002", "TRACK789012")
    
    print("\n=== SOLID Principles Summary ===")
    print("✅ SRP: Each class has a single responsibility")
    print("✅ OCP: New discount strategies can be added without modification")
    print("✅ LSP: Payment methods are fully substitutable")
    print("✅ ISP: Services implement only needed notification interfaces")
    print("✅ DIP: High-level service depends on abstractions, not concretions")


if __name__ == "__main__":
    demonstrate_solid_principles()
