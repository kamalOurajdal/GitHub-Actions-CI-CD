"""
Utility functions for common operations.
This module contains well-structured functions with clear documentation.
"""

from typing import List, Dict, Any, Optional, Union
import re
import json
from datetime import datetime, date
import math


def validate_email(email: str) -> bool:
    """
    Validate if a string is a properly formatted email address.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
        
    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    if not email or not isinstance(email, str):
        return False
    
    # Basic email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def calculate_fibonacci(n: int) -> List[int]:
    """
    Calculate the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci numbers to calculate
        
    Returns:
        List[int]: List containing the first n Fibonacci numbers
        
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> calculate_fibonacci(5)
        [0, 1, 1, 2, 3]
        >>> calculate_fibonacci(0)
        []
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return []
    
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence


def reverse_string(text: str) -> str:
    """
    Reverse a string while preserving word boundaries.
    
    Args:
        text (str): The text to reverse
        
    Returns:
        str: The reversed text
        
    Examples:
        >>> reverse_string("hello world")
        'world hello'
        >>> reverse_string("python")
        'python'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    words = text.split()
    return ' '.join(words[::-1])


def find_duplicates(items: List[Any]) -> List[Any]:
    """
    Find duplicate items in a list.
    
    Args:
        items (List[Any]): List of items to check for duplicates
        
    Returns:
        List[Any]: List of duplicate items (without duplicates)
        
    Examples:
        >>> find_duplicates([1, 2, 2, 3, 4, 4, 5])
        [2, 4]
        >>> find_duplicates(['a', 'b', 'a', 'c'])
        ['a']
    """
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    
    seen = set()
    duplicates = set()
    
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Format a number as currency string.
    
    Args:
        amount (float): The amount to format
        currency (str): Currency code (default: "USD")
        
    Returns:
        str: Formatted currency string
        
    Examples:
        >>> format_currency(1234.56)
        '$1,234.56'
        >>> format_currency(1000, "EUR")
        '€1,000.00'
    """
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    
    currency_symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥"
    }
    
    symbol = currency_symbols.get(currency, currency)
    
    # Format with commas and 2 decimal places
    formatted_amount = f"{amount:,.2f}"
    return f"{symbol}{formatted_amount}"


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    
    Args:
        text (str): The text to check
        
    Returns:
        bool: True if text is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove spaces and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned_text == cleaned_text[::-1]


def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dictionaries. If keys exist in both, dict2 values take precedence.
    
    Args:
        dict1 (Dict[str, Any]): First dictionary
        dict2 (Dict[str, Any]): Second dictionary
        
    Returns:
        Dict[str, Any]: Merged dictionary
        
    Examples:
        >>> merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
        {'a': 1, 'b': 3, 'c': 4}
    """
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Both arguments must be dictionaries")
    
    result = dict1.copy()
    result.update(dict2)
    return result


def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
    """
    Calculate basic statistics for a list of numbers.
    
    Args:
        numbers (List[float]): List of numbers to analyze
        
    Returns:
        Dict[str, float]: Dictionary containing mean, median, min, max
        
    Raises:
        ValueError: If list is empty
        
    Examples:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'mean': 3.0, 'median': 3.0, 'min': 1.0, 'max': 5.0}
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("List cannot be empty")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    mean = sum(sorted_numbers) / n
    median = sorted_numbers[n // 2] if n % 2 == 1 else (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    min_val = sorted_numbers[0]
    max_val = sorted_numbers[-1]
    
    return {
        'mean': mean,
        'median': median,
        'min': min_val,
        'max': max_val
    }


def validate_phone_number(phone: str) -> bool:
    """
    Validate if a string is a properly formatted phone number.
    
    Args:
        phone (str): The phone number to validate
        
    Returns:
        bool: True if phone number is valid, False otherwise
        
    Examples:
        >>> validate_phone_number("+1-555-123-4567")
        True
        >>> validate_phone_number("555-123-4567")
        True
        >>> validate_phone_number("invalid")
        False
    """
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove all non-digit characters except + and -
    cleaned = re.sub(r'[^\d+-]', '', phone)
    
    # Check for common phone number patterns
    patterns = [
        r'^\+?1?[-.\s]?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$',  # US format
        r'^\+?[0-9]{10,15}$'  # International format
    ]
    
    return any(re.match(pattern, cleaned) for pattern in patterns)


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert temperature between different units (Celsius, Fahrenheit, Kelvin).
    
    Args:
        value (float): Temperature value to convert
        from_unit (str): Source unit ('C', 'F', or 'K')
        to_unit (str): Target unit ('C', 'F', or 'K')
        
    Returns:
        float: Converted temperature value
        
    Raises:
        ValueError: If units are invalid
        
    Examples:
        >>> convert_temperature(32, 'F', 'C')
        0.0
        >>> convert_temperature(100, 'C', 'F')
        212.0
    """
    valid_units = {'C', 'F', 'K'}
    
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError(f"Invalid unit. Must be one of: {valid_units}")
    
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    
    # Convert to Celsius first
    if from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:  # from_unit == 'C'
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:  # to_unit == 'C'
        return celsius 