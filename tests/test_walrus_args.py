"""Tests for walrus operator and argument enforcement modules."""

from pyguide.syntax.walrus import main as walrus_main
from pyguide.syntax.arg_enforcement import (
    main as arg_main,
    positional_only,
    keyword_only,
    mixed_parameters,
    with_defaults,
)


class TestWalrusModule:
    """Tests for the walrus operator demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        walrus_main()

    def test_walrus_in_if(self):
        """Walrus operator should work in if statements."""
        if (n := 10) > 5:
            result = n
        assert result == 10

    def test_walrus_in_comprehension(self):
        """Walrus operator should work in list comprehensions."""
        results = [(x, sq) for x in [2, 3, 4] if (sq := x**2) > 5]
        assert results == [(3, 9), (4, 16)]

    def test_walrus_assigns_and_returns(self):
        """Walrus operator should both assign and return value."""
        assert (x := 42) == 42
        assert x == 42


class TestArgEnforcementModule:
    """Tests for the argument enforcement demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        arg_main()

    def test_positional_only(self):
        """Positional-only parameters must be passed positionally."""
        assert positional_only(3, 5) == 8

    def test_keyword_only(self):
        """Keyword-only parameters must be passed as keywords."""
        assert keyword_only(x=3, y=5) == 8
        assert keyword_only(y=5, x=3) == 8  # order doesn't matter

    def test_mixed_parameters(self):
        """Mixed parameters should handle all argument types."""
        assert mixed_parameters(1, 2, kw_only=3) == "pos=1, reg=2, kw=3"
        assert mixed_parameters(1, regular=2, kw_only=3) == "pos=1, reg=2, kw=3"

    def test_with_defaults(self):
        """Default values should work with parameter types."""
        assert with_defaults(5) == 35
        assert with_defaults(5, 15) == 40
        assert with_defaults(5, z=25) == 40
        assert with_defaults(5, 15, z=25) == 45

    def test_positional_only_rejects_keywords(self):
        """Positional-only should reject keyword arguments."""
        import pytest
        with pytest.raises(TypeError):
            positional_only(x=3, y=5)

    def test_keyword_only_rejects_positional(self):
        """Keyword-only should reject positional arguments."""
        import pytest
        with pytest.raises(TypeError):
            keyword_only(3, 5)
