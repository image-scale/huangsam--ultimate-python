"""Tests for MRO and mixin modules."""

from pyguide.advanced.mro import main as mro_main, A, B, C, D, E
from pyguide.advanced.mixins import (
    main as mixins_main,
    JSONMixin,
    ComparableMixin,
    LoggingMixin,
    SerializablePerson,
    ComparablePerson,
)


class TestMROModule:
    """Tests for the MRO demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        mro_main()

    def test_simple_mro(self):
        """Simple inheritance should have expected MRO."""
        assert B.__mro__ == (B, A, object)

    def test_diamond_mro(self):
        """Diamond inheritance should use C3 linearization."""
        assert D.__mro__ == (D, B, C, A, object)

    def test_reversed_parents_mro(self):
        """Reversed parents should give different MRO."""
        assert E.__mro__ == (E, C, B, A, object)

    def test_method_resolution(self):
        """Method should resolve according to MRO."""
        d = D()
        assert d.greet() == "Hello from B"


class TestMixinsModule:
    """Tests for the mixins demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        mixins_main()

    def test_json_mixin(self):
        """JSONMixin should add to_json method."""
        person = SerializablePerson("Test", 25)
        json = person.to_json()
        assert '"name": "Test"' in json

    def test_comparable_mixin(self):
        """ComparableMixin should add comparison operators."""
        p1 = ComparablePerson("A", 20)
        p2 = ComparablePerson("B", 30)
        assert p1 < p2
        assert p2 > p1

    def test_logging_mixin(self):
        """LoggingMixin should add logging capability."""
        LoggingMixin.clear_logs()

        class TestClass(LoggingMixin):
            pass

        obj = TestClass()
        obj.log("test message")
        logs = LoggingMixin.get_logs()
        assert len(logs) == 1
        assert "test message" in logs[0]
