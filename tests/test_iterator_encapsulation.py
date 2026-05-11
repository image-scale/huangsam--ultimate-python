"""Tests for iterator and encapsulation modules."""

from pyguide.classes.iterator_classes import (
    main as iterator_main,
    RangeIterator,
    FibonacciIterator,
    countdown_generator,
)
from pyguide.classes.encapsulation import (
    main as encap_main,
    BankAccount,
    Temperature,
)


class TestIteratorClassesModule:
    """Tests for the iterator classes demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        iterator_main()

    def test_range_iterator(self):
        """RangeIterator should work like range."""
        result = list(RangeIterator(0, 5))
        assert result == [0, 1, 2, 3, 4]

    def test_range_iterator_step(self):
        """RangeIterator should support step."""
        result = list(RangeIterator(0, 10, 2))
        assert result == [0, 2, 4, 6, 8]

    def test_fibonacci_iterator(self):
        """FibonacciIterator should generate Fibonacci numbers."""
        result = list(FibonacciIterator(10))
        assert result == [0, 1, 1, 2, 3, 5, 8]

    def test_generator_function(self):
        """Generator function should yield values."""
        result = list(countdown_generator(3))
        assert result == [3, 2, 1, 0]

    def test_iterator_single_use(self):
        """Iterator should be exhausted after one pass."""
        it = RangeIterator(0, 3)
        assert list(it) == [0, 1, 2]
        assert list(it) == []  # exhausted


class TestEncapsulationModule:
    """Tests for the encapsulation demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        encap_main()

    def test_public_attribute(self):
        """Public attributes should be directly accessible."""
        account = BankAccount("Alice")
        assert account.owner == "Alice"

    def test_property_access(self):
        """Properties should provide controlled access."""
        account = BankAccount("Alice", 100)
        assert account.balance == 100

    def test_private_name_mangling(self):
        """Private attributes should be name-mangled."""
        account = BankAccount("Alice")
        try:
            _ = account.__account_number
            assert False
        except AttributeError:
            pass

    def test_deposit_withdraw(self):
        """Deposit and withdraw should modify balance."""
        account = BankAccount("Alice", 100)
        account.deposit(50)
        assert account.balance == 150
        account.withdraw(30)
        assert account.balance == 120

    def test_property_setter(self):
        """Property setter should work."""
        temp = Temperature(0)
        temp.celsius = 100
        assert temp.celsius == 100

    def test_computed_property(self):
        """Computed properties should work."""
        temp = Temperature(100)
        assert temp.fahrenheit == 212
