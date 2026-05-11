"""Tests for conditional and loop syntax modules."""

from pyguide.syntax.conditionals import main as conditionals_main
from pyguide.syntax.loops import main as loops_main


class TestConditionalsModule:
    """Tests for the conditionals demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        conditionals_main()

    def test_if_statement(self):
        """If statement should evaluate condition correctly."""
        x = 10
        if x > 5:
            result = "greater"
        else:
            result = "not greater"
        assert result == "greater"

    def test_if_elif_else(self):
        """If-elif-else chain should select correct branch."""
        score = 85
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        else:
            grade = "C"
        assert grade == "B"

    def test_comparison_operators(self):
        """Comparison operators should work correctly."""
        assert (5 == 5) is True
        assert (5 != 10) is True
        assert (5 < 10) is True
        assert (10 > 5) is True
        assert (5 <= 5) is True
        assert (5 >= 5) is True

    def test_logical_operators(self):
        """Logical operators should combine conditions correctly."""
        assert (True and True) is True
        assert (True and False) is False
        assert (True or False) is True
        assert (not False) is True

    def test_chained_comparisons(self):
        """Chained comparisons should work correctly."""
        x = 5
        assert 1 < x < 10
        assert 0 <= x <= 5

    def test_ternary_operator(self):
        """Conditional expression should return correct value."""
        age = 21
        status = "adult" if age >= 18 else "minor"
        assert status == "adult"


class TestLoopsModule:
    """Tests for the loops demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        loops_main()

    def test_for_with_range(self):
        """For loop with range should iterate correctly."""
        total = 0
        for i in range(5):
            total += i
        assert total == 10

    def test_for_over_list(self):
        """For loop should iterate over list elements."""
        items = ["a", "b", "c"]
        result = []
        for item in items:
            result.append(item)
        assert result == ["a", "b", "c"]

    def test_while_loop(self):
        """While loop should repeat until condition is false."""
        count = 0
        while count < 5:
            count += 1
        assert count == 5

    def test_break_statement(self):
        """Break should exit loop early."""
        for i in range(10):
            if i == 5:
                break
        assert i == 5

    def test_continue_statement(self):
        """Continue should skip to next iteration."""
        evens = []
        for i in range(6):
            if i % 2 != 0:
                continue
            evens.append(i)
        assert evens == [0, 2, 4]

    def test_enumerate(self):
        """Enumerate should provide index and value."""
        items = ["a", "b"]
        result = list(enumerate(items))
        assert result == [(0, "a"), (1, "b")]

    def test_zip(self):
        """Zip should pair elements from multiple sequences."""
        nums = [1, 2]
        chars = ["a", "b"]
        result = list(zip(nums, chars))
        assert result == [(1, "a"), (2, "b")]
