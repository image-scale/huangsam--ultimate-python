"""
Demonstration of Python decorators.

Decorators modify or extend the behavior of functions or classes
at runtime using the @decorator syntax.
"""

from functools import wraps
from typing import Callable, Any


def simple_logger(func: Callable) -> Callable:
    """Simple decorator that logs function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    wrapper.call_count = 0
    return wrapper


def call_counter(func: Callable) -> Callable:
    """Decorator that counts how many times a function is called."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


def repeat(times: int) -> Callable:
    """Decorator factory that repeats function execution."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


def validate_positive(func: Callable) -> Callable:
    """Decorator that validates all numeric args are positive."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Arguments must be positive")
        for value in kwargs.values():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError("Arguments must be positive")
        return func(*args, **kwargs)
    return wrapper


def with_prefix(prefix: str) -> Callable:
    """Decorator factory that adds prefix to return value."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{prefix}{result}"
        return wrapper
    return decorator


def main() -> None:
    # Simple decorator
    @simple_logger
    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    assert add.__name__ == "add"  # wraps preserves name

    # Call counter decorator
    @call_counter
    def multiply(a, b):
        return a * b

    assert multiply(2, 3) == 6
    assert multiply.count == 1
    multiply(4, 5)
    assert multiply.count == 2

    # Decorator with arguments
    @repeat(3)
    def greet(name):
        return f"Hello, {name}!"

    result = greet("Alice")
    assert result == ["Hello, Alice!", "Hello, Alice!", "Hello, Alice!"]

    # Validation decorator
    @validate_positive
    def square_root(n):
        return n ** 0.5

    assert square_root(16) == 4.0
    try:
        square_root(-1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    # Decorator factory with prefix
    @with_prefix("Result: ")
    def compute(x):
        return x * 10

    assert compute(5) == "Result: 50"

    # Stacking decorators (applied bottom-up)
    @call_counter
    @validate_positive
    def safe_divide(a, b):
        return a / b

    assert safe_divide(10, 2) == 5
    assert safe_divide.count == 1

    # Class as decorator
    class Timer:
        def __init__(self, func):
            self.func = func
            wraps(func)(self)

        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs)

    @Timer
    def slow_function():
        return "done"

    assert slow_function() == "done"


if __name__ == "__main__":
    main()
