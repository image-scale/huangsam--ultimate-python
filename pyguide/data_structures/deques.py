"""
Demonstration of Python's collections.deque.

Deque (double-ended queue) provides O(1) append and pop operations
from both ends, making it ideal for queues and stacks.
"""

from collections import deque


def main() -> None:
    # Creating a deque
    d = deque([1, 2, 3])
    assert list(d) == [1, 2, 3]

    # Creating with maxlen - older items are discarded
    limited = deque([1, 2, 3], maxlen=3)
    limited.append(4)
    assert list(limited) == [2, 3, 4]  # 1 dropped

    # append - add to right end
    d = deque([1, 2])
    d.append(3)
    assert list(d) == [1, 2, 3]

    # appendleft - add to left end
    d.appendleft(0)
    assert list(d) == [0, 1, 2, 3]

    # pop - remove from right
    d = deque([1, 2, 3])
    right = d.pop()
    assert right == 3
    assert list(d) == [1, 2]

    # popleft - remove from left
    left = d.popleft()
    assert left == 1
    assert list(d) == [2]

    # extend - add multiple items to right
    d = deque([1])
    d.extend([2, 3, 4])
    assert list(d) == [1, 2, 3, 4]

    # extendleft - add multiple items to left (reversed order)
    d = deque([3])
    d.extendleft([2, 1, 0])  # 0 ends up leftmost
    assert list(d) == [0, 1, 2, 3]

    # rotate - rotate elements right (positive) or left (negative)
    d = deque([1, 2, 3, 4, 5])
    d.rotate(2)  # move last 2 to front
    assert list(d) == [4, 5, 1, 2, 3]

    d.rotate(-2)  # move first 2 to back
    assert list(d) == [1, 2, 3, 4, 5]

    # Indexing works but is O(n) in middle
    d = deque(['a', 'b', 'c'])
    assert d[0] == 'a'
    assert d[-1] == 'c'
    assert d[1] == 'b'

    # count - count occurrences
    d = deque([1, 2, 2, 3, 2])
    assert d.count(2) == 3

    # index - find position
    assert d.index(3) == 3

    # remove - remove first occurrence
    d = deque([1, 2, 3, 2])
    d.remove(2)
    assert list(d) == [1, 3, 2]

    # reverse
    d = deque([1, 2, 3])
    d.reverse()
    assert list(d) == [3, 2, 1]

    # clear
    d.clear()
    assert len(d) == 0

    # copy
    original = deque([1, 2, 3])
    copied = original.copy()
    copied.append(4)
    assert list(original) == [1, 2, 3]
    assert list(copied) == [1, 2, 3, 4]

    # Using deque as a stack (LIFO)
    stack = deque()
    stack.append('first')
    stack.append('second')
    stack.append('third')
    assert stack.pop() == 'third'
    assert stack.pop() == 'second'

    # Using deque as a queue (FIFO)
    queue = deque()
    queue.append('first')
    queue.append('second')
    queue.append('third')
    assert queue.popleft() == 'first'
    assert queue.popleft() == 'second'

    # Maxlen for sliding window
    window = deque(maxlen=3)
    for i in range(5):
        window.append(i)
    assert list(window) == [2, 3, 4]  # only last 3


if __name__ == "__main__":
    main()
