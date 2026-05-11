"""Tests for set and dict data structure modules."""

from pyguide.data_structures.sets import main as sets_main
from pyguide.data_structures.dicts import main as dicts_main


class TestSetsModule:
    """Tests for the sets demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        sets_main()

    def test_set_uniqueness(self):
        """Sets should contain only unique elements."""
        s = {1, 1, 2, 2, 3}
        assert s == {1, 2, 3}

    def test_set_add(self):
        """add should add element to set."""
        s = {1, 2}
        s.add(3)
        assert s == {1, 2, 3}

    def test_set_union(self):
        """Union should combine sets."""
        assert {1, 2} | {2, 3} == {1, 2, 3}

    def test_set_intersection(self):
        """Intersection should find common elements."""
        assert {1, 2, 3} & {2, 3, 4} == {2, 3}

    def test_set_difference(self):
        """Difference should find elements in first but not second."""
        assert {1, 2, 3} - {2, 3} == {1}

    def test_set_symmetric_difference(self):
        """Symmetric difference should find elements in either but not both."""
        assert {1, 2, 3} ^ {2, 3, 4} == {1, 4}

    def test_subset(self):
        """Subset should check containment."""
        assert {1, 2}.issubset({1, 2, 3})
        assert {1, 2} <= {1, 2, 3}

    def test_membership(self):
        """Membership testing should work."""
        s = {1, 2, 3}
        assert 2 in s
        assert 5 not in s


class TestDictsModule:
    """Tests for the dicts demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        dicts_main()

    def test_dict_access(self):
        """Dictionary access should work correctly."""
        d = {'a': 1, 'b': 2}
        assert d['a'] == 1

    def test_dict_get_with_default(self):
        """get should return default for missing key."""
        d = {'a': 1}
        assert d.get('b', 'default') == 'default'

    def test_dict_set_value(self):
        """Setting values should work."""
        d = {}
        d['key'] = 'value'
        assert d['key'] == 'value'

    def test_dict_delete(self):
        """Deleting keys should work."""
        d = {'a': 1, 'b': 2}
        del d['a']
        assert 'a' not in d

    def test_dict_pop(self):
        """pop should remove and return value."""
        d = {'a': 1}
        val = d.pop('a')
        assert val == 1
        assert 'a' not in d

    def test_dict_update(self):
        """update should merge dictionaries."""
        d = {'a': 1}
        d.update({'b': 2})
        assert d == {'a': 1, 'b': 2}

    def test_dict_keys_values_items(self):
        """keys, values, items should work."""
        d = {'a': 1, 'b': 2}
        assert set(d.keys()) == {'a', 'b'}
        assert set(d.values()) == {1, 2}
        assert set(d.items()) == {('a', 1), ('b', 2)}

    def test_dict_membership(self):
        """Membership testing should check keys."""
        d = {'a': 1, 'b': 2}
        assert 'a' in d
        assert 'c' not in d
