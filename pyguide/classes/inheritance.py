"""
Demonstration of Python class inheritance.

Inheritance allows classes to reuse code from parent classes while
adding or modifying functionality. This module covers single inheritance,
method overriding, and the super() function.
"""


class Animal:
    """Base animal class."""

    def __init__(self, name: str, species: str) -> None:
        """Initialize animal with name and species."""
        self.name = name
        self.species = species

    def __repr__(self) -> str:
        """Return developer representation."""
        return f"<Animal name={self.name} species={self.species}>"

    def __str__(self) -> str:
        """Return user representation."""
        return f"{self.name} ({self.species})"

    def speak(self) -> str:
        """Make the animal speak."""
        return f"{self.name} makes a sound"

    def describe(self) -> str:
        """Describe the animal."""
        return f"{self.name} is a {self.species}"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def __init__(self, name: str, indoor: bool = True) -> None:
        """Initialize cat with name and indoor status."""
        super().__init__(name, "Cat")
        self.indoor = indoor

    def __repr__(self) -> str:
        """Return developer representation."""
        return f"<Cat name={self.name} indoor={self.indoor}>"

    def speak(self) -> str:
        """Cats meow."""
        return f"{self.name} says meow!"

    def purr(self) -> str:
        """Cats can purr."""
        return f"{self.name} purrs contentedly"


class Bird(Animal):
    """Bird class that inherits from Animal."""

    def __init__(self, name: str, can_fly: bool = True) -> None:
        """Initialize bird with name and flight ability."""
        super().__init__(name, "Bird")
        self.can_fly = can_fly

    def __repr__(self) -> str:
        """Return developer representation."""
        return f"<Bird name={self.name} can_fly={self.can_fly}>"

    def speak(self) -> str:
        """Birds chirp."""
        return f"{self.name} says chirp!"

    def fly(self) -> str:
        """Attempt to fly."""
        if self.can_fly:
            return f"{self.name} soars through the sky"
        return f"{self.name} cannot fly"


def main() -> None:
    # Create instances
    whiskers = Cat("Whiskers")
    tweety = Bird("Tweety")
    penguin = Bird("Pingu", can_fly=False)

    # Subclass instances are instances of parent class
    assert isinstance(whiskers, Animal)
    assert isinstance(whiskers, Cat)
    assert isinstance(tweety, Animal)
    assert isinstance(tweety, Bird)

    # Subclass check
    assert issubclass(Cat, Animal)
    assert issubclass(Bird, Animal)
    assert not issubclass(Cat, Bird)

    # Inherited attribute
    assert whiskers.species == "Cat"
    assert tweety.species == "Bird"

    # Inherited method
    assert whiskers.describe() == "Whiskers is a Cat"
    assert tweety.describe() == "Tweety is a Bird"

    # Overridden method
    assert whiskers.speak() == "Whiskers says meow!"
    assert tweety.speak() == "Tweety says chirp!"

    # Subclass-specific methods
    assert whiskers.purr() == "Whiskers purrs contentedly"
    assert tweety.fly() == "Tweety soars through the sky"
    assert penguin.fly() == "Pingu cannot fly"

    # Subclass-specific attributes
    assert whiskers.indoor is True
    assert tweety.can_fly is True
    assert penguin.can_fly is False

    # __repr__ overridden
    assert repr(whiskers) == "<Cat name=Whiskers indoor=True>"
    assert repr(tweety) == "<Bird name=Tweety can_fly=True>"

    # __str__ inherited from Animal
    assert str(whiskers) == "Whiskers (Cat)"
    assert str(tweety) == "Tweety (Bird)"

    # type() shows actual class
    assert type(whiskers) is Cat
    assert type(whiskers) is not Animal

    # Method Resolution Order (MRO)
    assert Cat.__mro__ == (Cat, Animal, object)
    assert Bird.__mro__ == (Bird, Animal, object)


if __name__ == "__main__":
    main()
