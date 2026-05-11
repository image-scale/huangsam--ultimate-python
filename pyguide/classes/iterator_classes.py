"""
Demonstration of Python iterator classes.

Iterators implement __iter__ and __next__ to provide sequential access
to elements. Generators offer a simpler alternative using yield.
"""


class RangeIterator:
    """Custom iterator that mimics range behavior."""

    def __init__(self, start: int, stop: int, step: int = 1) -> None:
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self) -> int:
        """Return the next value or raise StopIteration."""
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        if self.step < 0 and self.current <= self.stop:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result


class FibonacciIterator:
    """Iterator that generates Fibonacci numbers up to a limit."""

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.a > self.limit:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


def countdown_generator(start: int):
    """Generator function that counts down to zero."""
    while start >= 0:
        yield start
        start -= 1


def fibonacci_generator(limit: int):
    """Generator function for Fibonacci numbers."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def main() -> None:
    # Using custom iterator in a for loop
    result = list(RangeIterator(0, 5))
    assert result == [0, 1, 2, 3, 4]

    # With step
    result = list(RangeIterator(0, 10, 2))
    assert result == [0, 2, 4, 6, 8]

    # Negative step
    result = list(RangeIterator(5, 0, -1))
    assert result == [5, 4, 3, 2, 1]

    # Manual iteration with next()
    it = RangeIterator(1, 4)
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3
    try:
        next(it)
        assert False, "Should have raised StopIteration"
    except StopIteration:
        pass

    # Fibonacci iterator
    fibs = list(FibonacciIterator(20))
    assert fibs == [0, 1, 1, 2, 3, 5, 8, 13]

    # Generator function - simpler syntax
    countdown = list(countdown_generator(5))
    assert countdown == [5, 4, 3, 2, 1, 0]

    # Generator is an iterator
    gen = countdown_generator(3)
    assert next(gen) == 3
    assert next(gen) == 2

    # Fibonacci generator
    gen_fibs = list(fibonacci_generator(20))
    assert gen_fibs == [0, 1, 1, 2, 3, 5, 8, 13]

    # Generator expression
    squares = (x ** 2 for x in range(5))
    assert list(squares) == [0, 1, 4, 9, 16]

    # iter() with sentinel
    def counter():
        count = [0]
        def inc():
            count[0] += 1
            return count[0]
        return inc

    # Iterate until callable returns 5
    values = list(iter(counter(), 5))
    assert values == [1, 2, 3, 4]

    # Iterators are single-use
    it = RangeIterator(0, 3)
    first_pass = list(it)
    second_pass = list(it)
    assert first_pass == [0, 1, 2]
    assert second_pass == []  # exhausted


if __name__ == "__main__":
    main()
