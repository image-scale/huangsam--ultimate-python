"""Tests for defaultdict and itertools modules."""

from collections import defaultdict
import itertools

from pyguide.data_structures.defaultdicts import main as defaultdicts_main
from pyguide.data_structures.itertoolsmod import main as itertools_main


class TestDefaultdictsModule:
    """Tests for the defaultdicts demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        defaultdicts_main()

    def test_defaultdict_int(self):
        """defaultdict(int) should return 0 for missing keys."""
        dd = defaultdict(int)
        assert dd['missing'] == 0

    def test_defaultdict_list(self):
        """defaultdict(list) should return [] for missing keys."""
        dd = defaultdict(list)
        dd['items'].append(1)
        assert dd['items'] == [1]

    def test_counting_pattern(self):
        """defaultdict should enable easy counting."""
        dd = defaultdict(int)
        for x in ['a', 'b', 'a']:
            dd[x] += 1
        assert dd['a'] == 2
        assert dd['b'] == 1


class TestItertoolsModule:
    """Tests for the itertools demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        itertools_main()

    def test_count(self):
        """count should generate infinite sequence."""
        counter = itertools.count(5)
        assert next(counter) == 5
        assert next(counter) == 6

    def test_chain(self):
        """chain should combine iterables."""
        result = list(itertools.chain([1, 2], [3, 4]))
        assert result == [1, 2, 3, 4]

    def test_islice(self):
        """islice should slice iterators."""
        result = list(itertools.islice(range(10), 3))
        assert result == [0, 1, 2]

    def test_permutations(self):
        """permutations should generate all orderings."""
        perms = list(itertools.permutations([1, 2], 2))
        assert perms == [(1, 2), (2, 1)]

    def test_combinations(self):
        """combinations should generate subsets."""
        combs = list(itertools.combinations([1, 2, 3], 2))
        assert combs == [(1, 2), (1, 3), (2, 3)]
