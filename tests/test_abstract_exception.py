"""Tests for abstract class and exception class modules."""

from abc import ABC

from pyguide.classes.abstract_classes import (
    main as abstract_main,
    Shape,
    Rectangle,
    Circle,
)
from pyguide.classes.exception_classes import (
    main as exception_main,
    ValidationError,
    AgeValidationError,
    EmailValidationError,
    ResourceNotFoundError,
    validate_age,
    validate_email,
)


class TestAbstractClassesModule:
    """Tests for the abstract classes demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        abstract_main()

    def test_cannot_instantiate_abstract(self):
        """Abstract class should not be instantiable."""
        try:
            Shape("test")
            assert False
        except TypeError:
            pass

    def test_concrete_subclass(self):
        """Concrete subclass should be instantiable."""
        rect = Rectangle(4, 5)
        assert rect.area() == 20
        assert rect.perimeter() == 18

    def test_isinstance_with_abstract(self):
        """isinstance should work with abstract base."""
        rect = Rectangle(4, 5)
        assert isinstance(rect, Shape)

    def test_issubclass_abc(self):
        """issubclass should work correctly."""
        assert issubclass(Rectangle, Shape)
        assert issubclass(Shape, ABC)


class TestExceptionClassesModule:
    """Tests for the exception classes demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        exception_main()

    def test_exception_inheritance(self):
        """Custom exceptions should inherit correctly."""
        assert issubclass(ValidationError, ValueError)
        assert issubclass(AgeValidationError, ValidationError)

    def test_age_validation_error(self):
        """AgeValidationError should have age attribute."""
        try:
            validate_age(-1)
            assert False
        except AgeValidationError as e:
            assert e.age == -1

    def test_email_validation_error(self):
        """EmailValidationError should have email attribute."""
        try:
            validate_email("bad")
            assert False
        except EmailValidationError as e:
            assert e.email == "bad"

    def test_resource_not_found(self):
        """ResourceNotFoundError should have resource info."""
        e = ResourceNotFoundError("User", "123")
        assert e.resource_type == "User"
        assert e.resource_id == "123"

    def test_catch_parent_exception(self):
        """Should be able to catch parent exception type."""
        try:
            validate_age(-1)
        except ValidationError:
            pass  # Caught as parent type
