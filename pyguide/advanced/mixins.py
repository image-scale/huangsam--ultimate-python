"""
Demonstration of Python mixin classes.

Mixins are classes that provide methods for other classes through
multiple inheritance, without being intended for standalone use.
"""

from abc import ABC, abstractmethod


class JSONMixin:
    """Mixin that adds JSON serialization capability."""

    def to_json(self) -> str:
        """Convert object to JSON-like string."""
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        pairs = [f'"{k}": "{v}"' for k, v in attrs.items()]
        return "{" + ", ".join(pairs) + "}"


class ComparableMixin:
    """Mixin that adds comparison operators based on a key."""

    def _compare_key(self):
        """Override this to define comparison key."""
        raise NotImplementedError

    def __lt__(self, other):
        return self._compare_key() < other._compare_key()

    def __le__(self, other):
        return self._compare_key() <= other._compare_key()

    def __gt__(self, other):
        return self._compare_key() > other._compare_key()

    def __ge__(self, other):
        return self._compare_key() >= other._compare_key()

    def __eq__(self, other):
        return self._compare_key() == other._compare_key()


class LoggingMixin:
    """Mixin that provides logging capability."""

    _log_messages = []

    def log(self, message: str) -> None:
        """Log a message."""
        LoggingMixin._log_messages.append(f"{self.__class__.__name__}: {message}")

    @classmethod
    def get_logs(cls) -> list:
        """Get all logged messages."""
        return cls._log_messages.copy()

    @classmethod
    def clear_logs(cls) -> None:
        """Clear all logged messages."""
        cls._log_messages.clear()


class Person:
    """Base person class."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class SerializablePerson(Person, JSONMixin):
    """Person that can be serialized to JSON."""
    pass


class ComparablePerson(Person, ComparableMixin):
    """Person that can be compared by age."""

    def _compare_key(self):
        return self.age


class FullFeaturedPerson(Person, JSONMixin, ComparableMixin, LoggingMixin):
    """Person with all mixin features."""

    def _compare_key(self):
        return self.age


def main() -> None:
    # JSONMixin adds to_json
    person = SerializablePerson("Alice", 30)
    json_str = person.to_json()
    assert '"name": "Alice"' in json_str
    assert '"age": "30"' in json_str

    # ComparableMixin adds comparison
    alice = ComparablePerson("Alice", 30)
    bob = ComparablePerson("Bob", 25)
    charlie = ComparablePerson("Charlie", 30)

    assert bob < alice
    assert alice > bob
    assert alice == charlie  # same age
    assert alice >= charlie
    assert bob <= alice

    # Can sort comparable persons
    people = [alice, bob, charlie]
    sorted_people = sorted(people)
    assert sorted_people[0].name == "Bob"

    # LoggingMixin adds logging
    LoggingMixin.clear_logs()

    class LoggingPerson(Person, LoggingMixin):
        pass

    p = LoggingPerson("Dave", 40)
    p.log("Created")
    p.log("Updated")

    logs = LoggingMixin.get_logs()
    assert len(logs) == 2
    assert "LoggingPerson: Created" in logs

    # Multiple mixins combined
    LoggingMixin.clear_logs()
    full = FullFeaturedPerson("Eve", 35)
    full.log("Initialized")

    # Has all capabilities
    assert '"name": "Eve"' in full.to_json()

    eve2 = FullFeaturedPerson("Eve2", 40)
    assert full < eve2

    assert len(LoggingMixin.get_logs()) == 1

    # MRO shows mixin order
    mro = FullFeaturedPerson.__mro__
    assert JSONMixin in mro
    assert ComparableMixin in mro
    assert LoggingMixin in mro


if __name__ == "__main__":
    main()
