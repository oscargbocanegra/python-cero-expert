# 🎯 SOLID Principles in Python - Interactive Learning Course

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-black-black.svg?style=for-the-badge)](https://github.com/psf/black)
[![Learning](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-orange.svg?style=for-the-badge)](README.md)

> 📚 **Interactive SOLID Principles Course** - Learn the 5 fundamental principles of software design with practical Python examples

<div align="center">

![SOLID Principles](https://img.shields.io/badge/S-Single%20Responsibility-red?style=for-the-badge)
![SOLID Principles](https://img.shields.io/badge/O-Open%2FClosed-orange?style=for-the-badge)
![SOLID Principles](https://img.shields.io/badge/L-Liskov%20Substitution-yellow?style=for-the-badge)
![SOLID Principles](https://img.shields.io/badge/I-Interface%20Segregation-green?style=for-the-badge)
![SOLID Principles](https://img.shields.io/badge/D-Dependency%20Inversion-blue?style=for-the-badge)

</div>

---

## 🎓 What Will You Learn?

This course will teach you the **5 SOLID principles** in a practical and progressive way:

- ✅ **Clean Code**: Write maintainable and readable code
- ✅ **Flexible Design**: Create architectures that adapt to change
- ✅ **Testing**: Code that's easier to test
- ✅ **Refactoring**: Improve existing code without breaking functionality
- ✅ **Best Practices**: Apply professional design patterns

---

## 🚀 Quick Setup

### 📋 Prerequisites
- ![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) or higher
- ![pip](https://img.shields.io/badge/pip-latest-green.svg) (Python package installer)

### ⚡ Express Installation

```bash
# 1. Navigate to project directory
cd py_patrones_solid

# 2. Create virtual environment (REQUIRED to avoid conflicts)
python3 -m venv env

# 3. Activate virtual environment
source env/bin/activate  # Linux/Mac
# env\Scripts\activate   # Windows

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Configure environment variables
cp .env.example .env
# Edit .env with your API keys
```

### 🎯 Verify Installation

```bash
# Test that everything works
python3 src/single_responsability/after.py
```

---

## 📁 Project Structure

```
py_patrones_solid/
├── 📖 README.md                     # This complete guide
├── 📦 requirements.txt              # Project dependencies
├── 🔐 .env.example                  # Environment variables template
├── 🔐 .env                          # Your configuration (not versioned)
├── 🚫 .gitignore                    # Files ignored by Git
├── 🐍 env/                          # Virtual environment (not versioned)
│
└── 📂 src/                          # 🎯 MAIN LEARNING CODE
    │
    ├── 🔴 initial_code.py          # ❌ Initial example (violates principles)
    │
    ├── 📁 single_responsability/    # 🎯 S - Single Responsibility Principle
    │   ├── before.py               # ❌ Code that violates SRP
    │   └── after.py                # ✅ Code that follows SRP
    │
    ├── 📁 open_close/              # 🎯 O - Open/Closed Principle  
    │   ├── before.py               # ❌ Code that violates OCP
    │   └── after.py                # ✅ Code that follows OCP
    │
    ├── 📁 liskov_substitution/     # 🎯 L - Liskov Substitution Principle
    │   ├── before.py               # ❌ Code that violates LSP
    │   └── after.py                # ✅ Code that follows LSP
    │
    ├── 📁 interfaces_segregation/  # 🎯 I - Interface Segregation Principle
    │   ├── before.py               # ❌ Code that violates ISP
    │   └── after.py                # ✅ Code that follows ISP
    │
    ├── 📁 dependency_inversion/    # 🎯 D - Dependency Inversion Principle
    │   ├── before.py               # ❌ Code that violates DIP
    │   └── after.py                # ✅ Code that follows DIP
    │
    └── 📁 solid_principles/        # 🎯 Integrated examples (coming soon)
        └── complete_example.py     # 🚀 All principles together
```

### 🎨 Project Dependencies

| Package | Version | Purpose | Badge |
|---------|---------|---------|-------|
| `python-dotenv` | ![Version](https://img.shields.io/badge/v1.1.0-blue) | Environment variables management | ![Purpose](https://img.shields.io/badge/Config-green) |
| `stripe` | ![Version](https://img.shields.io/badge/v12.2.0-blue) | Payment processing (demos) | ![Purpose](https://img.shields.io/badge/Payment-orange) |
| `requests` | ![Version](https://img.shields.io/badge/v2.32.3-blue) | HTTP client | ![Purpose](https://img.shields.io/badge/HTTP-red) |

---

## 🎯 SOLID Learning Path

### 🔥 Recommended Study Mode

| Order | Principle | Difficulty | Estimated Time | Files to Study |
|-------|-----------|------------|----------------|-----------------|
| 1️⃣ | **Single Responsibility** | ![Beginner](https://img.shields.io/badge/Beginner-green) | 30 min | `src/single_responsability/` |
| 2️⃣ | **Open/Closed** | ![Beginner](https://img.shields.io/badge/Beginner-green) | 45 min | `src/open_close/` |
| 3️⃣ | **Liskov Substitution** | ![Intermediate](https://img.shields.io/badge/Intermediate-orange) | 60 min | `src/liskov_substitution/` |
| 4️⃣ | **Interface Segregation** | ![Intermediate](https://img.shields.io/badge/Intermediate-orange) | 45 min | `src/interfaces_segregation/` |
| 5️⃣ | **Dependency Inversion** | ![Advanced](https://img.shields.io/badge/Advanced-red) | 90 min | `src/dependency_inversion/` |

### 📚 How to Study Each Principle

```bash
# For each principle, follow this pattern:

# 1. 👀 First, look at the problematic code
python3 src/[principle]/before.py

# 2. 🤔 Reflect: What problems do you identify?

# 3. ✅ Then, study the solution
python3 src/[principle]/after.py

# 4. 📝 Compare and note the differences
```

---

## 🧠 SOLID Principles - Visual Learning Guide

<table>
<tr>
<td align="center" width="20%">

### 🎯 **S** - Single Responsibility
![SRP](https://img.shields.io/badge/SRP-Single%20Job-red?style=for-the-badge)

**"One class, one responsibility"**

🔥 **Problem**: Classes that do too many things  
✅ **Solution**: Separate responsibilities  
📁 **Study**: `src/single_responsability/`

</td>
<td align="center" width="20%">

### 🔄 **O** - Open/Closed
![OCP](https://img.shields.io/badge/OCP-Extend%20Not%20Modify-orange?style=for-the-badge)

**"Open for extension, closed for modification"**

🔥 **Problem**: Modifying existing code  
✅ **Solution**: Use abstractions and inheritance  
📁 **Study**: `src/open_close/`

</td>
<td align="center" width="20%">

### 🔀 **L** - Liskov Substitution
![LSP](https://img.shields.io/badge/LSP-Replaceable%20Objects-yellow?style=for-the-badge)

**"Derived objects must be replaceable"**

🔥 **Problem**: Subclasses that break contracts  
✅ **Solution**: Correct inheritance  
📁 **Study**: `src/liskov_substitution/`

</td>
<td align="center" width="20%">

### ⚡ **I** - Interface Segregation
![ISP](https://img.shields.io/badge/ISP-Small%20Interfaces-green?style=for-the-badge)

**"Many specific interfaces, not one general"**

🔥 **Problem**: Fat and monolithic interfaces  
✅ **Solution**: Small and focused interfaces  
📁 **Study**: `src/interfaces_segregation/`

</td>
<td align="center" width="20%">

### 🔌 **D** - Dependency Inversion
![DIP](https://img.shields.io/badge/DIP-Depend%20on%20Abstractions-blue?style=for-the-badge)

**"Depend on abstractions, not concretions"**

🔥 **Problem**: Rigid dependencies  
✅ **Solution**: Dependency injection  
📁 **Study**: `src/dependency_inversion/`

</td>
</tr>
</table>

---

## 🛠️ Practical Lab

### 🎮 Interactive Exercises

```bash
# 🔥 CHALLENGE 1: Identify principle violations
python3 src/initial_code.py
# ❓ How many SOLID principles does this code violate?

# 🔥 CHALLENGE 2: Before/after comparison
# Run both files and note the differences
python3 src/single_responsability/before.py
python3 src/single_responsability/after.py

# 🔥 CHALLENGE 3: Create your own example
# Take the pattern from 'after.py' and create your own use case
```

### 📊 Learning Metrics

After each principle, evaluate your understanding:

- [ ] 🟩 **Basic**: I can identify when the principle is violated
- [ ] 🟨 **Intermediate**: I can explain why the code is problematic  
- [ ] 🟧 **Advanced**: I can refactor code to comply with the principle
- [ ] 🟥 **Expert**: I can apply the principle in new projects

---

## 📋 SOLID Technical Summary

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
<th style="text-align: center;"><strong>Study Files</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>SRP</strong><br>Single Responsibility</td>
<td>A class should have one, and only one, reason to change</td>
<td>• Easier to maintain<br>• Easier to test<br>• Better organization<br>• Lower coupling</td>
<td><code>single_responsability/</code><br>├── before.py ❌<br>└── after.py ✅</td>
</tr>
<tr>
<td><strong>OCP</strong><br>Open/Closed</td>
<td>Software entities should be open for extension, but closed for modification</td>
<td>• Extensible code<br>• Lower risk of bugs<br>• Clean architecture<br>• Flexible design</td>
<td><code>open_close/</code><br>├── before.py ❌<br>└── after.py ✅</td>
</tr>
<tr>
<td><strong>LSP</strong><br>Liskov Substitution</td>
<td>Objects of a superclass should be replaceable with objects of their subclasses</td>
<td>• Reliable polymorphism<br>• Predictable behavior<br>• Strong inheritance<br>• Better abstraction</td>
<td><code>liskov_substitution/</code><br>├── before.py ❌<br>└── after.py ✅</td>
</tr>
<tr>
<td><strong>ISP</strong><br>Interface Segregation</td>
<td>Clients should not be forced to depend on interfaces they don't use</td>
<td>• Focused interfaces<br>• Reduced dependencies<br>• Better modularity<br>• Easier testing</td>
<td><code>interfaces_segregation/</code><br>├── before.py ❌<br>└── after.py ✅</td>
</tr>
<tr>
<td><strong>DIP</strong><br>Dependency Inversion</td>
<td>High-level modules should not depend on low-level modules. Both should depend on abstractions</td>
<td>• Low coupling<br>• Better testability<br>• Flexible architecture<br>• Dependency injection</td>
<td><code>dependency_inversion/</code><br>├── before.py ❌<br>└── after.py ✅</td>
</tr>
</tbody>
</table>

---

## 💡 Quick Code Examples

### 1️⃣ Single Responsibility Principle (SRP)
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

### 2️⃣ Open/Closed Principle (OCP)
```python
# ✅ Open for extension, closed for modification
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount): pass

class RegularDiscount(DiscountStrategy): pass
class PremiumDiscount(DiscountStrategy): pass
class VIPDiscount(DiscountStrategy): pass  # New extension without modifying existing code
```

### 3️⃣ Liskov Substitution Principle (LSP)
```python
# ✅ All shapes are substitutable
def calculate_total_area(shapes: List[Shape]) -> float:
    return sum(shape.area() for shape in shapes)

# Works with any Shape subclass
shapes = [Rectangle(5, 3), Circle(2), Square(4)]
total = calculate_total_area(shapes)
```

### 4️⃣ Interface Segregation Principle (ISP)
```python
# ✅ Small and focused interfaces
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

### 5️⃣ Dependency Inversion Principle (DIP)
```python
# ✅ Depends on abstractions, not concretions
class OrderService:
    def __init__(self, db: DatabaseRepository, notifier: NotificationService):
        self.db = db          # Abstract dependency
        self.notifier = notifier  # Abstract dependency
    
# Easy to test and swap implementations
service = OrderService(MySQLRepository(), EmailNotifier())
```

---

## 🎯 Learning Outcomes

### ✅ Upon Completing This Course You'll Be Able To:

<div align="center">

| Skill | Level | Description |
|-------|--------|-------------|
| 🔍 **Identify Violations** | ![Fundamental](https://img.shields.io/badge/Fundamental-blue) | Detect when code violates SOLID principles |
| 🔧 **Refactor Code** | ![Intermediate](https://img.shields.io/badge/Intermediate-orange) | Improve existing code by applying SOLID |
| 🏗️ **Design Architectures** | ![Advanced](https://img.shields.io/badge/Advanced-red) | Create flexible systems from scratch |
| 🧪 **Write Tests** | ![Intermediate](https://img.shields.io/badge/Intermediate-orange) | SOLID code is easier to test |
| 📚 **Apply Patterns** | ![Advanced](https://img.shields.io/badge/Advanced-red) | Use professional design patterns |

</div>

### 🚫 Common Problems You'll Solve

- ❌ **Giant Classes**: Learn to separate responsibilities
- ❌ **Rigid Code**: Create flexible and extensible systems  
- ❌ **Hard to Test**: Write more modular code
- ❌ **Frequent Bugs**: Reduce errors with better design
- ❌ **Complex Maintenance**: Simplify maintenance

### 🎯 Best Practices You'll Master

1. **🎯 Start with SRP**: Ensure each class has one responsibility
2. **🔌 Use Abstractions**: Define interfaces for external dependencies
3. **🧩 Favor Composition**: Combine small and focused objects
4. **🧪 Test Early**: SOLID code is easier to unit test
5. **♻️ Refactor Regularly**: Improve design as requirements evolve

---

## 📚 Additional Resources for Deep Learning

### 📖 Recommended Books
- ![Book](https://img.shields.io/badge/📖-Clean%20Code-green) [Clean Code by Robert C. Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- ![Book](https://img.shields.io/badge/📖-Design%20Patterns-blue) [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612)
- ![Book](https://img.shields.io/badge/📖-Clean%20Architecture-orange) [Clean Architecture by Robert C. Martin](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)

### 🌐 Useful Links
- ![Link](https://img.shields.io/badge/🔗-SOLID%20Principles-blue) [SOLID Documentation](https://en.wikipedia.org/wiki/SOLID)
- ![Link](https://img.shields.io/badge/🔗-Python%20Type%20Hints-green) [Python Type Hints](https://docs.python.org/3/library/typing.html)
- ![Link](https://img.shields.io/badge/🔗-Abstract%20Base%20Classes-orange) [Abstract Base Classes](https://docs.python.org/3/library/abc.html)

### 🎥 Complementary Videos
- ![Video](https://img.shields.io/badge/🎥-Uncle%20Bob%20SOLID-red) Uncle Bob - SOLID Principles
- ![Video](https://img.shields.io/badge/🎥-Python%20Design%20Patterns-blue) Python Design Patterns

---

## 🤝 Contributions and Community

### 💡 How to Contribute?

[![Issues](https://img.shields.io/badge/Issues-Welcome-green?style=for-the-badge)](https://github.com/tu-repo/issues)
[![Pull Requests](https://img.shields.io/badge/Pull%20Requests-Welcome-blue?style=for-the-badge)](https://github.com/tu-repo/pulls)

- 🐛 **Report Bugs**: Help us improve the examples
- 💡 **Suggest Improvements**: Propose new use cases
- 📚 **Add Examples**: Contribute with more practical cases
- 📝 **Improve Documentation**: Make the content clearer

### 🎯 Ideas for Contributing

- [ ] More examples of common violations
- [ ] Use cases from different domains (web, data science, etc.)
- [ ] Interactive exercises with solutions
- [ ] Translation to other languages
- [ ] Explanatory videos

---

*📅 Last updated: June 2025 | 👨‍💻 Made with ❤️ for the Python community*