"""
Demonstration of Python tuples.

Tuples are immutable, ordered sequences. Once created, their contents
cannot be changed. They are useful for fixed collections of values.
"""


def main() -> None:
    # Creating tuples
    coords = (10, 20)
    assert len(coords) == 2

    # Single element tuple needs trailing comma
    single = (42,)
    assert isinstance(single, tuple)
    assert len(single) == 1

    # Without comma, it's just parentheses
    not_tuple = (42)
    assert isinstance(not_tuple, int)

    # Tuple without parentheses (packing)
    packed = 1, 2, 3
    assert isinstance(packed, tuple)
    assert packed == (1, 2, 3)

    # Indexing - same as lists
    colors = ('red', 'green', 'blue')
    assert colors[0] == 'red'
    assert colors[-1] == 'blue'

    # Slicing - same as lists
    numbers = (0, 1, 2, 3, 4, 5)
    assert numbers[1:4] == (1, 2, 3)
    assert numbers[::2] == (0, 2, 4)
    assert numbers[::-1] == (5, 4, 3, 2, 1, 0)

    # Tuples are immutable - cannot modify
    point = (3, 4)
    try:
        point[0] = 5  # This would raise TypeError
        assert False, "Should have raised TypeError"
    except TypeError:
        pass  # Expected

    # Tuple unpacking
    x, y = coords
    assert x == 10
    assert y == 20

    # Unpacking with * to collect remaining items
    first, *rest = (1, 2, 3, 4, 5)
    assert first == 1
    assert rest == [2, 3, 4, 5]  # rest is a list

    *start, last = (1, 2, 3, 4, 5)
    assert start == [1, 2, 3, 4]
    assert last == 5

    # Swapping values using tuple unpacking
    a, b = 5, 10
    a, b = b, a
    assert a == 10
    assert b == 5

    # Tuple methods
    items = (1, 2, 2, 3, 2, 4)
    assert items.count(2) == 3     # count occurrences
    assert items.index(3) == 3     # first index

    # Tuples as dict keys (because immutable)
    locations = {
        (40.7128, -74.0060): "New York",
        (34.0522, -118.2437): "Los Angeles",
    }
    assert locations[(40.7128, -74.0060)] == "New York"

    # Named tuples from collections provide named access
    # But for basic tuples, we use indexing

    # Tuple concatenation and repetition
    t1 = (1, 2)
    t2 = (3, 4)
    assert t1 + t2 == (1, 2, 3, 4)
    assert t1 * 3 == (1, 2, 1, 2, 1, 2)

    # Membership testing
    assert 2 in t1
    assert 5 not in t1

    # Comparing tuples - lexicographic comparison
    assert (1, 2, 3) < (1, 2, 4)
    assert (1, 2) < (1, 2, 3)
    assert (2,) > (1, 9, 9)  # first element compared first

    # Tuple from iterable
    from_list = tuple([1, 2, 3])
    assert from_list == (1, 2, 3)

    from_string = tuple("abc")
    assert from_string == ('a', 'b', 'c')

    # Empty tuple
    empty = ()
    assert len(empty) == 0
    assert not empty  # empty tuple is falsy

    # Nested tuples
    nested = ((1, 2), (3, 4), (5, 6))
    assert nested[0] == (1, 2)
    assert nested[1][1] == 4

    # Tuples containing mutable objects
    mixed = ([1, 2], [3, 4])
    mixed[0].append(9)  # can modify the list inside
    assert mixed == ([1, 2, 9], [3, 4])


if __name__ == "__main__":
    main()
