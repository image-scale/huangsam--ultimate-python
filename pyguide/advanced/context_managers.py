"""
Demonstration of Python context managers.

Context managers handle setup and cleanup automatically using the
with statement. They implement __enter__ and __exit__ or use
the @contextmanager decorator.
"""

from contextlib import contextmanager
from io import StringIO


MOCK_FILES = {
    "data.txt": "Hello World",
    "config.json": '{"key": "value"}',
}


class FileHandler:
    """Class-based context manager for file simulation."""

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.buffer = None

    def __enter__(self) -> StringIO:
        """Open the file and return the buffer."""
        if self.filename not in MOCK_FILES:
            raise FileNotFoundError(f"File not found: {self.filename}")
        self.buffer = StringIO(MOCK_FILES[self.filename])
        return self.buffer

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Close the buffer, optionally handle exceptions."""
        if self.buffer:
            self.buffer.close()
        return False  # Don't suppress exceptions


class SuppressErrors:
    """Context manager that suppresses specified exceptions."""

    def __init__(self, *exceptions) -> None:
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is not None and issubclass(exc_type, self.exceptions):
            return True  # Suppress the exception
        return False


@contextmanager
def temp_value(obj: dict, key: str, value):
    """Temporarily set a dict value, restore original after."""
    original = obj.get(key)
    existed = key in obj
    obj[key] = value
    try:
        yield obj
    finally:
        if existed:
            obj[key] = original
        else:
            del obj[key]


@contextmanager
def capture_output():
    """Capture stdout for testing."""
    buffer = StringIO()
    yield buffer
    buffer.seek(0)


def main() -> None:
    # Class-based context manager
    with FileHandler("data.txt") as f:
        content = f.read()
    assert content == "Hello World"

    # File is closed after with block
    assert f.closed

    # Handles missing files
    try:
        with FileHandler("missing.txt") as f:
            pass
        assert False
    except FileNotFoundError:
        pass

    # Context manager with exception suppression
    with SuppressErrors(ValueError, TypeError):
        raise ValueError("This is suppressed")
    # No exception raised outside with block

    # Exception not in list is not suppressed
    try:
        with SuppressErrors(ValueError):
            raise KeyError("This is not suppressed")
        assert False
    except KeyError:
        pass

    # Generator-based context manager
    config = {"debug": False}
    assert config["debug"] is False

    with temp_value(config, "debug", True) as c:
        assert c["debug"] is True

    assert config["debug"] is False  # Restored

    # Adding temporary key
    with temp_value(config, "new_key", "temp_value"):
        assert config["new_key"] == "temp_value"

    assert "new_key" not in config  # Removed

    # Nested context managers
    with FileHandler("data.txt") as f1:
        with FileHandler("config.json") as f2:
            content1 = f1.read()
            content2 = f2.read()

    assert "Hello" in content1
    assert "key" in content2

    # Multiple context managers in one with
    with FileHandler("data.txt") as f1, FileHandler("config.json") as f2:
        combined = f1.read() + f2.read()
    assert len(combined) > 0


if __name__ == "__main__":
    main()
