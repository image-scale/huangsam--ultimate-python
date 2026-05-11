"""
Demonstration of Python bitwise operators.

Bitwise operators manipulate integers at the binary level, operating on
individual bits. These are useful for low-level programming, flags,
and efficient algorithms.
"""


def main() -> None:
    # Bitwise AND (&) - bits are 1 only if both operands have 1
    a = 0b1100  # 12 in decimal
    b = 0b1010  # 10 in decimal
    result = a & b
    assert result == 0b1000  # 8 in decimal
    assert result == 8

    # Bitwise OR (|) - bits are 1 if either operand has 1
    result = a | b
    assert result == 0b1110  # 14 in decimal
    assert result == 14

    # Bitwise XOR (^) - bits are 1 if operands differ
    result = a ^ b
    assert result == 0b0110  # 6 in decimal
    assert result == 6

    # Bitwise NOT (~) - inverts all bits (two's complement)
    x = 5  # 0b0101
    result = ~x
    assert result == -6  # two's complement: -(x+1)

    # Left shift (<<) - shifts bits left, fills with zeros
    x = 1
    assert x << 1 == 2   # 0b0001 -> 0b0010
    assert x << 2 == 4   # 0b0001 -> 0b0100
    assert x << 3 == 8   # 0b0001 -> 0b1000

    # Left shift is equivalent to multiplying by powers of 2
    assert 5 << 3 == 5 * (2 ** 3)
    assert 5 << 3 == 40

    # Right shift (>>) - shifts bits right, discards bits
    x = 16  # 0b10000
    assert x >> 1 == 8   # 0b01000
    assert x >> 2 == 4   # 0b00100
    assert x >> 3 == 2   # 0b00010
    assert x >> 4 == 1   # 0b00001
    assert x >> 5 == 0   # 0b00000

    # Right shift is equivalent to integer division by powers of 2
    assert 40 >> 3 == 40 // (2 ** 3)
    assert 40 >> 3 == 5

    # bin() shows binary representation with '0b' prefix
    assert bin(10) == '0b1010'
    assert bin(255) == '0b11111111'

    # Practical example: checking if a number is even or odd using AND
    def is_even(n):
        return (n & 1) == 0

    assert is_even(10) is True
    assert is_even(7) is False

    # Practical example: using XOR to swap values without temp variable
    x, y = 5, 10
    x = x ^ y
    y = x ^ y
    x = x ^ y
    assert x == 10 and y == 5

    # Practical example: using OR to set a flag bit
    flags = 0b0000
    enable_read = 0b0001
    enable_write = 0b0010
    flags = flags | enable_read
    assert flags == 0b0001
    flags = flags | enable_write
    assert flags == 0b0011

    # Practical example: using AND to check a flag bit
    assert (flags & enable_read) != 0
    assert (flags & enable_write) != 0
    assert (flags & 0b0100) == 0  # execute flag not set


if __name__ == "__main__":
    main()
