"""
Demonstration of Python's heapq module.

Heaps are binary trees where parent nodes are smaller than children,
enabling efficient min-heap operations. Heapq uses regular lists.
"""

import heapq


def main() -> None:
    # heappush - add item maintaining heap property
    heap = []
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 5)
    assert heap[0] == 1  # smallest at root

    # heappop - remove and return smallest
    smallest = heapq.heappop(heap)
    assert smallest == 1
    assert heap[0] == 1  # next smallest

    # heapify - convert list to heap in-place
    numbers = [5, 3, 8, 1, 2]
    heapq.heapify(numbers)
    assert numbers[0] == 1  # smallest at root

    # Extract all in sorted order
    sorted_nums = []
    while numbers:
        sorted_nums.append(heapq.heappop(numbers))
    assert sorted_nums == [1, 2, 3, 5, 8]

    # heappushpop - push then pop (more efficient)
    heap = [1, 3, 5]
    heapq.heapify(heap)
    result = heapq.heappushpop(heap, 2)
    assert result == 1  # popped the smallest
    assert 2 in heap  # 2 was added

    # heapreplace - pop then push (more efficient)
    heap = [1, 3, 5]
    heapq.heapify(heap)
    result = heapq.heapreplace(heap, 6)
    assert result == 1  # popped first
    assert 3 == heap[0]  # new smallest

    # nlargest - get n largest elements
    numbers = [1, 8, 3, 9, 4, 2, 7]
    largest = heapq.nlargest(3, numbers)
    assert largest == [9, 8, 7]

    # nsmallest - get n smallest elements
    smallest = heapq.nsmallest(3, numbers)
    assert smallest == [1, 2, 3]

    # With key function
    words = ['programming', 'is', 'fun', 'python']
    longest = heapq.nlargest(2, words, key=len)
    assert longest == ['programming', 'python']

    shortest = heapq.nsmallest(2, words, key=len)
    assert shortest == ['is', 'fun']

    # Max-heap simulation (negate values)
    max_heap = []
    for num in [3, 1, 4, 1, 5]:
        heapq.heappush(max_heap, -num)

    largest = -heapq.heappop(max_heap)
    assert largest == 5
    largest = -heapq.heappop(max_heap)
    assert largest == 4

    # Heap with tuples (priority queue pattern)
    tasks = []
    heapq.heappush(tasks, (2, 'normal task'))
    heapq.heappush(tasks, (1, 'high priority'))
    heapq.heappush(tasks, (3, 'low priority'))

    priority, task = heapq.heappop(tasks)
    assert priority == 1
    assert task == 'high priority'

    # merge - merge sorted iterables
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = list(heapq.merge(list1, list2))
    assert merged == [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    main()
