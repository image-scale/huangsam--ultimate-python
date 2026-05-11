"""Tests for list and tuple data structure modules."""

from pyguide.data_structures.lists import main as lists_main
from pyguide.data_structures.tuples import main as tuples_main


class TestListsModule:
    """Tests for the lists demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        lists_main()

    def test_list_indexing(self):
        """List indexing should work correctly."""
        items = [1, 2, 3, 4, 5]
        assert items[0] == 1
        assert items[-1] == 5

    def test_list_slicing(self):
        """List slicing should work correctly."""
        items = [0, 1, 2, 3, 4]
        assert items[1:4] == [1, 2, 3]
        assert items[::2] == [0, 2, 4]
        assert items[::-1] == [4, 3, 2, 1, 0]

    def test_list_mutability(self):
        """Lists should be mutable."""
        items = [1, 2, 3]
        items[0] = 10
        assert items == [10, 2, 3]

    def test_list_append(self):
        """append should add to end of list."""
        items = [1, 2]
        items.append(3)
        assert items == [1, 2, 3]

    def test_list_extend(self):
        """extend should add multiple items."""
        items = [1, 2]
        items.extend([3, 4])
        assert items == [1, 2, 3, 4]

    def test_list_sort(self):
        """sort should sort in place."""
        items = [3, 1, 2]
        items.sort()
        assert items == [1, 2, 3]

    def test_list_reverse(self):
        """reverse should reverse in place."""
        items = [1, 2, 3]
        items.reverse()
        assert items == [3, 2, 1]

    def test_list_membership(self):
        """Membership testing should work."""
        items = [1, 2, 3]
        assert 2 in items
        assert 5 not in items


class TestTuplesModule:
    """Tests for the tuples demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        tuples_main()

    def test_tuple_indexing(self):
        """Tuple indexing should work correctly."""
        items = (1, 2, 3, 4, 5)
        assert items[0] == 1
        assert items[-1] == 5

    def test_tuple_slicing(self):
        """Tuple slicing should work correctly."""
        items = (0, 1, 2, 3, 4)
        assert items[1:4] == (1, 2, 3)
        assert items[::2] == (0, 2, 4)

    def test_tuple_immutability(self):
        """Tuples should be immutable."""
        items = (1, 2, 3)
        try:
            items[0] = 10
            assert False, "Should have raised TypeError"
        except TypeError:
            pass

    def test_tuple_unpacking(self):
        """Tuple unpacking should work correctly."""
        x, y, z = (1, 2, 3)
        assert x == 1
        assert y == 2
        assert z == 3

    def test_tuple_single_element(self):
        """Single element tuple needs trailing comma."""
        single = (42,)
        assert isinstance(single, tuple)
        not_tuple = (42)
        assert isinstance(not_tuple, int)

    def test_tuple_as_dict_key(self):
        """Tuples can be used as dict keys."""
        d = {(1, 2): "value"}
        assert d[(1, 2)] == "value"

    def test_tuple_comparison(self):
        """Tuple comparison should be lexicographic."""
        assert (1, 2) < (1, 3)
        assert (1, 2) < (2, 0)

    def test_tuple_concatenation(self):
        """Tuple concatenation should work."""
        assert (1, 2) + (3, 4) == (1, 2, 3, 4)
