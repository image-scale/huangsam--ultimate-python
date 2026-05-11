"""
Threading allows concurrent execution of code, particularly useful for
I/O-bound tasks. Due to Python's Global Interpreter Lock (GIL), threads
are not truly parallel for CPU-bound work, but they excel at tasks
involving waiting (network, file I/O, sleep).

This module demonstrates:
1. Basic threading with Thread class
2. ThreadPoolExecutor for managed thread pools
3. Thread synchronization with Lock
4. Thread-safe data sharing
5. Daemon threads
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable


class Counter:
    """Thread-safe counter using a lock."""

    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            current = self._value
            time.sleep(0.001)
            self._value = current + 1

    def increment_unsafe(self):
        current = self._value
        time.sleep(0.001)
        self._value = current + 1

    @property
    def value(self):
        return self._value


class SharedBuffer:
    """Thread-safe buffer using condition variable."""

    def __init__(self, max_size: int = 5):
        self.buffer: list = []
        self.max_size = max_size
        self._lock = threading.Lock()
        self._not_full = threading.Condition(self._lock)
        self._not_empty = threading.Condition(self._lock)

    def put(self, item):
        with self._not_full:
            while len(self.buffer) >= self.max_size:
                self._not_full.wait()
            self.buffer.append(item)
            self._not_empty.notify()

    def get(self):
        with self._not_empty:
            while not self.buffer:
                self._not_empty.wait()
            item = self.buffer.pop(0)
            self._not_full.notify()
            return item

    def size(self):
        with self._lock:
            return len(self.buffer)


def delayed_multiply(x: int, delay: float = 0.01) -> int:
    """Multiply by 2 with a delay to simulate I/O work."""
    time.sleep(delay)
    return x * 2


def run_with_threads(func: Callable[[int], int], items: list[int]) -> list[int]:
    """Run function on items using thread pool."""
    results = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(func, item): item for item in items}
        for future in as_completed(futures):
            results.append(future.result())
    return results


def run_sequential(func: Callable[[int], int], items: list[int]) -> list[int]:
    """Run function on items sequentially."""
    return [func(item) for item in items]


def basic_thread_example():
    """Create and run a basic thread."""
    results = []

    def worker(name: str, value: int):
        time.sleep(0.01)
        results.append((name, value * 2))

    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(f"thread-{i}", i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return results


def daemon_thread_example():
    """Demonstrate daemon vs non-daemon threads."""
    daemon_ran = []
    non_daemon_ran = []

    def daemon_work():
        daemon_ran.append(True)

    def non_daemon_work():
        non_daemon_ran.append(True)

    daemon = threading.Thread(target=daemon_work, daemon=True)
    non_daemon = threading.Thread(target=non_daemon_work, daemon=False)

    daemon.start()
    non_daemon.start()

    daemon.join(timeout=0.1)
    non_daemon.join(timeout=0.1)

    return len(daemon_ran), len(non_daemon_ran)


def main():
    # Basic thread creation and execution
    results = basic_thread_example()
    assert len(results) == 3

    # ThreadPoolExecutor is faster for I/O-bound work
    items = list(range(10))

    start_seq = time.time()
    sequential_results = run_sequential(delayed_multiply, items)
    seq_time = time.time() - start_seq

    start_thread = time.time()
    thread_results = run_with_threads(delayed_multiply, items)
    thread_time = time.time() - start_thread

    assert sorted(thread_results) == sorted(sequential_results)
    assert thread_time < seq_time

    # Thread-safe counter with lock
    counter = Counter()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=counter.increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert counter.value == 10

    # Unsafe counter may produce incorrect results with race conditions
    unsafe_counter = Counter()
    threads = []
    for _ in range(5):
        t = threading.Thread(target=unsafe_counter.increment_unsafe)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Buffer with producer/consumer pattern
    buffer = SharedBuffer(max_size=3)
    produced = []
    consumed = []

    def producer():
        for i in range(5):
            buffer.put(i)
            produced.append(i)

    def consumer():
        for _ in range(5):
            item = buffer.get()
            consumed.append(item)

    prod_thread = threading.Thread(target=producer)
    cons_thread = threading.Thread(target=consumer)

    prod_thread.start()
    cons_thread.start()

    prod_thread.join()
    cons_thread.join()

    assert produced == [0, 1, 2, 3, 4]
    assert sorted(consumed) == [0, 1, 2, 3, 4]

    # Thread attributes
    main_thread = threading.main_thread()
    current_thread = threading.current_thread()
    assert main_thread is current_thread
    assert threading.active_count() >= 1


if __name__ == "__main__":
    main()
