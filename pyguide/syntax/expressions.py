"""
Demonstration of Python expressions and arithmetic operations.

Expressions combine values and operators to produce new values.
Python supports standard arithmetic operations on numeric types.
"""

import math


def main() -> None:
    # Basic arithmetic with integers
    a = 10
    b = 3

    # Addition and subtraction
    assert a + b == 13
    assert a - b == 7

    # Multiplication
    assert a * b == 30

    # Division always returns a float in Python 3
    result = a / b
    assert isinstance(result, float)
    assert math.isclose(result, 3.3333333333333335)

    # Integer division (floor division) returns an integer
    floor_result = a // b
    assert floor_result == 3
    assert isinstance(floor_result, int)

    # Modulo gives the remainder
    remainder = a % b
    assert remainder == 1

    # Exponentiation
    power = 2 ** 10
    assert power == 1024

    # Negative exponents give floats
    neg_power = 2 ** -1
    assert math.isclose(neg_power, 0.5)

    # Expressions can be chained
    chained = 2 + 3 * 4
    assert chained == 14  # multiplication before addition

    # Parentheses control order of operations
    grouped = (2 + 3) * 4
    assert grouped == 20

    # More complex expression chains
    complex_expr = 1 + 2 * 3 ** 2
    assert complex_expr == 19  # exponent first, then multiply, then add

    # Unary operators
    negative = -5
    positive = +5
    assert negative == -5
    assert positive == 5

    # Division edge cases
    assert 5 / 2 == 2.5
    assert 5 // 2 == 2
    assert -5 // 2 == -3  # floor division rounds toward negative infinity

    # Built-in math functions
    assert abs(-42) == 42
    assert pow(2, 3) == 8
    assert round(3.7) == 4
    assert round(3.14159, 2) == 3.14


if __name__ == "__main__":
    main()
