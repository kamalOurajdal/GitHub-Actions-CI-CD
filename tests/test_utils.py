"""
Comprehensive tests for utility functions.
Tests cover normal cases, edge cases, and error conditions.
"""

import pytest
from src.utils import (
    validate_email,
    calculate_fibonacci,
    reverse_string,
    find_duplicates,
    format_currency,
    is_palindrome,
    merge_dictionaries,
    calculate_statistics,
    validate_phone_number,
    convert_temperature
)


class TestValidateEmail:
    """Test cases for email validation function."""
    
    def test_valid_emails(self):
        """Test various valid email formats."""
        valid_emails = [
            "user@example.com",
            "test.email@domain.co.uk",
            "user+tag@example.org",
            "user123@test-domain.com",
            "a@b.cd"
        ]
        
        for email in valid_emails:
            assert validate_email(email) is True
    
    def test_invalid_emails(self):
        """Test various invalid email formats."""
        invalid_emails = [
            "invalid-email",
            "@example.com",
            "user@",
            "user@.com",
            "",
            "user@example",
            "user name@example.com"
        ]
        
        for email in invalid_emails:
            assert validate_email(email) is False
    
    def test_non_string_input(self):
        """Test that non-string inputs return False."""
        assert validate_email(None) is False
        assert validate_email(123) is False
        assert validate_email([]) is False


class TestCalculateFibonacci:
    """Test cases for Fibonacci sequence calculation."""
    
    def test_normal_cases(self):
        """Test normal Fibonacci calculations."""
        assert calculate_fibonacci(5) == [0, 1, 1, 2, 3]
        assert calculate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
        assert calculate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    def test_edge_cases(self):
        """Test edge cases for Fibonacci."""
        assert calculate_fibonacci(0) == []
        assert calculate_fibonacci(1) == [0]
        assert calculate_fibonacci(2) == [0, 1]
    
    def test_negative_input(self):
        """Test that negative input raises ValueError."""
        with pytest.raises(ValueError, match="n must be non-negative"):
            calculate_fibonacci(-1)
        
        with pytest.raises(ValueError, match="n must be non-negative"):
            calculate_fibonacci(-10)


class TestReverseString:
    """Test cases for string reversal function."""
    
    def test_normal_cases(self):
        """Test normal string reversal."""
        assert reverse_string("hello world") == "world hello"
        assert reverse_string("python programming") == "programming python"
        assert reverse_string("a b c") == "c b a"
    
    def test_single_word(self):
        """Test single word strings."""
        assert reverse_string("python") == "python"
        assert reverse_string("hello") == "hello"
    
    def test_empty_and_whitespace(self):
        """Test empty strings and whitespace."""
        assert reverse_string("") == ""
        assert reverse_string("   ") == ""
        assert reverse_string("  hello  world  ") == "world hello"
    
    def test_non_string_input(self):
        """Test that non-string inputs raise TypeError."""
        with pytest.raises(TypeError, match="Input must be a string"):
            reverse_string(123)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            reverse_string(None)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            reverse_string([])


class TestFindDuplicates:
    """Test cases for duplicate finding function."""
    
    def test_normal_cases(self):
        """Test normal duplicate finding."""
        assert find_duplicates([1, 2, 2, 3, 4, 4, 5]) == [2, 4]
        assert find_duplicates(['a', 'b', 'a', 'c']) == ['a']
        assert find_duplicates([1, 1, 1, 1]) == [1]
    
    def test_no_duplicates(self):
        """Test lists with no duplicates."""
        assert find_duplicates([1, 2, 3, 4]) == []
        assert find_duplicates(['a', 'b', 'c']) == []
        assert find_duplicates([]) == []
    
    def test_mixed_types(self):
        """Test lists with mixed types."""
        assert find_duplicates([1, 'a', 1, 'a', True]) == [1, 'a']
        assert find_duplicates([None, None, 1, 1]) == [None, 1]
    
    def test_non_list_input(self):
        """Test that non-list inputs raise TypeError."""
        with pytest.raises(TypeError, match="Input must be a list"):
            find_duplicates("not a list")
        
        with pytest.raises(TypeError, match="Input must be a list"):
            find_duplicates(123)
        
        with pytest.raises(TypeError, match="Input must be a list"):
            find_duplicates(None)


