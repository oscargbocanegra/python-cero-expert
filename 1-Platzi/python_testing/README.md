# 🐍 Python Testing Project - Platzi Course

[![Python Testing CI](https://github.com/oscargbocanegra/python-cero-expert/actions/workflows/test-python.yml/badge.svg)](https://github.com/oscargbocanegra/python-cero-expert/actions/workflows/test-python.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](./htmlcov/index.html)
[![Code Quality](https://img.shields.io/badge/code%20quality-A+-green.svg)](.)

A comprehensive Python testing project demonstrating unit testing, mocking, coverage analysis, and CI/CD integration using pytest. This project showcases testing best practices with real-world examples including API clients and banking systems.

## 📋 Table of Contents

- [🏗️ Project Structure](#️-project-structure)
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🧪 Running Tests](#-running-tests)
- [📊 Coverage Reports](#-coverage-reports)
- [🔧 Development](#-development)
- [📚 What We Built](#-what-we-built)
- [🎯 Testing Strategies](#-testing-strategies)
- [🤖 CI/CD Pipeline](#-cicd-pipeline)
- [📖 Usage Examples](#-usage-examples)
- [🛠️ Troubleshooting](#️-troubleshooting)

## 🏗️ Project Structure

```
python_testing/
├── 📁 src/                          # Source code
│   ├── 🏦 bank_account.py           # Bank account implementation
│   ├── 🌐 api_client.py             # API client for IP geolocation
│   └── ⚠️  exceptions.py            # Custom exception classes
├── 📁 tests/                        # Test suite
│   ├── 🧪 test_bank_account.py      # Bank account unit tests
│   └── 🧪 test_api_client.py        # API client unit tests
├── 📁 htmlcov/                      # Coverage HTML reports
├── 📁 .vscode/                      # VS Code configuration
│   ├── ⚙️  settings.json           # Test runner settings
│   └── 🚀 launch.json              # Debug configurations
├── 📋 requirements.txt              # Project dependencies
├── 📊 coverage.xml                  # Coverage XML report
├── 📈 .coverage                     # Coverage data file
└── 📚 README.md                     # This file
```

## ✨ Features

### 🏦 Bank Account System
- ✅ **Deposit Operations**: Secure money deposits with validation
- 💸 **Withdrawal Operations**: Smart withdrawals with multiple restrictions
- ⏰ **Business Hours Control**: Only allows withdrawals during business hours (9 AM - 5 PM)
- 📅 **Weekend Restrictions**: Prevents withdrawals on weekends
- 💰 **Balance Management**: Real-time balance tracking and validation
- 📝 **Transaction Logging**: Automatic transaction history logging
- 🛡️ **Input Validation**: Prevents negative amounts and insufficient funds

### 🌐 API Client System
- 🌍 **IP Geolocation**: Fetch location data from IP addresses
- 🔍 **Input Validation**: Comprehensive IP address format validation
- ⚡ **HTTP Integration**: Real API integration with proper error handling
- 🛠️ **Mock Testing**: Extensive mocking for reliable unit tests

### 🧪 Comprehensive Testing Suite
- ✅ **100% Code Coverage**: Every line of code is tested
- 🎭 **Advanced Mocking**: DateTime, HTTP requests, and external dependencies
- 🔄 **CI/CD Integration**: Automated testing with GitHub Actions
- 📊 **Coverage Reports**: HTML and terminal coverage reports
- 🎯 **Edge Case Testing**: Comprehensive validation of error conditions

## 🚀 Quick Start

```bash
# 1️⃣ Clone the repository
git clone https://github.com/oscargbocanegra/python-cero-expert.git
cd python-cero-expert/1-Platzi/python_testing

# 2️⃣ Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run all tests
python -m pytest tests/ -v

# 5️⃣ Generate coverage report
python -m pytest tests/ --cov=src --cov-report=html
```

## 📦 Installation

### Prerequisites
- 🐍 **Python 3.9+** (Recommended: Python 3.12)
- 📦 **pip** (Python package manager)
- 🌐 **Internet connection** (for API testing)

### Step-by-Step Installation

1. **Create and activate virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv env
   
   # Activate virtual environment
   # On Linux/macOS:
   source env/bin/activate
   
   # On Windows:
   env\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python -c "import pytest; print('✅ Installation successful!')"
   ```

## 🧪 Running Tests

### Basic Test Commands

```bash
# 📋 Run all tests
python -m pytest tests/ -v

# 🏦 Run bank account tests only
python -m pytest tests/test_bank_account.py -v

# 🌐 Run API client tests only
python -m pytest tests/test_api_client.py -v

# 🎯 Run specific test
python -m pytest tests/test_bank_account.py::BankAccountTest::test_withdraw -v
```

### Advanced Test Options

```bash
# 📊 Run tests with coverage
python -m pytest tests/ --cov=src --cov-report=term-missing

# 📈 Generate HTML coverage report
python -m pytest tests/ --cov=src --cov-report=html

# 🐛 Run tests with detailed output
python -m pytest tests/ -v --tb=long

# ⚡ Run tests in parallel (if pytest-xdist installed)
python -m pytest tests/ -n auto

# 🔍 Run only failed tests from last run
python -m pytest tests/ --lf
```

### VS Code Integration

This project includes VS Code configuration for seamless testing:

1. **Open project in VS Code**
2. **Install Python extension**
3. **Tests will appear in Test Explorer**
4. **Click ▶️ Run Test buttons** next to individual tests

## 📊 Coverage Reports

### Viewing Coverage

After running tests with coverage, you can view reports in multiple formats:

```bash
# 🖥️ Terminal coverage report
python -m pytest tests/ --cov=src --cov-report=term-missing

# 🌐 HTML coverage report (opens in browser)
python -m pytest tests/ --cov=src --cov-report=html
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### Current Coverage Stats
- 📈 **Overall Coverage**: 100%
- 🏦 **Bank Account Module**: 100% (33/33 statements)
- 🌐 **API Client Module**: 100% (coverage varies)
- ⚠️ **Exceptions Module**: 100%

## 🔧 Development

### Adding New Tests

1. **Create test file** in `tests/` directory
2. **Follow naming convention**: `test_*.py`
3. **Use pytest conventions**:
   ```python
   import unittest
   from unittest.mock import patch, Mock
   
   class TestYourClass(unittest.TestCase):
       def setUp(self):
           # Setup test data
           pass
       
       def test_your_functionality(self):
           # Test implementation
           self.assertEqual(expected, actual)
   ```

### Running Individual Test Classes

```bash
# Run specific test class
python -m pytest tests/test_bank_account.py::BankAccountTest -v

# Run specific test method
python -m pytest tests/test_bank_account.py::BankAccountTest::test_deposit -v
```

## 📚 What We Built

### 🏦 Bank Account Features Implemented

| Feature | Description | Tests |
|---------|-------------|-------|
| 💰 **Deposits** | Add money to account with validation | ✅ Positive amounts<br>❌ Negative amounts |
| 💸 **Withdrawals** | Remove money with business rules | ✅ Sufficient funds<br>❌ Insufficient funds<br>❌ Negative amounts<br>❌ Zero amounts |
| ⏰ **Business Hours** | Only allow withdrawals 9 AM - 5 PM | ✅ Valid hours<br>❌ Before 9 AM<br>❌ After 5 PM |
| 📅 **Weekend Restrictions** | No withdrawals on Saturday/Sunday | ❌ Saturday withdrawals<br>❌ Sunday withdrawals |
| 📝 **Transaction Logging** | Automatic logging to file | ✅ File creation<br>✅ Transaction counting |

### 🌐 API Client Features Implemented

| Feature | Description | Tests |
|---------|-------------|-------|
| 🌍 **IP Geolocation** | Fetch location from valid IPs | ✅ Valid IP addresses |
| 🛡️ **Input Validation** | Comprehensive IP format checking | ❌ Invalid IP format<br>❌ Empty IP strings<br>❌ Out-of-range values |
| ⚡ **HTTP Handling** | Proper HTTP response processing | ✅ Successful responses<br>❌ Error responses |
| 🎭 **Mock Integration** | Isolated testing without external calls | ✅ All scenarios mocked |

## 🎯 Testing Strategies

### 🎭 Mocking Techniques Used

1. **DateTime Mocking**:
   ```python
   @patch('src.bank_account.datetime')
   def test_business_hours(self, mock_datetime):
       mock_datetime.now.return_value.hour = 10
       # Test implementation
   ```

2. **HTTP Request Mocking**:
   ```python
   @patch('src.api_client.requests.get')
   def test_api_call(self, mock_get):
       mock_get.return_value.status_code = 200
       # Test implementation
   ```

3. **Exception Testing**:
   ```python
   def test_invalid_withdrawal(self):
       with self.assertRaises(ValueError):
           self.account.withdraw(-100)
   ```

### 🧪 Test Categories

- **✅ Happy Path Tests**: Normal operation scenarios
- **❌ Error Path Tests**: Exception and error handling
- **🔍 Edge Case Tests**: Boundary conditions and limits
- **🎭 Integration Tests**: Component interaction testing

## 🤖 CI/CD Pipeline

### GitHub Actions Workflow

The project includes an automated CI/CD pipeline that:

1. **🔄 Triggers on**: Push/PR to `python_testing/` folder
2. **🐍 Environment**: Ubuntu with Python 3.12
3. **📦 Dependencies**: Auto-installs requirements
4. **🧪 Testing**: Runs complete test suite
5. **📊 Coverage**: Generates and uploads coverage reports
6. **📈 Artifacts**: Saves HTML coverage reports

### Pipeline Steps:

```yaml
✅ Checkout code
✅ Setup Python 3.12
✅ Install dependencies
✅ Verify test environment
✅ Run all tests
✅ Run individual test files
✅ Generate coverage reports
✅ Upload coverage artifacts
```

## 📖 Usage Examples

### 🏦 Bank Account Usage

```python
from src.bank_account import BankAccount

# Create account
account = BankAccount(balance=1000, log_file='transactions.txt')

# Make deposits
new_balance = account.deposit(500)  # Returns 1500

# Make withdrawals (during business hours)
new_balance = account.withdraw(200)  # Returns 1300

# Error cases
account.withdraw(-100)  # Raises ValueError
account.withdraw(2000)  # Raises ValueError (insufficient funds)
```

### 🌐 API Client Usage

```python
from src.api_client import APIClient

# Create client
client = APIClient()

# Get location data
location = client.get_location("8.8.8.8")
print(location)  # {'country': 'US', 'city': 'Mountain View', ...}

# Error cases
client.get_location("invalid.ip")  # Raises ValueError
client.get_location("")           # Raises ValueError
```

## 🛠️ Troubleshooting

### Common Issues

#### ❌ ModuleNotFoundError
```bash
# Solution: Ensure you're in the correct directory
cd /path/to/python_testing
python -m pytest tests/
```

#### ❌ Import Errors in Tests
```bash
# Solution: Check Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python -m pytest tests/
```

#### ❌ VS Code Test Discovery Issues
```json
// Add to .vscode/settings.json
{
    "python.testing.unittestEnabled": true,
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "test_*.py"
    ]
}
```

#### ❌ Coverage Command Not Found
```bash
# Install coverage
pip install pytest-cov

# Or reinstall all requirements
pip install -r requirements.txt
```

### 🆘 Getting Help

If you encounter issues:

1. **📝 Check logs**: Look at test output for detailed error messages
2. **🔍 Verify environment**: Ensure virtual environment is activated
3. **📦 Update dependencies**: `pip install -r requirements.txt --upgrade`
4. **🐛 Run single test**: Isolate the problem with specific test execution
5. **📞 Create issue**: Open GitHub issue with error details

---

## 🎯 Results Achieved

- ✅ **100% Test Coverage**: All code paths tested
- ✅ **Comprehensive Test Suite**: 15+ test cases covering all scenarios
- ✅ **CI/CD Integration**: Automated testing pipeline
- ✅ **Professional Documentation**: Complete project documentation
- ✅ **Best Practices**: Following Python testing conventions
- ✅ **Real-world Examples**: Banking and API client implementations

## 🚀 Next Steps

To extend this project, consider:

1. **🔐 Add authentication tests** for API client
2. **📊 Implement database integration** tests
3. **🌐 Add more API endpoints** and corresponding tests
4. **📈 Performance testing** with pytest-benchmark
5. **🔒 Security testing** for input validation

---

**📚 Happy Testing! 🧪**

*This project demonstrates professional Python testing practices and serves as a template for test-driven development.*