"""
Demonstration of Python abstract classes.

Abstract classes define interfaces that subclasses must implement.
They use the ABC (Abstract Base Class) module and cannot be instantiated directly.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    def __init__(self, name: str) -> None:
        """Initialize shape with a name."""
        self.name = name

    @abstractmethod
    def area(self) -> float:
        """Calculate the area. Must be implemented by subclasses."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter. Must be implemented by subclasses."""
        raise NotImplementedError

    def describe(self) -> str:
        """Describe the shape (concrete method)."""
        return f"{self.name}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Rectangle(Shape):
    """Concrete rectangle class."""

    def __init__(self, width: float, height: float) -> None:
        """Initialize rectangle with dimensions."""
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate rectangle area."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Concrete circle class."""

    PI = 3.14159

    def __init__(self, radius: float) -> None:
        """Initialize circle with radius."""
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        """Calculate circle area."""
        return self.PI * self.radius ** 2

    def perimeter(self) -> float:
        """Calculate circle circumference."""
        return 2 * self.PI * self.radius


def main() -> None:
    # Cannot instantiate abstract class
    try:
        Shape("test")
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "abstract" in str(e).lower()

    # Can instantiate concrete subclasses
    rect = Rectangle(4, 5)
    assert rect.area() == 20
    assert rect.perimeter() == 18

    circle = Circle(3)
    assert 28 < circle.area() < 29  # ~28.27
    assert 18 < circle.perimeter() < 19  # ~18.85

    # Concrete method from abstract class works
    desc = rect.describe()
    assert "Rectangle" in desc
    assert "area=20" in desc

    # isinstance works with abstract class
    assert isinstance(rect, Shape)
    assert isinstance(circle, Shape)

    # issubclass works
    assert issubclass(Rectangle, Shape)
    assert issubclass(Circle, Shape)
    assert issubclass(Shape, ABC)

    # Polymorphism - same interface, different implementations
    shapes = [Rectangle(2, 3), Circle(2), Rectangle(5, 5)]
    total_area = sum(shape.area() for shape in shapes)
    assert 43 < total_area < 44  # 6 + ~12.57 + 25

    # Incomplete subclass cannot be instantiated
    class PartialShape(Shape):
        def area(self) -> float:
            return 0
        # Missing perimeter()

    try:
        PartialShape("test")
        assert False, "Should have raised TypeError"
    except TypeError:
        pass


if __name__ == "__main__":
    main()
