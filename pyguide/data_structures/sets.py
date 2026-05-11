"""
Demonstration of Python sets.

Sets are unordered collections of unique elements. They support
mathematical set operations like union, intersection, and difference.
"""


def main() -> None:
    # Creating sets
    fruits = {'apple', 'banana', 'cherry'}
    assert len(fruits) == 3

    # Sets contain unique elements only
    numbers = {1, 2, 2, 3, 3, 3}
    assert len(numbers) == 3
    assert numbers == {1, 2, 3}

    # Empty set must use set(), not {} (which creates empty dict)
    empty_set = set()
    assert len(empty_set) == 0
    assert isinstance(empty_set, set)

    # Creating from iterable
    from_list = set([1, 2, 3, 2, 1])
    assert from_list == {1, 2, 3}

    from_string = set('hello')
    assert from_string == {'h', 'e', 'l', 'o'}  # unique chars

    # Adding elements
    colors = {'red', 'green'}
    colors.add('blue')
    assert 'blue' in colors

    # Adding duplicate has no effect
    colors.add('red')
    assert len(colors) == 3

    # Adding multiple elements
    colors.update(['yellow', 'purple'])
    assert 'yellow' in colors
    assert 'purple' in colors

    # Removing elements
    colors = {'red', 'green', 'blue'}
    colors.remove('red')  # raises KeyError if not found
    assert 'red' not in colors

    colors.discard('purple')  # no error if not found
    colors.discard('green')
    assert colors == {'blue'}

    # pop removes and returns arbitrary element
    items = {'a', 'b', 'c'}
    popped = items.pop()
    assert popped in {'a', 'b', 'c'}
    assert len(items) == 2

    # Set operations - union (elements in either set)
    a = {1, 2, 3}
    b = {3, 4, 5}
    assert a | b == {1, 2, 3, 4, 5}
    assert a.union(b) == {1, 2, 3, 4, 5}

    # Intersection (elements in both sets)
    assert a & b == {3}
    assert a.intersection(b) == {3}

    # Difference (elements in a but not in b)
    assert a - b == {1, 2}
    assert a.difference(b) == {1, 2}

    # Symmetric difference (elements in either but not both)
    assert a ^ b == {1, 2, 4, 5}
    assert a.symmetric_difference(b) == {1, 2, 4, 5}

    # Subset and superset
    small = {1, 2}
    large = {1, 2, 3, 4}
    assert small.issubset(large)
    assert small <= large
    assert large.issuperset(small)
    assert large >= small

    # Proper subset (subset but not equal)
    assert small < large
    assert not small < small

    # Disjoint sets (no common elements)
    x = {1, 2}
    y = {3, 4}
    assert x.isdisjoint(y)

    # Membership testing
    nums = {1, 2, 3, 4, 5}
    assert 3 in nums
    assert 6 not in nums

    # Set comparison
    assert {1, 2, 3} == {3, 2, 1}  # order doesn't matter

    # Frozen sets - immutable sets
    frozen = frozenset([1, 2, 3])
    assert 2 in frozen
    # frozen.add(4) would raise AttributeError

    # Frozen sets can be dict keys or set elements
    sets_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
    assert len(sets_of_sets) == 2

    # In-place operations
    a = {1, 2, 3}
    a |= {4, 5}  # update with union
    assert a == {1, 2, 3, 4, 5}

    a &= {3, 4, 5, 6}  # update with intersection
    assert a == {3, 4, 5}


if __name__ == "__main__":
    main()
