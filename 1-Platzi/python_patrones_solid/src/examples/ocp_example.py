"""
Open/Closed Principle (OCP) Examples

"Software entities should be open for extension, but closed for modification."

This means you should be able to extend a class's behavior without modifying its source code.
"""

from abc import ABC, abstractmethod
from typing import List


# ========================================
# ❌ VIOLATES Open/Closed Principle
# ========================================

class DiscountCalculatorViolatesOCP:
    """
    ❌ This class violates OCP because every time we want to add a new discount type,
    we need to modify the existing class by adding new if/elif conditions.
    """
    
    def calculate_discount(self, customer_type: str, amount: float) -> float:
        if customer_type == "regular":
            return amount * 0.0  # No discount
        elif customer_type == "premium":
            return amount * 0.1  # 10% discount
        elif customer_type == "vip":
            return amount * 0.2  # 20% discount
        # ❌ Problem: Adding new customer types requires modifying this method
        elif customer_type == "employee":  # New requirement
            return amount * 0.5  # 50% discount
        elif customer_type == "student":  # Another new requirement
            return amount * 0.15  # 15% discount
        else:
            return 0.0


# ========================================
# ✅ FOLLOWS Open/Closed Principle
# ========================================

class DiscountStrategy(ABC):
    """
    ✅ Abstract base class for discount strategies.
    This allows us to extend functionality without modifying existing code.
    """
    
    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        """Calculate discount for given amount."""
        pass
    
    @abstractmethod
    def get_customer_type(self) -> str:
        """Return the customer type this strategy handles."""
        pass


class RegularCustomerDiscount(DiscountStrategy):
    """✅ Discount strategy for regular customers."""
    
    def calculate_discount(self, amount: float) -> float:
        return amount * 0.0  # No discount
    
    def get_customer_type(self) -> str:
        return "regular"


class PremiumCustomerDiscount(DiscountStrategy):
    """✅ Discount strategy for premium customers."""
    
    def calculate_discount(self, amount: float) -> float:
        return amount * 0.1  # 10% discount
    
    def get_customer_type(self) -> str:
        return "premium"


class VIPCustomerDiscount(DiscountStrategy):
    """✅ Discount strategy for VIP customers."""
    
    def calculate_discount(self, amount: float) -> float:
        return amount * 0.2  # 20% discount
    
    def get_customer_type(self) -> str:
        return "vip"


# ✅ NEW DISCOUNT TYPES - Added without modifying existing code!
class EmployeeDiscount(DiscountStrategy):
    """✅ New discount strategy for employees - extends without modification!"""
    
    def calculate_discount(self, amount: float) -> float:
        return amount * 0.5  # 50% discount
    
    def get_customer_type(self) -> str:
        return "employee"


class StudentDiscount(DiscountStrategy):
    """✅ New discount strategy for students - extends without modification!"""
    
    def calculate_discount(self, amount: float) -> float:
        return amount * 0.15  # 15% discount
    
    def get_customer_type(self) -> str:
        return "student"


class DiscountCalculator:
    """
    ✅ This class follows OCP - it's closed for modification but open for extension.
    We can add new discount types without changing this class.
    """
    
    def __init__(self):
        self.strategies: List[DiscountStrategy] = []
    
    def register_strategy(self, strategy: DiscountStrategy) -> None:
        """Register a new discount strategy."""
        self.strategies.append(strategy)
    
    def calculate_discount(self, customer_type: str, amount: float) -> float:
        """Calculate discount using the appropriate strategy."""
        for strategy in self.strategies:
            if strategy.get_customer_type() == customer_type:
                return strategy.calculate_discount(amount)
        return 0.0  # No discount found


# ========================================
# ADVANCED EXAMPLE: Payment Processing
# ========================================

class PaymentProcessor(ABC):
    """Abstract base class for payment processors."""
    
    @abstractmethod
    def process_payment(self, amount: float, **kwargs) -> dict:
        """Process payment and return result."""
        pass


class CreditCardProcessor(PaymentProcessor):
    """✅ Credit card payment processor."""
    
    def process_payment(self, amount: float, **kwargs) -> dict:
        card_number = kwargs.get('card_number')
        cvv = kwargs.get('cvv')
        
        # Simulate credit card processing
        print(f"Processing credit card payment: ${amount}")
        return {
            "success": True,
            "transaction_id": f"cc_{card_number[-4:]}_{amount}",
            "method": "credit_card"
        }


