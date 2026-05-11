"""Tests for bitwise operations module."""

from pyguide.syntax.bitwise import main as bitwise_main


class TestBitwiseModule:
    """Tests for the bitwise operations demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        bitwise_main()

    def test_bitwise_and(self):
        """Bitwise AND should set bits only where both operands have 1."""
        assert 0b1100 & 0b1010 == 0b1000
        assert 12 & 10 == 8

    def test_bitwise_or(self):
        """Bitwise OR should set bits where either operand has 1."""
        assert 0b1100 | 0b1010 == 0b1110
        assert 12 | 10 == 14

    def test_bitwise_xor(self):
        """Bitwise XOR should set bits where operands differ."""
        assert 0b1100 ^ 0b1010 == 0b0110
        assert 12 ^ 10 == 6

    def test_bitwise_not(self):
        """Bitwise NOT should invert bits using two's complement."""
        assert ~5 == -6
        assert ~0 == -1

    def test_left_shift(self):
        """Left shift should shift bits left and multiply by power of 2."""
        assert 1 << 3 == 8
        assert 5 << 2 == 20

    def test_right_shift(self):
        """Right shift should shift bits right and divide by power of 2."""
        assert 16 >> 2 == 4
        assert 40 >> 3 == 5

    def test_bin_function(self):
        """bin() should return binary string representation."""
        assert bin(10) == '0b1010'
        assert bin(255) == '0b11111111'

    def test_even_odd_check_with_and(self):
        """Bitwise AND with 1 can check even/odd."""
        assert (10 & 1) == 0  # even
        assert (7 & 1) == 1   # odd

    def test_xor_swap(self):
        """XOR can swap values without temporary variable."""
        x, y = 5, 10
        x = x ^ y
        y = x ^ y
        x = x ^ y
        assert x == 10 and y == 5
