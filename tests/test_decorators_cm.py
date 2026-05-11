"""Tests for decorator and context manager modules."""

from io import StringIO

from pyguide.advanced.decorators import (
    main as decorators_main,
    call_counter,
    validate_positive,
    repeat,
)
from pyguide.advanced.context_managers import (
    main as cm_main,
    FileHandler,
    SuppressErrors,
    temp_value,
)


class TestDecoratorsModule:
    """Tests for the decorators demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        decorators_main()

    def test_call_counter(self):
        """call_counter should track calls."""
        @call_counter
        def func():
            return 42
        assert func() == 42
        assert func.count == 1
        func()
        assert func.count == 2

    def test_validate_positive(self):
        """validate_positive should reject negative args."""
        @validate_positive
        def func(x):
            return x * 2
        assert func(5) == 10
        try:
            func(-1)
            assert False
        except ValueError:
            pass

    def test_repeat(self):
        """repeat should call function multiple times."""
        @repeat(3)
        def func():
            return "hi"
        assert func() == ["hi", "hi", "hi"]


class TestContextManagersModule:
    """Tests for the context managers demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        cm_main()

    def test_file_handler(self):
        """FileHandler should read mock files."""
        with FileHandler("data.txt") as f:
            content = f.read()
        assert content == "Hello World"
        assert f.closed

    def test_suppress_errors(self):
        """SuppressErrors should suppress specified exceptions."""
        with SuppressErrors(ValueError):
            raise ValueError("suppressed")
        # Should not raise

    def test_suppress_errors_no_match(self):
        """SuppressErrors should not suppress unmatched exceptions."""
        try:
            with SuppressErrors(ValueError):
                raise KeyError("not suppressed")
            assert False
        except KeyError:
            pass

    def test_temp_value(self):
        """temp_value should restore original value."""
        d = {"key": "original"}
        with temp_value(d, "key", "temp"):
            assert d["key"] == "temp"
        assert d["key"] == "original"
