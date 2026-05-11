"""Tests for comprehensions module."""

from pyguide.data_structures.comprehensions import main as comp_main


class TestComprehensionsModule:
    """Tests for the comprehensions demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        comp_main()

    def test_list_comprehension_basic(self):
        """Basic list comprehension should transform elements."""
        squares = [x ** 2 for x in range(5)]
        assert squares == [0, 1, 4, 9, 16]

    def test_list_comprehension_filter(self):
        """List comprehension with condition should filter."""
        evens = [x for x in range(10) if x % 2 == 0]
        assert evens == [0, 2, 4, 6, 8]

    def test_list_comprehension_nested(self):
        """Nested list comprehension should flatten."""
        matrix = [[1, 2], [3, 4]]
        flat = [x for row in matrix for x in row]
        assert flat == [1, 2, 3, 4]

    def test_set_comprehension(self):
        """Set comprehension should remove duplicates."""
        chars = {c for c in "hello"}
        assert chars == {'h', 'e', 'l', 'o'}

    def test_dict_comprehension(self):
        """Dict comprehension should create key-value pairs."""
        d = {x: x ** 2 for x in range(3)}
        assert d == {0: 0, 1: 1, 2: 4}

    def test_dict_comprehension_swap(self):
        """Dict comprehension can swap keys and values."""
        original = {'a': 1, 'b': 2}
        swapped = {v: k for k, v in original.items()}
        assert swapped == {1: 'a', 2: 'b'}

    def test_tuple_from_generator(self):
        """Generator expression wrapped in tuple()."""
        t = tuple(x ** 2 for x in range(3))
        assert t == (0, 1, 4)

    def test_comprehension_with_ternary(self):
        """Comprehension with if-else expression."""
        labels = ['even' if x % 2 == 0 else 'odd' for x in range(3)]
        assert labels == ['even', 'odd', 'even']
