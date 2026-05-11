"""
Demonstration of Python functions.

Functions allow code to be organized into reusable blocks. Python supports
regular functions with def, anonymous functions with lambda, and
higher-order functions that accept or return other functions.
"""

from typing import Any, Callable


def add_numbers(x: int, y: int) -> int:
    """Add two numbers together."""
    return x + y


def greet(name: str, greeting: str = "Hello") -> str:
    """Greet a person with a customizable greeting."""
    return f"{greeting}, {name}!"


def calculate_sum(fn: Callable[[int], int], n: int) -> int:
    """Apply a function to each number from 0 to n-1 and sum the results."""
    total = 0
    for i in range(n):
        total += fn(i)
    return total


def create_multiplier(factor: int) -> Callable[[int], int]:
    """Create a function that multiplies by a fixed factor."""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier


def apply_to_all(fn: Callable[[Any], Any], items: list) -> list:
    """Apply a function to all items in a list."""
    return [fn(item) for item in items]


def no_return_value() -> None:
    """Function that returns None implicitly."""
    pass


def main() -> None:
    # Basic function with positional arguments
    result = add_numbers(3, 5)
    assert result == 8

    # Function with default argument
    greeting1 = greet("Alice")
    assert greeting1 == "Hello, Alice!"

    greeting2 = greet("Bob", "Hi")
    assert greeting2 == "Hi, Bob!"

    # Keyword arguments allow any order
    greeting3 = greet(greeting="Howdy", name="Charlie")
    assert greeting3 == "Howdy, Charlie!"

    # Lambda functions - anonymous single-expression functions
    square = lambda x: x ** 2
    assert square(4) == 16

    # Lambda with multiple parameters
    multiply = lambda a, b: a * b
    assert multiply(3, 4) == 12

    # Higher-order function with lambda
    sum_of_squares = calculate_sum(lambda i: i ** 2, 5)
    assert sum_of_squares == 30  # 0 + 1 + 4 + 9 + 16

    # Function that returns a function (closure)
    double = create_multiplier(2)
    triple = create_multiplier(3)
    assert double(5) == 10
    assert triple(5) == 15

    # The closure captures the factor value
    assert double(7) == 14
    assert triple(7) == 21

    # Applying functions to collections
    numbers = [1, 2, 3, 4, 5]
    squared = apply_to_all(lambda x: x ** 2, numbers)
    assert squared == [1, 4, 9, 16, 25]

    # Built-in higher-order functions
    # map - apply function to each element
    doubled = list(map(lambda x: x * 2, numbers))
    assert doubled == [2, 4, 6, 8, 10]

    # filter - keep elements that satisfy a predicate
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    assert evens == [2, 4]

    # Functions are objects - they have attributes
    assert add_numbers.__name__ == "add_numbers"
    assert "Add two numbers" in add_numbers.__doc__

    # Functions without explicit return give None
    result = no_return_value()
    assert result is None

    # *args for variable positional arguments
    def sum_all(*args):
        return sum(args)

    assert sum_all(1, 2, 3) == 6
    assert sum_all(1, 2, 3, 4, 5) == 15

    # **kwargs for variable keyword arguments
    def describe(**kwargs):
        return {k: v for k, v in kwargs.items()}

    result = describe(name="Alice", age=30)
    assert result == {"name": "Alice", "age": 30}

    # Combining *args and **kwargs
    def flexible_func(*args, **kwargs):
        return (len(args), len(kwargs))

    assert flexible_func(1, 2, 3, x=10, y=20) == (3, 2)


if __name__ == "__main__":
    main()