class TestFormatCurrency:
    """Test cases for currency formatting function."""
    
    def test_normal_cases(self):
        """Test normal currency formatting."""
        assert format_currency(1234.56) == "$1,234.56"
        assert format_currency(1000) == "$1,000.00"
        assert format_currency(0) == "$0.00"
        assert format_currency(999999.99) == "$999,999.99"
    
    def test_different_currencies(self):
        """Test different currency symbols."""
        assert format_currency(1000, "EUR") == "€1,000.00"
        assert format_currency(1000, "GBP") == "£1,000.00"
        assert format_currency(1000, "JPY") == "¥1,000.00"
        assert format_currency(1000, "CAD") == "CAD1,000.00"
    
    def test_negative_amounts(self):
        """Test negative amounts."""
        assert format_currency(-1234.56) == "$-1,234.56"
        assert format_currency(-1000, "EUR") == "€-1,000.00"
    
    def test_non_numeric_input(self):
        """Test that non-numeric inputs raise TypeError."""
        with pytest.raises(TypeError, match="Amount must be a number"):
            format_currency("not a number")
        
        with pytest.raises(TypeError, match="Amount must be a number"):
            format_currency(None)
        
        with pytest.raises(TypeError, match="Amount must be a number"):
            format_currency([])


class TestIsPalindrome:
    """Test cases for palindrome checking function."""
    
    def test_valid_palindromes(self):
        """Test valid palindromes."""
        assert is_palindrome("racecar") is True
        assert is_palindrome("A man a plan a canal Panama") is True
        assert is_palindrome("Madam, I'm Adam") is True
        assert is_palindrome("12321") is True
        assert is_palindrome("") is True
        assert is_palindrome("a") is True
    
    def test_not_palindromes(self):
        """Test strings that are not palindromes."""
        assert is_palindrome("hello") is False
        assert is_palindrome("python") is False
        assert is_palindrome("not a palindrome") is False
        assert is_palindrome("12345") is False
    
    def test_case_insensitive(self):
        """Test that palindrome check is case insensitive."""
        assert is_palindrome("Racecar") is True
        assert is_palindrome("MADAM") is True
        assert is_palindrome("Madam") is True
    
    def test_ignores_punctuation(self):
        """Test that punctuation is ignored."""
        assert is_palindrome("A man, a plan, a canal: Panama") is True
        assert is_palindrome("Was it a car or a cat I saw?") is True
    
    def test_non_string_input(self):
        """Test that non-string inputs raise TypeError."""
        with pytest.raises(TypeError, match="Input must be a string"):
            is_palindrome(123)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            is_palindrome(None)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            is_palindrome([])


