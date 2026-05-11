"""
Demonstration of Python class basics.

Classes combine data (attributes) and behavior (methods) into
reusable objects. This module covers class definition, instantiation,
and basic object-oriented concepts.
"""

from inspect import isfunction, ismethod, signature


class Dog:
    """Basic dog class demonstrating class fundamentals."""

    species = "Canis familiaris"  # Class attribute

    def __init__(self, name: str, age: int) -> None:
        """Initialize a dog with name and age."""
        self.name = name  # Instance attribute
        self.age = age

    def __repr__(self) -> str:
        """Return developer-friendly representation."""
        return f"<Dog name={self.name} age={self.age}>"

    def __str__(self) -> str:
        """Return user-friendly representation."""
        return f"{self.name} the dog"

    def bark(self) -> str:
        """Make the dog bark."""
        return f"{self.name} says woof!"

    def get_human_age(self) -> int:
        """Calculate approximate human equivalent age."""
        return self.age * 7


def main() -> None:
    # Creating an instance
    buddy = Dog("Buddy", 3)
    assert buddy.name == "Buddy"
    assert buddy.age == 3

    # __repr__ for debugging
    assert repr(buddy) == "<Dog name=Buddy age=3>"

    # __str__ for display
    assert str(buddy) == "Buddy the dog"

    # Calling methods
    assert buddy.bark() == "Buddy says woof!"
    assert buddy.get_human_age() == 21

    # Class attribute is shared
    assert buddy.species == "Canis familiaris"
    assert Dog.species == "Canis familiaris"

    # Multiple instances
    max_dog = Dog("Max", 5)
    assert max_dog.name == "Max"
    assert max_dog.bark() == "Max says woof!"

    # Instances are independent
    buddy.age = 4
    assert buddy.age == 4
    assert max_dog.age == 5  # unchanged

    # Everything is an object in Python
    assert isinstance(buddy, object)
    assert isinstance(Dog, object)
    assert issubclass(Dog, object)

    # Methods are bound to instances
    bark_method = buddy.bark
    assert ismethod(bark_method)
    assert bark_method.__self__ == buddy

    # Method signature
    params = signature(bark_method).parameters
    assert len(params) == 0  # self is implicit

    # Class functions vs instance methods
    assert isfunction(Dog.bark)  # unbound
    assert ismethod(buddy.bark)  # bound

    # type() and isinstance()
    assert type(buddy) is Dog
    assert isinstance(buddy, Dog)

    # Dynamic attribute assignment
    buddy.color = "brown"
    assert buddy.color == "brown"
    assert not hasattr(max_dog, 'color')

    # getattr and setattr
    assert getattr(buddy, 'name') == "Buddy"
    setattr(buddy, 'name', "Buddy Jr")
    assert buddy.name == "Buddy Jr"

    # hasattr
    assert hasattr(buddy, 'name')
    assert not hasattr(buddy, 'weight')


if __name__ == "__main__":
    main()
