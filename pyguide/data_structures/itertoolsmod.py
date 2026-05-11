"""
Demonstration of Python's itertools module.

Itertools provides memory-efficient iterators for common patterns
like counting, cycling, chaining, and combinations.
"""

import itertools


def main() -> None:
    # count - infinite counter
    counter = itertools.count(10, 2)  # start at 10, step by 2
    assert next(counter) == 10
    assert next(counter) == 12
    assert next(counter) == 14

    # cycle - infinite cycling through iterable
    cycler = itertools.cycle(['A', 'B', 'C'])
    result = [next(cycler) for _ in range(5)]
    assert result == ['A', 'B', 'C', 'A', 'B']

    # repeat - repeat value n times (or infinitely)
    repeated = list(itertools.repeat('X', 4))
    assert repeated == ['X', 'X', 'X', 'X']

    # chain - combine iterables sequentially
    combined = list(itertools.chain([1, 2], [3, 4], [5]))
    assert combined == [1, 2, 3, 4, 5]

    # chain.from_iterable - flatten nested iterables
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = list(itertools.chain.from_iterable(nested))
    assert flat == [1, 2, 3, 4, 5, 6]

    # islice - slice an iterator
    counter = itertools.count()
    sliced = list(itertools.islice(counter, 5))  # first 5
    assert sliced == [0, 1, 2, 3, 4]

    sliced = list(itertools.islice(range(10), 2, 7, 2))  # [start:stop:step]
    assert sliced == [2, 4, 6]

    # takewhile - take while predicate is true
    taken = list(itertools.takewhile(lambda x: x < 5, range(10)))
    assert taken == [0, 1, 2, 3, 4]

    # dropwhile - skip while predicate is true
    dropped = list(itertools.dropwhile(lambda x: x < 5, range(10)))
    assert dropped == [5, 6, 7, 8, 9]

    # filterfalse - opposite of filter
    odds = list(itertools.filterfalse(lambda x: x % 2 == 0, range(8)))
    assert odds == [1, 3, 5, 7]

    # groupby - group consecutive elements
    data = 'AAABBBCCAAA'
    groups = [(key, list(group)) for key, group in itertools.groupby(data)]
    assert groups == [('A', ['A', 'A', 'A']),
                      ('B', ['B', 'B', 'B']),
                      ('C', ['C', 'C']),
                      ('A', ['A', 'A', 'A'])]

    # accumulate - running totals (or other operations)
    running_sum = list(itertools.accumulate([1, 2, 3, 4]))
    assert running_sum == [1, 3, 6, 10]

    import operator
    running_product = list(itertools.accumulate([1, 2, 3, 4], operator.mul))
    assert running_product == [1, 2, 6, 24]

    # product - cartesian product
    prod = list(itertools.product([1, 2], ['a', 'b']))
    assert prod == [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

    # permutations - all orderings
    perms = list(itertools.permutations([1, 2, 3], 2))
    assert len(perms) == 6
    assert (1, 2) in perms
    assert (2, 1) in perms

    # combinations - subsets without repetition
    combs = list(itertools.combinations([1, 2, 3], 2))
    assert combs == [(1, 2), (1, 3), (2, 3)]

    # combinations_with_replacement
    combs_rep = list(itertools.combinations_with_replacement([1, 2], 2))
    assert combs_rep == [(1, 1), (1, 2), (2, 2)]

    # zip_longest - zip but continue to longest iterable
    zipped = list(itertools.zip_longest([1, 2], [3, 4, 5], fillvalue=0))
    assert zipped == [(1, 3), (2, 4), (0, 5)]

    # starmap - apply function with unpacked arguments
    points = [(2, 3), (4, 5), (6, 7)]
    sums = list(itertools.starmap(lambda x, y: x + y, points))
    assert sums == [5, 9, 13]

    # tee - create multiple iterators from one
    it = iter([1, 2, 3])
    it1, it2 = itertools.tee(it)
    assert list(it1) == [1, 2, 3]
    assert list(it2) == [1, 2, 3]


if __name__ == "__main__":
    main()
