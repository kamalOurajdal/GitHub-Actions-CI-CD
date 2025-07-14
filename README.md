# Structured Functions with Pytest Tests

This project demonstrates well-structured Python functions with comprehensive test coverage using pytest.

## Project Structure

```
GitHub-Actions-CI-CD/
├── src/
│   ├── __init__.py
│   └── utils.py          # Main utility functions
├── tests/
│   ├── __init__.py
│   └── test_utils.py     # Comprehensive test suite
├── requirements.txt      # Python dependencies
├── pytest.ini          # Pytest configuration
└── README.md           # This file
```

## Functions Overview

The `src/utils.py` module contains the following well-structured functions:

### 1. `validate_email(email: str) -> bool`
Validates if a string is a properly formatted email address.

**Examples:**
```python
validate_email("user@example.com")  # True
validate_email("invalid-email")     # False
```

### 2. `calculate_fibonacci(n: int) -> List[int]`
Calculates the first n numbers in the Fibonacci sequence.

**Examples:**
```python
calculate_fibonacci(5)  # [0, 1, 1, 2, 3]
calculate_fibonacci(0)  # []
```

### 3. `reverse_string(text: str) -> str`
Reverses a string while preserving word boundaries.

**Examples:**
```python
reverse_string("hello world")  # "world hello"
reverse_string("python")       # "python"
```

### 4. `find_duplicates(items: List[Any]) -> List[Any]`
Finds duplicate items in a list.

**Examples:**
```python
find_duplicates([1, 2, 2, 3, 4, 4, 5])  # [2, 4]
find_duplicates(['a', 'b', 'a', 'c'])   # ['a']
```

### 5. `format_currency(amount: float, currency: str = "USD") -> str`
Formats a number as a currency string.

**Examples:**
```python
format_currency(1234.56)           # "$1,234.56"
format_currency(1000, "EUR")       # "€1,000.00"
```

### 6. `is_palindrome(text: str) -> bool`
Checks if a string is a palindrome.

**Examples:**
```python
is_palindrome("racecar")                    # True
is_palindrome("A man a plan a canal Panama") # True
is_palindrome("hello")                      # False
```

### 7. `merge_dictionaries(dict1: Dict, dict2: Dict) -> Dict`
Merges two dictionaries with dict2 values taking precedence.

**Examples:**
```python
merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
# {'a': 1, 'b': 3, 'c': 4}
```

### 8. `calculate_statistics(numbers: List[float]) -> Dict[str, float]`
Calculates basic statistics for a list of numbers.

**Examples:**
```python
calculate_statistics([1, 2, 3, 4, 5])
# {'mean': 3.0, 'median': 3.0, 'min': 1.0, 'max': 5.0}
```

### 9. `validate_phone_number(phone: str) -> bool`
Validates if a string is a properly formatted phone number.

**Examples:**
```python
validate_phone_number("+1-555-123-4567")  # True
validate_phone_number("555-123-4567")     # True
validate_phone_number("invalid")          # False
```

### 10. `convert_temperature(value: float, from_unit: str, to_unit: str) -> float`
Converts temperature between different units (Celsius, Fahrenheit, Kelvin).

**Examples:**
```python
convert_temperature(32, 'F', 'C')   # 0.0
convert_temperature(100, 'C', 'F')  # 212.0
```

## Testing

### Running Tests

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run all tests:**
   ```bash
   pytest
   ```

3. **Run tests with coverage:**
   ```bash
   pytest --cov=src --cov-report=html
   ```

4. **Run specific test classes:**
   ```bash
   pytest tests/test_utils.py::TestValidateEmail
   ```

5. **Run specific test methods:**
   ```bash
   pytest tests/test_utils.py::TestValidateEmail::test_valid_emails
   ```

6. **Run parametrized tests:**
   ```bash
   pytest tests/test_utils.py::test_validate_email_parametrized
   ```

### Test Structure

The test suite includes:

- **Class-based tests** for each function with multiple test methods
- **Parametrized tests** for comprehensive input coverage
- **Edge case testing** (empty inputs, boundary values)
- **Error condition testing** (invalid inputs, exceptions)
- **Type checking** for all functions

### Test Coverage

Each function is tested for:
- ✅ Normal/expected inputs
- ✅ Edge cases (empty, single element, etc.)
- ✅ Invalid inputs (wrong types, out of range)
- ✅ Error conditions and exceptions
- ✅ Multiple input variations

## Code Quality Features

### Function Design Principles

1. **Type Hints**: All functions use proper type annotations
2. **Documentation**: Comprehensive docstrings with examples
3. **Input Validation**: Proper validation of input parameters
4. **Error Handling**: Appropriate exceptions for invalid inputs
5. **Single Responsibility**: Each function has one clear purpose

### Testing Best Practices

1. **Test Organization**: Logical grouping of related tests
2. **Descriptive Names**: Clear test method names
3. **Comprehensive Coverage**: Tests for all code paths
4. **Parametrized Tests**: Efficient testing of multiple inputs
5. **Edge Case Testing**: Boundary conditions and error cases

## Development Workflow

1. **Write the function** in `src/utils.py`
2. **Add comprehensive tests** in `tests/test_utils.py`
3. **Run tests** to ensure everything works
4. **Check coverage** to identify untested code
5. **Refactor** if needed based on test results

## Dependencies

- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **pytest-mock**: Mocking utilities
- **black**: Code formatting
- **flake8**: Linting

## GitHub Actions Integration

This project is set up to work with GitHub Actions CI/CD. The existing workflow in `.github/workflows/hello.yml` can be extended to run tests automatically on every push.

Example workflow addition:
```yaml
- name: Run tests
  run: |
    pip install -r requirements.txt
    pytest --cov=src --cov-report=xml
```

This structured approach ensures maintainable, testable, and reliable code that can be easily extended and modified. 