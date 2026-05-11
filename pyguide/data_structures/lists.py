"""
Demonstration of Python lists.

Lists are mutable, ordered sequences that can hold any type of object.
They support indexing, slicing, and various modification methods.
"""


def main() -> None:
    # Creating lists
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5

    # Indexing - positive and negative
    assert numbers[0] == 1        # first element
    assert numbers[-1] == 5       # last element
    assert numbers[-2] == 4       # second to last

    # Slicing - [start:stop:step]
    assert numbers[1:4] == [2, 3, 4]      # elements 1, 2, 3
    assert numbers[:3] == [1, 2, 3]        # first 3 elements
    assert numbers[2:] == [3, 4, 5]        # from index 2 onwards
    assert numbers[::2] == [1, 3, 5]       # every other element
    assert numbers[::-1] == [5, 4, 3, 2, 1]  # reversed

    # Lists are mutable - can modify in place
    numbers[0] = 10
    assert numbers[0] == 10
    numbers[0] = 1  # restore

    # Modifying with slice assignment
    letters = ['a', 'b', 'c', 'd']
    letters[1:3] = ['X', 'Y', 'Z']
    assert letters == ['a', 'X', 'Y', 'Z', 'd']

    # Adding elements
    items = [1, 2, 3]
    items.append(4)               # add to end
    assert items == [1, 2, 3, 4]

    items.insert(0, 0)            # insert at index
    assert items == [0, 1, 2, 3, 4]

    items.extend([5, 6])          # add multiple items
    assert items == [0, 1, 2, 3, 4, 5, 6]

    # Removing elements
    items = [1, 2, 3, 2, 4]
    items.remove(2)               # remove first occurrence
    assert items == [1, 3, 2, 4]

    popped = items.pop()          # remove and return last
    assert popped == 4
    assert items == [1, 3, 2]

    popped = items.pop(0)         # remove at index
    assert popped == 1
    assert items == [3, 2]

    # Sorting
    unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
    unsorted.sort()               # in-place sort
    assert unsorted == [1, 1, 2, 3, 4, 5, 6, 9]

    unsorted.sort(reverse=True)   # descending
    assert unsorted == [9, 6, 5, 4, 3, 2, 1, 1]

    # sorted() returns new list
    original = [3, 1, 2]
    new_sorted = sorted(original)
    assert new_sorted == [1, 2, 3]
    assert original == [3, 1, 2]  # unchanged

    # Reversing
    items = [1, 2, 3]
    items.reverse()               # in-place
    assert items == [3, 2, 1]

    # reversed() returns iterator
    items = [1, 2, 3]
    assert list(reversed(items)) == [3, 2, 1]

    # Finding elements
    items = ['a', 'b', 'c', 'b']
    assert items.index('b') == 1       # first index of 'b'
    assert items.count('b') == 2       # count occurrences

    # Membership testing
    assert 'a' in items
    assert 'x' not in items

    # List concatenation and repetition
    a = [1, 2]
    b = [3, 4]
    assert a + b == [1, 2, 3, 4]
    assert a * 3 == [1, 2, 1, 2, 1, 2]

    # Nested lists
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix[0][0] == 1
    assert matrix[1][2] == 6

    # List copying
    original = [1, 2, 3]
    shallow = original.copy()     # or original[:]
    assert shallow == original
    shallow[0] = 99
    assert original[0] == 1       # original unchanged

    # Empty list checks
    empty = []
    assert not empty              # empty list is falsy
    assert len(empty) == 0


if __name__ == "__main__":
    main()
