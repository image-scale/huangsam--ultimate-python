"""
Demonstration of Python loop constructs.

Loops allow code to repeat execution. Python provides for loops for
iterating over sequences and while loops for condition-based repetition.
"""


def main() -> None:
    # For loop with range() - generates sequence of numbers
    total = 0
    for i in range(5):  # 0, 1, 2, 3, 4
        total += i
    assert total == 10  # 0+1+2+3+4 = 10

    # Range with start and end
    total = 0
    for i in range(1, 6):  # 1, 2, 3, 4, 5
        total += i
    assert total == 15

    # Range with step
    even_sum = 0
    for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
        even_sum += i
    assert even_sum == 20

    # For loop over a list
    fruits = ["apple", "banana", "cherry"]
    collected = []
    for fruit in fruits:
        collected.append(fruit.upper())
    assert collected == ["APPLE", "BANANA", "CHERRY"]

    # For loop over a string
    chars = []
    for char in "hello":
        chars.append(char)
    assert chars == ["h", "e", "l", "l", "o"]

    # While loop - continues while condition is true
    count = 0
    while count < 5:
        count += 1
    assert count == 5

    # While loop with accumulator
    total = 0
    n = 1
    while n <= 10:
        total += n
        n += 1
    assert total == 55  # sum of 1 to 10

    # Break statement - exits the loop early
    found_at = -1
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i, num in enumerate(numbers):
        if num == 7:
            found_at = i
            break
    assert found_at == 6

    # Continue statement - skips to next iteration
    odd_numbers = []
    for num in range(10):
        if num % 2 == 0:
            continue  # skip even numbers
        odd_numbers.append(num)
    assert odd_numbers == [1, 3, 5, 7, 9]

    # Enumerate - get index and value together
    names = ["Alice", "Bob", "Charlie"]
    indexed = []
    for idx, name in enumerate(names):
        indexed.append((idx, name))
    assert indexed == [(0, "Alice"), (1, "Bob"), (2, "Charlie")]

    # Enumerate with custom start index
    indexed = []
    for idx, name in enumerate(names, start=1):
        indexed.append((idx, name))
    assert indexed == [(1, "Alice"), (2, "Bob"), (3, "Charlie")]

    # Zip - iterate over multiple sequences in parallel
    numbers = [1, 2, 3]
    letters = ["a", "b", "c"]
    paired = []
    for num, letter in zip(numbers, letters):
        paired.append((num, letter))
    assert paired == [(1, "a"), (2, "b"), (3, "c")]

    # Zip stops at the shortest sequence
    short = [1, 2]
    long = ["a", "b", "c"]
    result = list(zip(short, long))
    assert result == [(1, "a"), (2, "b")]

    # Nested loops
    matrix = []
    for row in range(3):
        for col in range(3):
            matrix.append((row, col))
    assert len(matrix) == 9
    assert matrix[0] == (0, 0)
    assert matrix[-1] == (2, 2)

    # For-else clause - else runs if loop completes without break
    search_list = [1, 2, 3, 4, 5]
    found = False
    for item in search_list:
        if item == 10:
            found = True
            break
    else:
        found = False  # No break occurred
    assert found is False

    # While-else clause
    n = 5
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    else:
        completed = True
    assert factorial == 120
    assert completed is True


if __name__ == "__main__":
    main()
