from typing import Union


def sum(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Sums two numbers.
    
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    
    Returns:
        int, float: The sum of the two numbers.
    """
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtracts the second number from the first.
    
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    
    Returns:
        int, float: The result of the subtraction.
    """
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplies two numbers.
    
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    
    Returns:
        int, float: The product of the two numbers.
    """
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> float:
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

