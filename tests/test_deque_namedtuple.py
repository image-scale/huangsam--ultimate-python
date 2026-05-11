"""Tests for deque and namedtuple modules."""

from collections import deque, namedtuple

from pyguide.data_structures.deques import main as deques_main
from pyguide.data_structures.namedtuples import main as namedtuples_main


class TestDequesModule:
    """Tests for the deques demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        deques_main()

    def test_deque_append_pop(self):
        """Deque should support append and pop on both ends."""
        d = deque([1, 2, 3])
        d.append(4)
        assert d.pop() == 4
        d.appendleft(0)
        assert d.popleft() == 0

    def test_deque_maxlen(self):
        """Deque with maxlen should discard old items."""
        d = deque([1, 2, 3], maxlen=3)
        d.append(4)
        assert list(d) == [2, 3, 4]

    def test_deque_rotate(self):
        """Rotate should move elements."""
        d = deque([1, 2, 3, 4])
        d.rotate(1)
        assert list(d) == [4, 1, 2, 3]


class TestNamedtuplesModule:
    """Tests for the namedtuples demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        namedtuples_main()

    def test_namedtuple_creation(self):
        """Named tuples should have named fields."""
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(3, 4)
        assert p.x == 3
        assert p.y == 4

    def test_namedtuple_indexing(self):
        """Named tuples should support indexing."""
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(3, 4)
        assert p[0] == 3
        assert p[1] == 4

    def test_namedtuple_immutability(self):
        """Named tuples should be immutable."""
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(3, 4)
        try:
            p.x = 10
            assert False
        except AttributeError:
            pass

    def test_namedtuple_asdict(self):
        """_asdict should convert to dict."""
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(3, 4)
        assert p._asdict() == {'x': 3, 'y': 4}
