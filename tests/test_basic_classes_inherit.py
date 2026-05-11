"""Tests for basic class and inheritance modules."""

from pyguide.classes.basic_classes import main as basic_main, Dog
from pyguide.classes.inheritance import main as inherit_main, Animal, Cat, Bird


class TestBasicClassesModule:
    """Tests for the basic classes demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        basic_main()

    def test_class_instantiation(self):
        """Class should be instantiable."""
        dog = Dog("Rex", 5)
        assert dog.name == "Rex"
        assert dog.age == 5

    def test_repr(self):
        """__repr__ should return developer string."""
        dog = Dog("Rex", 5)
        assert repr(dog) == "<Dog name=Rex age=5>"

    def test_str(self):
        """__str__ should return user string."""
        dog = Dog("Rex", 5)
        assert str(dog) == "Rex the dog"

    def test_methods(self):
        """Methods should work correctly."""
        dog = Dog("Rex", 2)
        assert dog.bark() == "Rex says woof!"
        assert dog.get_human_age() == 14

    def test_class_attribute(self):
        """Class attribute should be shared."""
        dog = Dog("Rex", 5)
        assert dog.species == "Canis familiaris"
        assert Dog.species == "Canis familiaris"


class TestInheritanceModule:
    """Tests for the inheritance demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        inherit_main()

    def test_subclass_isinstance(self):
        """Subclass instances should be instances of parent."""
        cat = Cat("Whiskers")
        assert isinstance(cat, Animal)
        assert isinstance(cat, Cat)

    def test_issubclass(self):
        """issubclass should work correctly."""
        assert issubclass(Cat, Animal)
        assert issubclass(Bird, Animal)

    def test_inherited_method(self):
        """Inherited methods should work."""
        cat = Cat("Whiskers")
        assert cat.describe() == "Whiskers is a Cat"

    def test_overridden_method(self):
        """Overridden methods should use subclass version."""
        cat = Cat("Whiskers")
        assert cat.speak() == "Whiskers says meow!"

    def test_subclass_specific_method(self):
        """Subclass-specific methods should work."""
        cat = Cat("Whiskers")
        assert cat.purr() == "Whiskers purrs contentedly"

    def test_super_init(self):
        """super().__init__ should initialize parent attributes."""
        cat = Cat("Whiskers")
        assert cat.species == "Cat"
        assert cat.name == "Whiskers"
