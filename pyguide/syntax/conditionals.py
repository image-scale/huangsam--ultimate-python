"""
Demonstration of Python conditional statements.

Conditional statements allow code to make decisions based on conditions.
Python uses if, elif, and else keywords for branching logic.
"""


def main() -> None:
    # Simple if statement
    x = 10
    if x > 5:
        result = "greater"
    else:
        result = "not greater"
    assert result == "greater"

    # If-else statement
    temperature = 72
    if temperature > 80:
        weather = "hot"
    else:
        weather = "not hot"
    assert weather == "not hot"

    # If-elif-else chain for multiple conditions
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    assert grade == "B"

    # Comparison operators
    a, b = 5, 10
    assert (a == b) is False   # equal
    assert (a != b) is True    # not equal
    assert (a < b) is True     # less than
    assert (a > b) is False    # greater than
    assert (a <= b) is True    # less than or equal
    assert (a >= b) is False   # greater than or equal

    # Chained comparisons
    x = 5
    assert 1 < x < 10
    assert 0 <= x <= 5
    assert not (10 < x < 20)

    # Logical operators: and, or, not
    is_sunny = True
    is_warm = True
    assert (is_sunny and is_warm) is True
    assert (is_sunny or is_warm) is True
    assert (not is_sunny) is False

    # Short-circuit evaluation
    x = 0
    # This won't cause division by zero because of short-circuit
    if x != 0 and (10 / x) > 1:
        result = "positive"
    else:
        result = "not applicable"
    assert result == "not applicable"

    # Truthy and falsy values
    assert bool([]) is False       # empty list is falsy
    assert bool([1, 2]) is True    # non-empty list is truthy
    assert bool("") is False       # empty string is falsy
    assert bool("hello") is True   # non-empty string is truthy
    assert bool(0) is False        # zero is falsy
    assert bool(42) is True        # non-zero is truthy
    assert bool(None) is False     # None is falsy

    # Conditional expression (ternary operator)
    age = 21
    status = "adult" if age >= 18 else "minor"
    assert status == "adult"

    # Identity comparison with is and is not
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    assert a is b      # same object
    assert a is not c  # different objects (even if equal)
    assert a == c      # equal values

    # Membership testing with in
    fruits = ["apple", "banana", "cherry"]
    assert "banana" in fruits
    assert "grape" not in fruits


if __name__ == "__main__":
    main()
