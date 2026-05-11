"""
Benchmarking helps identify performance bottlenecks in code. Python
provides several tools for measuring execution time and profiling.

This module demonstrates:
1. Basic timing with time module
2. cProfile for detailed profiling
3. timeit for microbenchmarks
4. Comparing algorithmic approaches
5. Memory usage awareness
"""

import cProfile
import io
import pstats
import time
import timeit
from functools import lru_cache


def time_function(func, *args, **kwargs):
    """Time a function execution and return (result, duration)."""
    start = time.perf_counter()
    result = func(*args, **kwargs)
    duration = time.perf_counter() - start
    return result, duration


def slow_fibonacci(n: int) -> int:
    """Compute Fibonacci number (slow recursive implementation)."""
    if n < 2:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


@lru_cache(maxsize=None)
def cached_fibonacci(n: int) -> int:
    """Compute Fibonacci number with memoization."""
    if n < 2:
        return n
    return cached_fibonacci(n - 1) + cached_fibonacci(n - 2)


def iterative_fibonacci(n: int) -> int:
    """Compute Fibonacci number iteratively."""
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def linear_search(items: list, target) -> int:
    """Linear search returning index or -1."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1


def binary_search(items: list, target) -> int:
    """Binary search on sorted list returning index or -1."""
    left, right = 0, len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


class ProfileResult:
    """Container for profiling results."""

    def __init__(self, stats_str: str, total_time: float, call_count: int):
        self.stats_str = stats_str
        self.total_time = total_time
        self.call_count = call_count


def profile_function(func, *args, **kwargs) -> ProfileResult:
    """Profile a function and return statistics."""
    profiler = cProfile.Profile()

    profiler.enable()
    func(*args, **kwargs)
    profiler.disable()

    buffer = io.StringIO()
    stats = pstats.Stats(profiler, stream=buffer)
    stats.sort_stats("cumulative")
    stats.print_stats()

    total_time = stats.total_tt
    total_calls = stats.total_calls

    return ProfileResult(buffer.getvalue(), total_time, total_calls)


def timeit_compare(stmt1: str, stmt2: str, setup: str = "", number: int = 1000):
    """Compare execution times of two statements."""
    time1 = timeit.timeit(stmt1, setup=setup, number=number)
    time2 = timeit.timeit(stmt2, setup=setup, number=number)
    return time1, time2


def main():
    # Basic timing comparison
    _, slow_time = time_function(slow_fibonacci, 20)
    _, cached_time = time_function(cached_fibonacci, 20)
    _, iter_time = time_function(iterative_fibonacci, 20)

    assert cached_time < slow_time
    assert iter_time < slow_time

    cached_fibonacci.cache_clear()

    # All produce same result
    assert slow_fibonacci(20) == cached_fibonacci(20) == iterative_fibonacci(20)

    # Search algorithm comparison
    items = list(range(10000))
    target = 9999

    _, linear_time = time_function(linear_search, items, target)
    _, binary_time = time_function(binary_search, items, target)

    assert binary_time < linear_time
    assert linear_search(items, target) == binary_search(items, target)

    # Profile the slow fibonacci
    result = profile_function(slow_fibonacci, 15)
    assert result.call_count > 0
    assert result.total_time > 0
    assert "slow_fibonacci" in result.stats_str

    # Timeit for microbenchmarks
    list_time, set_time = timeit_compare(
        "5000 in items",
        "5000 in items",
        setup="items = list(range(10000)); items_set = set(items)",
        number=100,
    )

    set_lookup_time = timeit.timeit(
        "5000 in items_set",
        setup="items_set = set(range(10000))",
        number=1000,
    )
    list_lookup_time = timeit.timeit(
        "5000 in items_list",
        setup="items_list = list(range(10000))",
        number=1000,
    )

    assert set_lookup_time < list_lookup_time

    # String concatenation comparison
    join_time = timeit.timeit(
        "''.join(['a'] * 1000)", number=1000
    )
    concat_time = timeit.timeit(
        "s = ''\nfor _ in range(1000): s += 'a'", number=1000
    )

    assert join_time < concat_time

    # List comprehension vs loop
    comp_time = timeit.timeit(
        "[x * 2 for x in range(1000)]", number=1000
    )
    loop_time = timeit.timeit(
        "result = []\nfor x in range(1000): result.append(x * 2)",
        number=1000,
    )

    assert comp_time < loop_time


if __name__ == "__main__":
    main()