class TestMergeDictionaries:
    """Test cases for dictionary merging function."""
    
    def test_normal_merging(self):
        """Test normal dictionary merging."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 3, "c": 4}
        assert merge_dictionaries(dict1, dict2) == expected
    
    def test_empty_dictionaries(self):
        """Test merging with empty dictionaries."""
        assert merge_dictionaries({}, {"a": 1}) == {"a": 1}
        assert merge_dictionaries({"a": 1}, {}) == {"a": 1}
        assert merge_dictionaries({}, {}) == {}
    
    def test_nested_dictionaries(self):
        """Test merging nested dictionaries."""
        dict1 = {"a": {"x": 1}, "b": 2}
        dict2 = {"a": {"y": 2}, "c": 3}
        expected = {"a": {"y": 2}, "b": 2, "c": 3}
        assert merge_dictionaries(dict1, dict2) == expected
    
    def test_non_dict_input(self):
        """Test that non-dict inputs raise TypeError."""
        with pytest.raises(TypeError, match="Both arguments must be dictionaries"):
            merge_dictionaries({"a": 1}, "not a dict")
        
        with pytest.raises(TypeError, match="Both arguments must be dictionaries"):
            merge_dictionaries("not a dict", {"a": 1})
        
        with pytest.raises(TypeError, match="Both arguments must be dictionaries"):
            merge_dictionaries(None, {"a": 1})


class TestCalculateStatistics:
    """Test cases for statistics calculation function."""
    
    def test_normal_cases(self):
        """Test normal statistics calculations."""
        result = calculate_statistics([1, 2, 3, 4, 5])
        expected = {'mean': 3.0, 'median': 3.0, 'min': 1.0, 'max': 5.0}
        assert result == expected
        
        result = calculate_statistics([1, 2, 3, 4])
        expected = {'mean': 2.5, 'median': 2.5, 'min': 1.0, 'max': 4.0}
        assert result == expected
    
    def test_single_element(self):
        """Test statistics with single element."""
        result = calculate_statistics([42])
        expected = {'mean': 42.0, 'median': 42.0, 'min': 42.0, 'max': 42.0}
        assert result == expected
    
    def test_negative_numbers(self):
        """Test statistics with negative numbers."""
        result = calculate_statistics([-5, -3, 0, 3, 5])
        expected = {'mean': 0.0, 'median': 0.0, 'min': -5.0, 'max': 5.0}
        assert result == expected
    
    def test_floating_point(self):
        """Test statistics with floating point numbers."""
        result = calculate_statistics([1.5, 2.5, 3.5])
        expected = {'mean': 2.5, 'median': 2.5, 'min': 1.5, 'max': 3.5}
        assert result == expected
    
    def test_empty_list(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="List cannot be empty"):
            calculate_statistics([])
    
    def test_non_list_input(self):
        """Test that non-list inputs raise TypeError."""
        with pytest.raises(TypeError, match="Input must be a list"):
            calculate_statistics("not a list")
        
        with pytest.raises(TypeError, match="Input must be a list"):
            calculate_statistics(123)
    
    def test_non_numeric_elements(self):
        """Test that non-numeric elements raise TypeError."""
        with pytest.raises(TypeError, match="All elements must be numbers"):
            calculate_statistics([1, 2, "three", 4])
        
        with pytest.raises(TypeError, match="All elements must be numbers"):
            calculate_statistics([1, None, 3])


class TestValidatePhoneNumber:
    """Test cases for phone number validation function."""
    
    def test_valid_phone_numbers(self):
        """Test valid phone number formats."""
        valid_numbers = [
            "+1-555-123-4567",
            "555-123-4567",
            "(555) 123-4567",
            "555.123.4567",
            "555 123 4567",
            "+44 20 7946 0958",
            "+1 555 123 4567"
        ]
        
        for phone in valid_numbers:
            assert validate_phone_number(phone) is True
    
    def test_invalid_phone_numbers(self):
        """Test invalid phone number formats."""
        invalid_numbers = [
            "invalid",
            "123",
            "555-123",
            "555-123-456",
            "abc-def-ghij",
            "",
            "555-123-45678"  # too long
        ]
        
        for phone in invalid_numbers:
            assert validate_phone_number(phone) is False
    
    def test_non_string_input(self):
        """Test that non-string inputs return False."""
        assert validate_phone_number(None) is False
        assert validate_phone_number(123) is False
        assert validate_phone_number([]) is False


class TestConvertTemperature:
    """Test cases for temperature conversion function."""
    
    def test_celsius_to_fahrenheit(self):
        """Test Celsius to Fahrenheit conversion."""
        assert convert_temperature(0, 'C', 'F') == 32.0
        assert convert_temperature(100, 'C', 'F') == 212.0
        assert convert_temperature(-40, 'C', 'F') == -40.0
    
    def test_fahrenheit_to_celsius(self):
        """Test Fahrenheit to Celsius conversion."""
        assert convert_temperature(32, 'F', 'C') == 0.0
        assert convert_temperature(212, 'F', 'C') == 100.0
        assert convert_temperature(-40, 'F', 'C') == -40.0
    
    def test_celsius_to_kelvin(self):
        """Test Celsius to Kelvin conversion."""
        assert convert_temperature(0, 'C', 'K') == 273.15
        assert convert_temperature(100, 'C', 'K') == 373.15
        assert convert_temperature(-273.15, 'C', 'K') == 0.0
    
    def test_kelvin_to_celsius(self):
        """Test Kelvin to Celsius conversion."""
        assert convert_temperature(273.15, 'K', 'C') == 0.0
        assert convert_temperature(373.15, 'K', 'C') == 100.0
        assert convert_temperature(0, 'K', 'C') == -273.15
    
    def test_fahrenheit_to_kelvin(self):
        """Test Fahrenheit to Kelvin conversion."""
        assert convert_temperature(32, 'F', 'K') == 273.15
        assert convert_temperature(212, 'F', 'K') == 373.15
    
    def test_kelvin_to_fahrenheit(self):
        """Test Kelvin to Fahrenheit conversion."""
        assert convert_temperature(273.15, 'K', 'F') == 32.0
        assert convert_temperature(373.15, 'K', 'F') == 212.0
    
    def test_invalid_units(self):
        """Test that invalid units raise ValueError."""
        with pytest.raises(ValueError, match="Invalid unit"):
            convert_temperature(100, 'C', 'X')
        
        with pytest.raises(ValueError, match="Invalid unit"):
            convert_temperature(100, 'X', 'F')
        
        with pytest.raises(ValueError, match="Invalid unit"):
            convert_temperature(100, 'X', 'Y')
    
    def test_non_numeric_value(self):
        """Test that non-numeric values raise TypeError."""
        with pytest.raises(TypeError, match="Value must be a number"):
            convert_temperature("100", 'C', 'F')
        
        with pytest.raises(TypeError, match="Value must be a number"):
            convert_temperature(None, 'C', 'F')
        
        with pytest.raises(TypeError, match="Value must be a number"):
            convert_temperature([100], 'C', 'F')


# Parametrized tests for more comprehensive coverage
@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),
    ("test@domain.co.uk", True),
    ("invalid-email", False),
    ("@example.com", False),
    ("user@", False),
    ("", False),
    (None, False),
])
def test_validate_email_parametrized(email, expected):
    """Parametrized test for email validation."""
    assert validate_email(email) == expected


@pytest.mark.parametrize("n,expected", [
    (0, []),
    (1, [0]),
    (2, [0, 1]),
    (5, [0, 1, 1, 2, 3]),
    (7, [0, 1, 1, 2, 3, 5, 8]),
])
def test_calculate_fibonacci_parametrized(n, expected):
    """Parametrized test for Fibonacci calculation."""
    assert calculate_fibonacci(n) == expected


@pytest.mark.parametrize("text,expected", [
    ("hello world", "world hello"),
    ("python", "python"),
    ("a b c", "c b a"),
    ("", ""),
    ("  hello  world  ", "world hello"),
])
def test_reverse_string_parametrized(text, expected):
    """Parametrized test for string reversal."""
    assert reverse_string(text) == expected


@pytest.mark.parametrize("items,expected", [
    ([1, 2, 2, 3, 4, 4, 5], [2, 4]),
    (['a', 'b', 'a', 'c'], ['a']),
    ([1, 2, 3, 4], []),
    ([1, 1, 1, 1], [1]),
    ([], []),
])
def test_find_duplicates_parametrized(items, expected):
    """Parametrized test for duplicate finding."""
    result = find_duplicates(items)
    assert sorted(result) == sorted(expected)  # Order doesn't matter


@pytest.mark.parametrize("amount,currency,expected", [
    (1234.56, "USD", "$1,234.56"),
    (1000, "EUR", "€1,000.00"),
    (0, "GBP", "£0.00"),
    (-1234.56, "USD", "$-1,234.56"),
])
def test_format_currency_parametrized(amount, currency, expected):
    """Parametrized test for currency formatting."""
    assert format_currency(amount, currency) == expected


@pytest.mark.parametrize("text,expected", [
    ("racecar", True),
    ("A man a plan a canal Panama", True),
    ("hello", False),
    ("", True),
    ("a", True),
    ("12321", True),
])
def test_is_palindrome_parametrized(text, expected):
    """Parametrized test for palindrome checking."""
    assert is_palindrome(text) == expected


@pytest.mark.parametrize("dict1,dict2,expected", [
    ({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 1, "b": 3, "c": 4}),
    ({}, {"a": 1}, {"a": 1}),
    ({"a": 1}, {}, {"a": 1}),
    ({}, {}, {}),
])
def test_merge_dictionaries_parametrized(dict1, dict2, expected):
    """Parametrized test for dictionary merging."""
    assert merge_dictionaries(dict1, dict2) == expected


@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3, 4, 5], {'mean': 3.0, 'median': 3.0, 'min': 1.0, 'max': 5.0}),
    ([1, 2, 3, 4], {'mean': 2.5, 'median': 2.5, 'min': 1.0, 'max': 4.0}),
    ([42], {'mean': 42.0, 'median': 42.0, 'min': 42.0, 'max': 42.0}),
])
def test_calculate_statistics_parametrized(numbers, expected):
    """Parametrized test for statistics calculation."""
    assert calculate_statistics(numbers) == expected


@pytest.mark.parametrize("phone,expected", [
    ("+1-555-123-4567", True),
    ("555-123-4567", True),
    ("(555) 123-4567", True),
    ("invalid", False),
    ("123", False),
    ("", False),
])
def test_validate_phone_number_parametrized(phone, expected):
    """Parametrized test for phone number validation."""
    assert validate_phone_number(phone) == expected


@pytest.mark.parametrize("value,from_unit,to_unit,expected", [
    (0, 'C', 'F', 32.0),
    (100, 'C', 'F', 212.0),
    (32, 'F', 'C', 0.0),
    (212, 'F', 'C', 100.0),
    (0, 'C', 'K', 273.15),
    (273.15, 'K', 'C', 0.0),
])
def test_convert_temperature_parametrized(value, from_unit, to_unit, expected):
    """Parametrized test for temperature conversion."""
    assert convert_temperature(value, from_unit, to_unit) == expected 