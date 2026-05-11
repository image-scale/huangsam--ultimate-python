"""
Demonstration of Python dictionaries.

Dictionaries are mutable mappings from keys to values. Keys must be
hashable (immutable), but values can be any type.
"""


def main() -> None:
    # Creating dictionaries
    person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
    assert len(person) == 3

    # Accessing values
    assert person['name'] == 'Alice'
    assert person.get('age') == 30
    assert person.get('country', 'Unknown') == 'Unknown'  # with default

    # Setting values
    person['email'] = 'alice@example.com'
    assert 'email' in person

    # Modifying values
    person['age'] = 31
    assert person['age'] == 31

    # Removing items
    del person['email']
    assert 'email' not in person

    # pop removes and returns
    age = person.pop('age')
    assert age == 31
    assert 'age' not in person

    # pop with default for missing key
    result = person.pop('missing', 'default')
    assert result == 'default'

    # Dictionary from keys
    keys = ['a', 'b', 'c']
    d = dict.fromkeys(keys, 0)
    assert d == {'a': 0, 'b': 0, 'c': 0}

    # Dictionary from list of tuples
    pairs = [('x', 1), ('y', 2), ('z', 3)]
    d = dict(pairs)
    assert d == {'x': 1, 'y': 2, 'z': 3}

    # Iterating over dictionaries
    data = {'a': 1, 'b': 2, 'c': 3}

    # Keys
    collected_keys = []
    for key in data:  # or data.keys()
        collected_keys.append(key)
    assert set(collected_keys) == {'a', 'b', 'c'}

    # Values
    collected_values = []
    for value in data.values():
        collected_values.append(value)
    assert set(collected_values) == {1, 2, 3}

    # Key-value pairs
    collected_items = []
    for key, value in data.items():
        collected_items.append((key, value))
    assert set(collected_items) == {('a', 1), ('b', 2), ('c', 3)}

    # Membership testing (checks keys)
    assert 'a' in data
    assert 'd' not in data

    # setdefault - get or set if missing
    counts = {'apple': 5}
    counts.setdefault('apple', 0)  # exists, no change
    assert counts['apple'] == 5

    counts.setdefault('banana', 0)  # doesn't exist, sets to 0
    assert counts['banana'] == 0

    # update - merge dictionaries
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    d1.update(d2)
    assert d1 == {'a': 1, 'b': 3, 'c': 4}  # b overwritten

    # Dictionary copying
    original = {'x': 1, 'y': 2}
    shallow = original.copy()
    shallow['x'] = 99
    assert original['x'] == 1  # original unchanged

    # Nested dictionaries
    nested = {
        'user': {'name': 'Bob', 'age': 25},
        'settings': {'theme': 'dark'}
    }
    assert nested['user']['name'] == 'Bob'

    # Dictionary with various key types
    mixed_keys = {
        'string': 1,
        42: 2,
        (1, 2): 3,  # tuples are hashable
    }
    assert mixed_keys[(1, 2)] == 3

    # keys(), values(), items() return views
    d = {'a': 1, 'b': 2}
    keys_view = d.keys()
    d['c'] = 3
    assert 'c' in keys_view  # view updates with dict

    # clear removes all items
    d = {'a': 1, 'b': 2}
    d.clear()
    assert len(d) == 0

    # popitem removes last inserted item (Python 3.7+)
    d = {'first': 1, 'second': 2, 'third': 3}
    key, value = d.popitem()
    assert key == 'third'
    assert len(d) == 2


if __name__ == "__main__":
    main()
