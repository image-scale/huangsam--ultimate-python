"""
Demonstration of Python variables and literal types.

Variables store values in named references that can be used throughout a program.
Python supports multiple literal types including integers, floats, booleans, and strings.
"""

import math


def main() -> None:
    # Python has several fundamental literal types
    integer_val = 42
    float_val = 3.14
    boolean_val = True
    string_val = "hello"

    # Each variable has a type that can be checked with type()
    assert type(integer_val) is int
    assert type(float_val) is float
    assert type(boolean_val) is bool
    assert type(string_val) is str

    # Everything in Python is an object, including the types themselves
    assert isinstance(integer_val, object)
    assert isinstance(int, object)
    assert isinstance(float_val, object)
    assert isinstance(float, object)
    assert isinstance(boolean_val, object)
    assert isinstance(bool, object)
    assert isinstance(string_val, object)
    assert isinstance(str, object)

    # Integers can be represented in different number bases
    decimal_num = 255
    hexadecimal_num = 0xFF
    octal_num = 0o377
    binary_num = 0b11111111

    assert decimal_num == hexadecimal_num == octal_num == binary_num
    assert decimal_num == 255

    # Underscores can be used to separate digit groups for readability
    large_number = 1_000_000
    assert large_number == 1000000

    hex_with_underscores = 0xAB_CD
    assert hex_with_underscores == 43981

    float_with_underscores = 1_234.567_89
    assert math.isclose(float_with_underscores, 1234.56789)

    # Scientific notation for floats
    scientific = 2.5e3
    assert math.isclose(scientific, 2500.0)

    # None represents the absence of a value
    empty_val = None
    assert type(empty_val) is type(None)
    assert isinstance(empty_val, object)

    # Boolean is a subclass of int in Python
    assert isinstance(True, int)
    assert True == 1
    assert False == 0


if __name__ == "__main__":
    main()
