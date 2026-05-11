"""
Demonstration of Python encapsulation.

Encapsulation controls access to class internals. Python uses naming
conventions: _single_underscore for internal, __double_underscore
for name mangling.
"""


class BankAccount:
    """Bank account demonstrating encapsulation patterns."""

    def __init__(self, owner: str, initial_balance: float = 0) -> None:
        self.owner = owner  # Public
        self._balance = initial_balance  # Protected (convention)
        self.__account_number = f"ACC{id(self)}"  # Private (name mangled)

    @property
    def balance(self) -> float:
        """Read-only access to balance via property."""
        return self._balance

    @property
    def account_number(self) -> str:
        """Read-only access to account number."""
        return self.__account_number

    def deposit(self, amount: float) -> None:
        """Deposit money (validates amount)."""
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> float:
        """Withdraw money (validates balance)."""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return amount


class Temperature:
    """Temperature class demonstrating property setters."""

    def __init__(self, celsius: float = 0) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Get temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Set temperature in Celsius (validates range)."""
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Get temperature in Fahrenheit (computed)."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Set temperature via Fahrenheit."""
        celsius = (value - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = celsius


def main() -> None:
    # Public attribute - direct access
    account = BankAccount("Alice", 100)
    assert account.owner == "Alice"

    # Protected attribute - accessible but convention says don't
    assert account._balance == 100  # Works but discouraged

    # Private attribute - name mangled
    try:
        _ = account.__account_number
        assert False, "Should have raised AttributeError"
    except AttributeError:
        pass

    # Access via property
    assert account.balance == 100
    assert account.account_number.startswith("ACC")

    # Can still access mangled name if you know the pattern
    mangled_name = f"_BankAccount__account_number"
    assert hasattr(account, mangled_name)

    # Using methods to modify protected state
    account.deposit(50)
    assert account.balance == 150

    withdrawn = account.withdraw(30)
    assert withdrawn == 30
    assert account.balance == 120

    # Validation in methods
    try:
        account.deposit(-10)
        assert False
    except ValueError as e:
        assert "positive" in str(e)

    try:
        account.withdraw(1000)
        assert False
    except ValueError as e:
        assert "Insufficient" in str(e)

    # Property with setter
    temp = Temperature(20)
    assert temp.celsius == 20
    assert temp.fahrenheit == 68

    # Set via Celsius
    temp.celsius = 100
    assert temp.fahrenheit == 212

    # Set via Fahrenheit
    temp.fahrenheit = 32
    assert temp.celsius == 0

    # Validation in setter
    try:
        temp.celsius = -300
        assert False
    except ValueError as e:
        assert "absolute zero" in str(e)

    # Property cannot be deleted by default
    try:
        del temp.celsius
        assert False
    except AttributeError:
        pass


if __name__ == "__main__":
    main()
