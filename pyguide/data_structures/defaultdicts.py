"""
Demonstration of Python's collections.defaultdict.

Defaultdict provides automatic default values for missing keys,
eliminating the need for key existence checks.
"""

from collections import defaultdict


def main() -> None:
    # Regular dict raises KeyError for missing keys
    regular = {}
    try:
        _ = regular['missing']
        assert False, "Should have raised KeyError"
    except KeyError:
        pass

    # defaultdict returns default for missing keys
    dd = defaultdict(int)  # int() returns 0
    assert dd['missing'] == 0

    # The key is now in the dict
    assert 'missing' in dd

    # Using defaultdict for counting
    counts = defaultdict(int)
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    for word in words:
        counts[word] += 1
    assert counts['apple'] == 3
    assert counts['banana'] == 2
    assert counts['cherry'] == 1

    # Using defaultdict for grouping
    groups = defaultdict(list)
    items = [('fruit', 'apple'), ('veg', 'carrot'), ('fruit', 'banana')]
    for category, item in items:
        groups[category].append(item)
    assert groups['fruit'] == ['apple', 'banana']
    assert groups['veg'] == ['carrot']

    # Using defaultdict for sets (no duplicates)
    unique = defaultdict(set)
    data = [('a', 1), ('b', 2), ('a', 1), ('a', 3)]
    for key, value in data:
        unique[key].add(value)
    assert unique['a'] == {1, 3}
    assert unique['b'] == {2}

    # Custom default factory with lambda
    dd = defaultdict(lambda: 'N/A')
    dd['name'] = 'Alice'
    assert dd['name'] == 'Alice'
    assert dd['age'] == 'N/A'

    # Nested defaultdict
    nested = defaultdict(lambda: defaultdict(int))
    nested['users']['count'] += 1
    nested['users']['count'] += 1
    nested['posts']['count'] += 5
    assert nested['users']['count'] == 2
    assert nested['posts']['count'] == 5

    # Converting to regular dict
    dd = defaultdict(int, {'a': 1, 'b': 2})
    regular = dict(dd)
    assert regular == {'a': 1, 'b': 2}

    # defaultdict with existing data
    dd = defaultdict(list, {'colors': ['red']})
    dd['colors'].append('blue')
    dd['sizes'].append('small')
    assert dd['colors'] == ['red', 'blue']
    assert dd['sizes'] == ['small']

    # Accessing default_factory
    dd = defaultdict(str)
    assert dd.default_factory == str

    # Setting default_factory to None makes it behave like dict
    dd.default_factory = None
    try:
        _ = dd['missing']
        assert False, "Should have raised KeyError"
    except KeyError:
        pass


if __name__ == "__main__":
    main()
