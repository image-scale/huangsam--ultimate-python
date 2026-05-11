"""
Demonstration of Python's argument enforcement features.

Python supports positional-only and keyword-only parameters to control
how arguments must be passed to functions. Introduced in Python 3.8
(PEP 570 for positional-only) and Python 3.0 (keyword-only).
"""


def positional_only(x, y, /):
    """Function with positional-only parameters (before /).

    These parameters cannot be passed as keyword arguments.
    """
    return x + y


def keyword_only(*, x, y):
    """Function with keyword-only parameters (after *).

    These parameters must be passed as keyword arguments.
    """
    return x + y


def mixed_parameters(pos_only, /, regular, *, kw_only):
    """Function with all three types of parameters.

    - pos_only: must be passed positionally
    - regular: can be passed either way
    - kw_only: must be passed as keyword
    """
    return f"pos={pos_only}, reg={regular}, kw={kw_only}"


def with_defaults(x, /, y=10, *, z=20):
    """Function combining positional-only with defaults."""
    return x + y + z


def main() -> None:
    # Positional-only parameters
    result = positional_only(3, 5)
    assert result == 8

    # This would fail: positional_only(x=3, y=5)
    # TypeError: positional_only() got some positional-only arguments
    # passed as keyword arguments: 'x', 'y'

    # Keyword-only parameters
    result = keyword_only(x=3, y=5)
    assert result == 8

    # Order doesn't matter for keyword arguments
    result = keyword_only(y=5, x=3)
    assert result == 8

    # This would fail: keyword_only(3, 5)
    # TypeError: keyword_only() takes 0 positional arguments but 2 were given

    # Mixed parameters - demonstrates all three types
    result = mixed_parameters(1, 2, kw_only=3)
    assert result == "pos=1, reg=2, kw=3"

    # Regular parameter can be passed as keyword
    result = mixed_parameters(1, regular=2, kw_only=3)
    assert result == "pos=1, reg=2, kw=3"

    # This would fail: mixed_parameters(pos_only=1, regular=2, kw_only=3)
    # This would fail: mixed_parameters(1, 2, 3)

    # Default values work with all parameter types
    assert with_defaults(5) == 35         # 5 + 10 + 20
    assert with_defaults(5, 15) == 40     # 5 + 15 + 20
    assert with_defaults(5, z=25) == 40   # 5 + 10 + 25
    assert with_defaults(5, 15, z=25) == 45

    # Practical example: function where parameter names might conflict
    def dict_get(d, /, key, default=None):
        """Get a value from dict. 'd' is positional-only to avoid
        conflict if the dict contains 'd' as a key."""
        return d.get(key, default)

    my_dict = {"d": "value_d", "key": "value_key"}
    # Without positional-only, this call would be ambiguous
    result = dict_get(my_dict, "d")
    assert result == "value_d"

    # Practical example: enforcing readable API at call site
    def connect(*, host, port, timeout=30):
        """Connect to a server. Keywords-only makes calls self-documenting."""
        return f"Connecting to {host}:{port} (timeout={timeout}s)"

    # Caller must name the arguments - more readable
    result = connect(host="localhost", port=8080)
    assert "localhost:8080" in result

    # With *args and keyword-only
    def log(*messages, level="INFO"):
        """Log messages with keyword-only level."""
        return f"[{level}] " + " ".join(messages)

    result = log("Hello", "World")
    assert result == "[INFO] Hello World"

    result = log("Error occurred", level="ERROR")
    assert result == "[ERROR] Error occurred"


if __name__ == "__main__":
    main()
