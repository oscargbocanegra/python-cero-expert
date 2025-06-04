# SOLID Principles in Python 🐍

A comprehensive demonstration of the SOLID principles with practical Python examples.

## 🚀 Setup and Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd python_patrones_solid
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env file with your actual API keys
   ```

5. **Run the examples:**
   ```bash
   # Run individual principle examples
   python3 src/initial_code.py          # Original code (violates SRP)
   python3 src/srp_refactored.py        # SRP compliant version
   python3 src/srp_comparison.py        # Side-by-side comparison
   python3 src/ocp_example.py           # Open/Closed Principle
   python3 src/lsp_example.py           # Liskov Substitution Principle
   python3 src/isp_example.py           # Interface Segregation Principle
   python3 src/dip_example.py           # Dependency Inversion Principle
   
   # Run comprehensive SOLID demo
   python3 src/solid_demo.py            # All principles working together
   ```

### Dependencies
- `python-dotenv` - Environment variable management
- `stripe` - Payment processing
- `requests` - HTTP library (stripe dependency)

### Project Structure
```
python_patrones_solid/
├── README.md
├── requirements.txt
├── .env.example
├── .env
├── .gitignore
├── env/                          # Virtual environment
└── src/
    ├── initial_code.py           # Original code (violates SRP)
    ├── srp_refactored.py         # SRP compliant refactor
    ├── srp_comparison.py         # SRP before/after comparison
    ├── ocp_example.py            # Open/Closed Principle examples
    ├── lsp_example.py            # Liskov Substitution Principle examples
    ├── isp_example.py            # Interface Segregation Principle examples
    ├── dip_example.py            # Dependency Inversion Principle examples
    └── solid_demo.py             # Complete SOLID principles demo
```

---

## SOLID Principles Overview

<table>
<colgroup>
<col width="15%" />
<col width="25%" />
<col width="30%" />
<col width="30%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: center;"><strong>Principle</strong></th>
<th style="text-align: center;"><strong>Definition</strong></th>
<th style="text-align: center;"><strong>Benefits</strong></th>
<th style="text-align: center;"><strong>Example File</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>SRP</strong><br>Single Responsibility</td>
<td>A class should have one, and only one, reason to change</td>
<td>• Easier to maintain<br>• Easier to test<br>• Better organization<br>• Reduced coupling</td>
<td><code>srp_refactored.py</code><br><code>srp_comparison.py</code></td>
</tr>
<tr>
<td><strong>OCP</strong><br>Open/Closed</td>
<td>Software entities should be open for extension, but closed for modification</td>
<td>• Extensible code<br>• Reduced risk of bugs<br>• Clean architecture<br>• Flexible design</td>
<td><code>ocp_example.py</code></td>
</tr>
<tr>
<td><strong>LSP</strong><br>Liskov Substitution</td>
<td>Objects of a superclass should be replaceable with objects of its subclasses</td>
<td>• Reliable polymorphism<br>• Predictable behavior<br>• Strong inheritance<br>• Better abstraction</td>
<td><code>lsp_example.py</code></td>
</tr>
<tr>
<td><strong>ISP</strong><br>Interface Segregation</td>
<td>Clients should not be forced to depend upon interfaces they do not use</td>
<td>• Focused interfaces<br>• Reduced dependencies<br>• Better modularity<br>• Easier testing</td>
<td><code>isp_example.py</code></td>
</tr>
<tr>
<td><strong>DIP</strong><br>Dependency Inversion</td>
<td>High-level modules should not depend on low-level modules. Both should depend on abstractions</td>
<td>• Loose coupling<br>• Better testability<br>• Flexible architecture<br>• Dependency injection</td>
<td><code>dip_example.py</code></td>
</tr>
</tbody>
</table>

---

## Quick Start Examples

### 1. Single Responsibility Principle (SRP)
```python
# ❌ Violates SRP - One class doing everything
class PaymentProcessor:
    def validate_data(self): pass
    def process_payment(self): pass
    def send_email(self): pass
    def log_transaction(self): pass

# ✅ Follows SRP - Each class has one responsibility
class PaymentValidator: pass
class PaymentProcessor: pass  
class EmailService: pass
class TransactionLogger: pass
```

### 2. Open/Closed Principle (OCP)
```python
# ✅ Open for extension, closed for modification
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount): pass

class RegularDiscount(DiscountStrategy): pass
class PremiumDiscount(DiscountStrategy): pass
class VIPDiscount(DiscountStrategy): pass  # New discount added without modifying existing code
```

### 3. Liskov Substitution Principle (LSP)
```python
# ✅ All shapes are substitutable
def calculate_total_area(shapes: List[Shape]) -> float:
    return sum(shape.area() for shape in shapes)

# Works with any Shape subclass
shapes = [Rectangle(5, 3), Circle(2), Square(4)]
total = calculate_total_area(shapes)
```

### 4. Interface Segregation Principle (ISP)
```python
# ✅ Small, focused interfaces
class Readable(ABC):
    @abstractmethod
    def read(self): pass

class Writable(ABC):
    @abstractmethod
    def write(self): pass

# Classes implement only what they need
class ReadOnlyFile(Readable): pass
class ReadWriteFile(Readable, Writable): pass
```

### 5. Dependency Inversion Principle (DIP)
```python
# ✅ Depend on abstractions, not concretions
class OrderService:
    def __init__(self, db: DatabaseRepository, notifier: NotificationService):
        self.db = db          # Abstract dependency
        self.notifier = notifier  # Abstract dependency
    
# Easy to test and swap implementations
service = OrderService(MySQLRepository(), EmailNotifier())
```

---

## Running the Examples

Each example file is self-contained and demonstrates specific concepts:

```bash
# Individual principle demonstrations
python3 src/srp_refactored.py    # See SRP refactoring in action
python3 src/ocp_example.py       # Add new discount types without modification
python3 src/lsp_example.py       # Proper inheritance and substitution
python3 src/isp_example.py       # Focused interfaces for different needs
python3 src/dip_example.py       # Loose coupling through dependency injection

# Complete e-commerce example with all principles
python3 src/solid_demo.py        # See all SOLID principles working together
```

---

## Key Takeaways

### ✅ SOLID Benefits
- **Maintainable Code**: Easy to modify and extend
- **Testable Code**: Each component can be tested in isolation
- **Flexible Architecture**: Easy to swap implementations
- **Readable Code**: Clear responsibilities and relationships
- **Scalable Design**: Can grow without becoming unwieldy

### 🚫 Common Violations to Avoid
- **SRP**: Classes that do too many things
- **OCP**: Modifying existing code to add features
- **LSP**: Subclasses that break parent class contracts
- **ISP**: Fat interfaces that force unused dependencies
- **DIP**: High-level modules depending on concrete implementations

### 💡 Best Practices
1. **Start with SRP**: Make sure each class has one responsibility
2. **Use Abstractions**: Define interfaces for external dependencies
3. **Favor Composition**: Combine small, focused objects
4. **Test Early**: SOLID code is easier to unit test
5. **Refactor Regularly**: Improve design as requirements evolve

---

## Additional Resources

- [Clean Code by Robert C. Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [SOLID Principles Documentation](https://en.wikipedia.org/wiki/SOLID)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Abstract Base Classes](https://docs.python.org/3/library/abc.html)

---

## Contributing

Feel free to submit issues and pull requests to improve the examples or add new use cases that demonstrate SOLID principles.