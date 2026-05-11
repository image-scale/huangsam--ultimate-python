"""
Demonstration of Python dictionary merge/union operators.

Python 3.9+ introduced | and |= operators for merging dictionaries,
providing cleaner syntax than dict.update() or {**d1, **d2}.
"""


def main() -> None:
    # Dictionary union with | (creates new dict)
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}

    merged = d1 | d2
    assert merged == {'a': 1, 'b': 3, 'c': 4}  # d2 values win
    assert d1 == {'a': 1, 'b': 2}  # d1 unchanged

    # Order matters - right dict values take precedence
    merged_reverse = d2 | d1
    assert merged_reverse == {'a': 1, 'b': 2, 'c': 4}  # d1 values win

    # In-place union with |=
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    d1 |= d2
    assert d1 == {'a': 1, 'b': 3, 'c': 4}  # d1 modified

    # Chaining multiple dictionaries
    d1 = {'a': 1}
    d2 = {'b': 2}
    d3 = {'c': 3}
    combined = d1 | d2 | d3
    assert combined == {'a': 1, 'b': 2, 'c': 3}

    # Union with iterables of key-value pairs
    d = {'a': 1}
    d |= [('b', 2), ('c', 3)]
    assert d == {'a': 1, 'b': 2, 'c': 3}

    # Comparison with older methods
    # Method 1: dict.update() - modifies in place
    d1 = {'a': 1}
    d1.update({'b': 2})
    assert d1 == {'a': 1, 'b': 2}

    # Method 2: unpacking with ** - creates new dict
    d1 = {'a': 1}
    d2 = {'b': 2}
    merged = {**d1, **d2}
    assert merged == {'a': 1, 'b': 2}

    # Method 3: dict() constructor with unpacking
    merged = dict(**d1, **d2)  # fails if same key in both
    assert merged == {'a': 1, 'b': 2}

    # Union preserves key order (insertion order)
    d1 = {'z': 1, 'a': 2}
    d2 = {'b': 3}
    result = d1 | d2
    assert list(result.keys()) == ['z', 'a', 'b']

    # Union with empty dicts
    d = {'a': 1}
    assert d | {} == {'a': 1}
    assert {} | d == {'a': 1}

    # Real-world example: config defaults with overrides
    defaults = {'debug': False, 'timeout': 30, 'retries': 3}
    user_config = {'debug': True, 'timeout': 60}
    final_config = defaults | user_config
    assert final_config == {'debug': True, 'timeout': 60, 'retries': 3}


if __name__ == "__main__":
    main()
