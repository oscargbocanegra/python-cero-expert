"""
SRP Comparison: Before vs After Refactoring

This file demonstrates the difference between code that violates SRP 
and code that follows SRP principles.
"""

# ========================================
# ❌ BEFORE: Violates Single Responsibility Principle
# ========================================

class PaymentProcessorViolatesSRP:
    """
    ❌ This class violates SRP because it has multiple responsibilities:
    1. Validates customer data
    2. Validates payment data  
    3. Processes payments through Stripe
    4. Sends email notifications
    5. Sends SMS notifications
    6. Logs transactions to file
    
    Problems with this approach:
    - Hard to test individual functionalities
    - Changes in one area affect the entire class
    - Difficult to maintain and extend
    - Violates separation of concerns
    - High coupling between different functionalities
    """
    
    def process_transaction(self, customer_data, payment_data):
        # Responsibility 1: Customer validation
        if not customer_data.get("name"):
            print("Invalid customer data: missing name")
            return
        if not customer_data.get("contact_info"):
            print("Invalid customer data: missing contact info")
            return
        
        # Responsibility 2: Payment validation
        if not payment_data.get("source"):
            print("Invalid payment data")
            return
        
        # Responsibility 3: Payment processing
        import stripe
        stripe.api_key = "sk_test_..."
        try:
            charge = stripe.Charge.create(
                amount=payment_data["amount"],
                currency="usd",
                source=payment_data["source"],
                description="Charge for " + customer_data["name"],
            )
            print("Payment successful")
        except stripe.error.StripeError as e:
            print("Payment failed:", e)
            return
        
        # Responsibility 4: Email notification
        if "email" in customer_data["contact_info"]:
            from email.mime.text import MIMEText
            msg = MIMEText("Thank you for your payment.")
            msg["Subject"] = "Payment Confirmation"
            msg["From"] = "no-reply@example.com"
            msg["To"] = customer_data["contact_info"]["email"]
            print("Email sent to", customer_data["contact_info"]["email"])
        
        # Responsibility 5: SMS notification
        elif "phone" in customer_data["contact_info"]:
            phone_number = customer_data["contact_info"]["phone"]
            print(f"SMS sent to {phone_number}: Thank you for your payment.")
        
        # Responsibility 6: Transaction logging
        with open("transactions.log", "a") as log_file:
            log_file.write(f"{customer_data['name']} paid {payment_data['amount']}\n")


# ========================================
# ✅ AFTER: Follows Single Responsibility Principle
# ========================================

class CustomerValidator:
    """✅ Single Responsibility: Validates customer data only"""
    
    def validate(self, customer_data):
        if not customer_data.get("name"):
            return False, "Invalid customer data: missing name"
        if not customer_data.get("contact_info"):
            return False, "Invalid customer data: missing contact info"
        return True, ""


class PaymentValidator:
    """✅ Single Responsibility: Validates payment data only"""
    
    def validate(self, payment_data):
        if not payment_data.get("source"):
            return False, "Invalid payment data: missing source"
        if payment_data.get("amount", 0) <= 0:
            return False, "Invalid payment data: amount must be positive"
        return True, ""


class StripePaymentProcessor:
    """✅ Single Responsibility: Processes payments through Stripe only"""
    
    def __init__(self, api_key):
        import stripe
        stripe.api_key = api_key
        self.stripe = stripe
    
    def process_payment(self, customer_data, payment_data):
        try:
            charge = self.stripe.Charge.create(
                amount=payment_data["amount"],
                currency="usd",
                source=payment_data["source"],
                description=f"Charge for {customer_data['name']}",
            )
            return {"success": True, "charge": charge}
        except self.stripe.error.StripeError as e:
            return {"success": False, "error": str(e)}


class EmailNotifier:
    """✅ Single Responsibility: Sends email notifications only"""
    
    def send_notification(self, email, message):
        from email.mime.text import MIMEText
        msg = MIMEText(message)
        msg["Subject"] = "Payment Confirmation"
        msg["From"] = "no-reply@example.com"
        msg["To"] = email
        print(f"Email sent to {email}")
        return True


class SMSNotifier:
    """✅ Single Responsibility: Sends SMS notifications only"""
    
    def send_notification(self, phone, message):
        print(f"SMS sent to {phone}: {message}")
        return True


class TransactionLogger:
    """✅ Single Responsibility: Logs transactions only"""
    
    def log_transaction(self, customer_data, payment_data, result):
        with open("transactions.log", "a") as log_file:
            log_file.write(f"{customer_data['name']} paid {payment_data['amount']}\n")
            log_file.write(f"Status: {result.get('success', False)}\n")


class PaymentOrchestrator:
    """
    ✅ Single Responsibility: Coordinates the payment process
    
    This class orchestrates the workflow but doesn't handle the specific
    business logic of each operation - that's delegated to specialized classes.
    """
    
    def __init__(self, stripe_api_key):
        self.customer_validator = CustomerValidator()
        self.payment_validator = PaymentValidator()
        self.payment_processor = StripePaymentProcessor(stripe_api_key)
        self.email_notifier = EmailNotifier()
        self.sms_notifier = SMSNotifier()
        self.transaction_logger = TransactionLogger()
    
    def process_transaction(self, customer_data, payment_data):
        # Validate customer
        customer_valid, customer_error = self.customer_validator.validate(customer_data)
        if not customer_valid:
            print(customer_error)
            return False
        
        # Validate payment
        payment_valid, payment_error = self.payment_validator.validate(payment_data)
        if not payment_valid:
            print(payment_error)
            return False
        
        # Process payment
        result = self.payment_processor.process_payment(customer_data, payment_data)
        
        if result["success"]:
            print("Payment successful")
            
            # Send notification
            contact_info = customer_data["contact_info"]
            if "email" in contact_info:
                self.email_notifier.send_notification(
                    contact_info["email"], 
                    "Thank you for your payment."
                )
            elif "phone" in contact_info:
                self.sms_notifier.send_notification(
                    contact_info["phone"], 
                    "Thank you for your payment."
                )
            
            # Log transaction
            self.transaction_logger.log_transaction(customer_data, payment_data, result)
            return True
        else:
            print(f"Payment failed: {result['error']}")
            return False


# ========================================
# KEY DIFFERENCES AND BENEFITS
# ========================================

"""
🔍 ANALYSIS: What changed and why it's better

1. SEPARATION OF CONCERNS:
   ❌ Before: One class handled 6 different responsibilities
   ✅ After: Each class has exactly one responsibility

2. EASIER TESTING:
   ❌ Before: To test email functionality, you need to mock Stripe, database, etc.
   ✅ After: You can test EmailNotifier in isolation

3. MAINTAINABILITY:
   ❌ Before: Changing email format requires touching payment processing code
   ✅ After: Email changes only affect EmailNotifier class

4. REUSABILITY:
   ❌ Before: Can't reuse email logic without payment processing
   ✅ After: EmailNotifier can be used in other contexts

5. EXTENSIBILITY:
   ❌ Before: Adding new notification types requires modifying main class
   ✅ After: Just create a new notifier class

6. DEBUGGING:
   ❌ Before: Payment issues could be validation, processing, or notification related
   ✅ After: Clear separation makes it easy to identify where issues occur

7. DEPENDENCY MANAGEMENT:
   ❌ Before: Single class depends on Stripe, email libraries, file system, etc.
   ✅ After: Each class has minimal, focused dependencies

8. CODE ORGANIZATION:
   ❌ Before: 80+ lines in one method doing everything
   ✅ After: Small, focused classes and methods that are easy to understand
"""