class PayPalProcessor(PaymentProcessor):
    """✅ PayPal payment processor."""
    
    def process_payment(self, amount: float, **kwargs) -> dict:
        email = kwargs.get('paypal_email')
        
        # Simulate PayPal processing
        print(f"Processing PayPal payment: ${amount}")
        return {
            "success": True,
            "transaction_id": f"pp_{email}_{amount}",
            "method": "paypal"
        }


# ✅ NEW PAYMENT METHOD - Added without modifying existing code!
class CryptocurrencyProcessor(PaymentProcessor):
    """✅ New cryptocurrency processor - extends without modification!"""
    
    def process_payment(self, amount: float, **kwargs) -> dict:
        wallet_address = kwargs.get('wallet_address')
        crypto_type = kwargs.get('crypto_type', 'bitcoin')
        
        # Simulate cryptocurrency processing
        print(f"Processing {crypto_type} payment: ${amount}")
        return {
            "success": True,
            "transaction_id": f"crypto_{crypto_type}_{amount}",
            "method": "cryptocurrency"
        }


class PaymentService:
    """
    ✅ Payment service that follows OCP.
    New payment methods can be added without modifying this class.
    """
    
    def __init__(self):
        self.processors: dict[str, PaymentProcessor] = {}
    
    def register_processor(self, payment_type: str, processor: PaymentProcessor) -> None:
        """Register a new payment processor."""
        self.processors[payment_type] = processor
    
    def process_payment(self, payment_type: str, amount: float, **kwargs) -> dict:
        """Process payment using the specified processor."""
        processor = self.processors.get(payment_type)
        if processor:
            return processor.process_payment(amount, **kwargs)
        else:
            return {"success": False, "error": f"Unsupported payment type: {payment_type}"}


def demonstrate_ocp():
    """Demonstrate the Open/Closed Principle in action."""
    
    print("=== OCP Demonstration: Discount Calculator ===")
    
    # Create discount calculator
    calculator = DiscountCalculator()
    
    # Register existing strategies
    calculator.register_strategy(RegularCustomerDiscount())
    calculator.register_strategy(PremiumCustomerDiscount())
    calculator.register_strategy(VIPCustomerDiscount())
    
    # ✅ Add new strategies without modifying existing code
    calculator.register_strategy(EmployeeDiscount())
    calculator.register_strategy(StudentDiscount())
    
    # Test discounts
    amount = 100.0
    customer_types = ["regular", "premium", "vip", "employee", "student"]
    
    for customer_type in customer_types:
        discount = calculator.calculate_discount(customer_type, amount)
        final_amount = amount - discount
        print(f"{customer_type.capitalize()}: ${amount} - ${discount:.2f} = ${final_amount:.2f}")
    
    print("\n=== OCP Demonstration: Payment Service ===")
    
    # Create payment service
    payment_service = PaymentService()
    
    # Register existing processors
    payment_service.register_processor("credit_card", CreditCardProcessor())
    payment_service.register_processor("paypal", PayPalProcessor())
    
    # ✅ Add new processor without modifying existing code
    payment_service.register_processor("cryptocurrency", CryptocurrencyProcessor())
    
    # Test payments
    payments = [
        ("credit_card", 50.0, {"card_number": "1234567890123456", "cvv": "123"}),
        ("paypal", 75.0, {"paypal_email": "user@example.com"}),
        ("cryptocurrency", 100.0, {"wallet_address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "crypto_type": "bitcoin"}),
    ]
    
    for payment_type, amount, kwargs in payments:
        result = payment_service.process_payment(payment_type, amount, **kwargs)
        print(f"Payment result: {result}")


if __name__ == "__main__":
    demonstrate_ocp()


"""
🔍 OCP BENEFITS SUMMARY:

1. EXTENSIBILITY:
   ✅ New discount types and payment methods can be added without modifying existing code
   
2. MAINTAINABILITY:
   ✅ Existing functionality remains untouched when adding new features
   
3. REDUCED RISK:
   ✅ No risk of breaking existing functionality when extending
   
4. CLEAN CODE:
   ✅ No growing if/elif chains or switch statements
   
5. TESTABILITY:
   ✅ Each strategy/processor can be tested independently
   
6. FLEXIBILITY:
   ✅ Strategies can be changed at runtime
"""
