"""Tests for function syntax module."""

from pyguide.syntax.functions import (
    main as functions_main,
    add_numbers,
    greet,
    calculate_sum,
    create_multiplier,
    apply_to_all,
)


class TestFunctionsModule:
    """Tests for the functions demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        functions_main()

    def test_add_numbers(self):
        """add_numbers should add two numbers."""
        assert add_numbers(3, 5) == 8
        assert add_numbers(0, 0) == 0
        assert add_numbers(-1, 1) == 0

    def test_greet_with_default(self):
        """greet should use default greeting."""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_with_custom_greeting(self):
        """greet should accept custom greeting."""
        assert greet("Bob", "Hi") == "Hi, Bob!"

    def test_lambda_functions(self):
        """Lambda functions should work as expected."""
        square = lambda x: x ** 2
        assert square(4) == 16

    def test_higher_order_function(self):
        """Higher-order functions should accept function arguments."""
        result = calculate_sum(lambda i: i * 2, 5)
        assert result == 20  # 0 + 2 + 4 + 6 + 8

    def test_function_returning_function(self):
        """Functions can return other functions."""
        double = create_multiplier(2)
        assert double(5) == 10
        triple = create_multiplier(3)
        assert triple(5) == 15

    def test_apply_to_all(self):
        """apply_to_all should apply function to each item."""
        result = apply_to_all(lambda x: x + 1, [1, 2, 3])
        assert result == [2, 3, 4]

    def test_map_builtin(self):
        """Built-in map should apply function to sequence."""
        result = list(map(lambda x: x * 2, [1, 2, 3]))
        assert result == [2, 4, 6]

    def test_filter_builtin(self):
        """Built-in filter should keep matching elements."""
        result = list(filter(lambda x: x > 2, [1, 2, 3, 4]))
        assert result == [3, 4]

    def test_function_has_name(self):
        """Functions have __name__ attribute."""
        assert add_numbers.__name__ == "add_numbers"

    def test_function_has_docstring(self):
        """Functions have __doc__ attribute."""
        assert "Add two numbers" in add_numbers.__doc__
