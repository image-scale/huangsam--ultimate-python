"""Tests for variable and expression syntax modules."""

import math

from pyguide.syntax.variables import main as variables_main
from pyguide.syntax.expressions import main as expressions_main


class TestVariablesModule:
    """Tests for the variables demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        variables_main()

    def test_integer_types(self):
        """Integers should have type int."""
        val = 42
        assert type(val) is int
        assert isinstance(val, object)

    def test_float_types(self):
        """Floats should have type float."""
        val = 3.14
        assert type(val) is float
        assert isinstance(val, object)

    def test_boolean_types(self):
        """Booleans should have type bool and be instances of int."""
        val = True
        assert type(val) is bool
        assert isinstance(val, int)

    def test_string_types(self):
        """Strings should have type str."""
        val = "hello"
        assert type(val) is str
        assert isinstance(val, object)

    def test_number_bases(self):
        """Integers can be expressed in different bases."""
        decimal = 255
        hexadecimal = 0xFF
        octal = 0o377
        binary = 0b11111111
        assert decimal == hexadecimal == octal == binary

    def test_underscores_in_numbers(self):
        """Underscores can be used in numeric literals."""
        big_num = 1_000_000
        assert big_num == 1000000

    def test_none_type(self):
        """None has its own type NoneType."""
        val = None
        assert type(val) is type(None)


class TestExpressionsModule:
    """Tests for the expressions demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        expressions_main()

    def test_addition(self):
        """Addition should work correctly."""
        assert 10 + 3 == 13

    def test_subtraction(self):
        """Subtraction should work correctly."""
        assert 10 - 3 == 7

    def test_multiplication(self):
        """Multiplication should work correctly."""
        assert 10 * 3 == 30

    def test_division_returns_float(self):
        """Division always returns a float."""
        result = 10 / 3
        assert isinstance(result, float)

    def test_floor_division(self):
        """Floor division returns an integer."""
        result = 10 // 3
        assert result == 3
        assert isinstance(result, int)

    def test_modulo(self):
        """Modulo returns the remainder."""
        assert 10 % 3 == 1

    def test_exponentiation(self):
        """Exponentiation raises to a power."""
        assert 2 ** 10 == 1024

    def test_operator_precedence(self):
        """Operators follow precedence rules."""
        assert 2 + 3 * 4 == 14
        assert (2 + 3) * 4 == 20

    def test_negative_floor_division(self):
        """Negative floor division rounds toward negative infinity."""
        assert -5 // 2 == -3
