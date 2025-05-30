def sum(a,b):
    """
    Sums two numbers.
    
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    
    Returns:
        int, float: The sum of the two numbers.
    """
    return a + b

def subtract(a,b):
    """
    Subtracts the second number from the first.
    
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    
    Returns:
        int, float: The result of the subtraction.
    """
    return a - b

def multiply(a,b):
    """
    Multiplies two numbers.
    
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    
    Returns:
        int, float: The product of the two numbers.
    """
    return a * b

def divide(a,b):
    """
    Divides the first number by the second.
    
    Args:
        a (int, float): The numerator.
        b (int, float): The denominator.
    
    Returns:
        float: The result of the division.
    
    Raises:
        ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

