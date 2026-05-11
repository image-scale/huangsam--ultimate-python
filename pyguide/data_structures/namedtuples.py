"""
Demonstration of Python's collections.namedtuple.

Named tuples provide named fields while remaining immutable and
memory-efficient like regular tuples.
"""

from collections import namedtuple


def main() -> None:
    # Creating a named tuple class
    Point = namedtuple('Point', ['x', 'y'])

    # Creating instances
    p = Point(3, 4)
    assert p.x == 3
    assert p.y == 4

    # Can also use positional indexing
    assert p[0] == 3
    assert p[1] == 4

    # Unpack like regular tuples
    x, y = p
    assert x == 3 and y == 4

    # Named tuples are immutable
    try:
        p.x = 10
        assert False, "Should have raised AttributeError"
    except AttributeError:
        pass

    # Alternative field specification
    Person = namedtuple('Person', 'name age city')  # space-separated
    person = Person('Alice', 30, 'NYC')
    assert person.name == 'Alice'
    assert person.age == 30

    # Creating from iterable
    data = ['Bob', 25, 'LA']
    p2 = Person._make(data)
    assert p2.name == 'Bob'

    # Converting to dict
    d = person._asdict()
    assert d == {'name': 'Alice', 'age': 30, 'city': 'NYC'}

    # Creating modified copy with _replace
    older = person._replace(age=31)
    assert older.age == 31
    assert person.age == 30  # original unchanged

    # Access field names
    assert Person._fields == ('name', 'age', 'city')

    # Named tuples are a subclass of tuple
    assert isinstance(person, tuple)

    # Can be used as dict keys
    points = {Point(0, 0): 'origin', Point(1, 0): 'unit x'}
    assert points[Point(0, 0)] == 'origin'

    # Default values with _field_defaults (Python 3.7+)
    Employee = namedtuple('Employee', ['name', 'dept', 'salary'],
                          defaults=['Engineering', 50000])
    emp = Employee('Charlie')
    assert emp.name == 'Charlie'
    assert emp.dept == 'Engineering'
    assert emp.salary == 50000

    # Only provide some defaults
    emp2 = Employee('Diana', 'Sales')
    assert emp2.dept == 'Sales'
    assert emp2.salary == 50000

    # Named tuple comparison
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)
    assert p1 == p2
    assert p1 != p3

    # repr shows readable output
    point = Point(10, 20)
    assert repr(point) == 'Point(x=10, y=20)'

    # Length works
    assert len(point) == 2

    # Iteration works
    coords = list(point)
    assert coords == [10, 20]


if __name__ == "__main__":
    main()
