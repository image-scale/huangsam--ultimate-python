"""Tests for dict union and heap modules."""

import heapq

from pyguide.data_structures.dict_union import main as dict_union_main
from pyguide.data_structures.heaps import main as heaps_main


class TestDictUnionModule:
    """Tests for the dict union demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        dict_union_main()

    def test_union_operator(self):
        """| should merge dictionaries."""
        d1 = {'a': 1}
        d2 = {'b': 2}
        assert (d1 | d2) == {'a': 1, 'b': 2}

    def test_union_right_wins(self):
        """Right dict values should override left."""
        d1 = {'a': 1}
        d2 = {'a': 2}
        assert (d1 | d2) == {'a': 2}

    def test_inplace_union(self):
        """|= should modify dict in place."""
        d = {'a': 1}
        d |= {'b': 2}
        assert d == {'a': 1, 'b': 2}


class TestHeapsModule:
    """Tests for the heaps demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        heaps_main()

    def test_heappush_heappop(self):
        """heappush/heappop should maintain min-heap."""
        heap = []
        heapq.heappush(heap, 3)
        heapq.heappush(heap, 1)
        heapq.heappush(heap, 2)
        assert heapq.heappop(heap) == 1

    def test_heapify(self):
        """heapify should convert list to heap."""
        nums = [3, 1, 4, 1, 5]
        heapq.heapify(nums)
        assert nums[0] == 1

    def test_nlargest_nsmallest(self):
        """nlargest/nsmallest should return top n."""
        nums = [3, 1, 4, 1, 5, 9, 2, 6]
        assert heapq.nlargest(3, nums) == [9, 6, 5]
        assert heapq.nsmallest(3, nums) == [1, 1, 2]
