"""
Demonstration of Python comprehensions.

Comprehensions provide concise syntax for creating collections by
transforming and filtering iterables in a single expression.
"""


def main() -> None:
    # Basic list comprehension
    squares = [x ** 2 for x in range(6)]
    assert squares == [0, 1, 4, 9, 16, 25]

    # List comprehension with condition (filter)
    evens = [x for x in range(10) if x % 2 == 0]
    assert evens == [0, 2, 4, 6, 8]

    # List comprehension with transformation
    words = ['hello', 'world', 'python']
    upper_words = [word.upper() for word in words]
    assert upper_words == ['HELLO', 'WORLD', 'PYTHON']

    # List comprehension with both filter and transformation
    long_upper = [word.upper() for word in words if len(word) > 5]
    assert long_upper == ['PYTHON']

    # Nested list comprehension
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    assert flattened == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Creating a matrix with comprehension
    grid = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    assert grid == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

    # Tuple comprehension (actually a generator, wrap in tuple())
    cubes_gen = (x ** 3 for x in range(5))
    cubes = tuple(cubes_gen)
    assert cubes == (0, 1, 8, 27, 64)

    # Set comprehension - automatically removes duplicates
    word = "mississippi"
    unique_chars = {char for char in word}
    assert unique_chars == {'m', 'i', 's', 'p'}

    # Set comprehension with transformation
    abs_values = {abs(x) for x in [-3, -1, 0, 1, 2, 3]}
    assert abs_values == {0, 1, 2, 3}

    # Dictionary comprehension
    numbers = [1, 2, 3, 4, 5]
    squared_dict = {x: x ** 2 for x in numbers}
    assert squared_dict == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # Dict comprehension with condition
    even_squared = {x: x ** 2 for x in numbers if x % 2 == 0}
    assert even_squared == {2: 4, 4: 16}

    # Swapping keys and values
    original = {'a': 1, 'b': 2, 'c': 3}
    swapped = {v: k for k, v in original.items()}
    assert swapped == {1: 'a', 2: 'b', 3: 'c'}

    # Multiple conditions in comprehension
    nums = range(1, 31)
    special = [x for x in nums if x % 2 == 0 if x % 3 == 0]
    assert special == [6, 12, 18, 24, 30]  # divisible by both 2 and 3

    # if-else in expression (ternary in comprehension)
    numbers = [1, 2, 3, 4, 5]
    labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
    assert labels == ['odd', 'even', 'odd', 'even', 'odd']

    # Comprehension with enumerate
    items = ['apple', 'banana', 'cherry']
    indexed = {i: item for i, item in enumerate(items)}
    assert indexed == {0: 'apple', 1: 'banana', 2: 'cherry'}

    # Comprehension with zip
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    combined = {k: v for k, v in zip(keys, values)}
    assert combined == {'a': 1, 'b': 2, 'c': 3}

    # Nested dict comprehension
    outer = {x: {y: x * y for y in range(1, 3)} for x in range(1, 3)}
    assert outer == {1: {1: 1, 2: 2}, 2: {1: 2, 2: 4}}

    # Comprehension calling functions
    def process(x):
        return x * 10

    processed = [process(x) for x in range(5)]
    assert processed == [0, 10, 20, 30, 40]

    # Creating zeros
    zeros = [0 for _ in range(5)]
    assert zeros == [0, 0, 0, 0, 0]


if __name__ == "__main__":
    main()
