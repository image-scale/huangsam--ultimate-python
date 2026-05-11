"""
Structural pattern matching (Python 3.10+) allows matching complex data
structures against patterns and extracting values. It uses the match/case
syntax and provides powerful pattern types including literals, sequences,
mappings, and class patterns.

This module demonstrates:
1. Literal pattern matching
2. Sequence patterns (tuples and lists)
3. Mapping patterns (dictionaries)
4. Class patterns with attribute matching
5. Guard clauses for additional conditions
6. OR patterns and AS patterns
7. Wildcard patterns
"""


def match_literal(value) -> str:
    """Match against literal values."""
    match value:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case True:
            return "true"
        case False:
            return "false"
        case "hello":
            return "greeting"
        case _:
            return "unknown"


def match_http_status(status: int) -> str:
    """Match HTTP status codes."""
    match status:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 204:
            return "No Content"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown"


def match_point(point) -> str:
    """Match tuple patterns for 2D points."""
    match point:
        case (0, 0):
            return "origin"
        case (0, y):
            return f"y-axis at {y}"
        case (x, 0):
            return f"x-axis at {x}"
        case (x, y):
            return f"point ({x}, {y})"
        case _:
            return "not a point"


def match_sequence(seq) -> str:
    """Match list/sequence patterns."""
    match seq:
        case []:
            return "empty"
        case [x]:
            return f"single: {x}"
        case [x, y]:
            return f"pair: {x}, {y}"
        case [first, second, *rest]:
            return f"first: {first}, second: {second}, rest: {rest}"
        case _:
            return "not a sequence"


def match_mapping(data: dict) -> str:
    """Match dictionary patterns."""
    match data:
        case {"type": "user", "name": name, "age": age}:
            return f"user {name} age {age}"
        case {"type": "user", "name": name}:
            return f"user {name}"
        case {"type": "product", "name": name, "price": price}:
            return f"product {name} ${price}"
        case {"type": t}:
            return f"unknown type: {t}"
        case {}:
            return "empty dict"
        case _:
            return "not a dict"


class Point:
    """2D point class for pattern matching."""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:
    """Circle class for pattern matching."""

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


def match_class(obj) -> str:
    """Match class patterns with attribute extraction."""
    match obj:
        case Point(x=0, y=0):
            return "origin point"
        case Point(x=0, y=y):
            return f"y-axis point at {y}"
        case Point(x=x, y=0):
            return f"x-axis point at {x}"
        case Point(x=x, y=y) if x == y:
            return f"diagonal point at {x}"
        case Point(x=x, y=y):
            return f"point at ({x}, {y})"
        case Circle(center=Point(x=0, y=0), radius=r):
            return f"centered circle r={r}"
        case Circle(center=c, radius=r):
            return f"circle at ({c.x}, {c.y}) r={r}"
        case _:
            return "unknown shape"


def match_with_guard(value) -> str:
    """Match with guard clauses (if conditions)."""
    match value:
        case x if x < 0:
            return "negative"
        case x if x == 0:
            return "zero"
        case x if x < 10:
            return "small positive"
        case x if x < 100:
            return "medium positive"
        case x:
            return "large positive"


def match_or_pattern(value) -> str:
    """Match using OR patterns (|)."""
    match value:
        case 0 | 1 | 2:
            return "small"
        case 3 | 4 | 5:
            return "medium"
        case "a" | "b" | "c":
            return "early letter"
        case _:
            return "other"


def match_as_pattern(data) -> str:
    """Match using AS pattern for capture."""
    match data:
        case [x, y] as pair if x < y:
            return f"ascending pair: {pair}"
        case [x, y] as pair:
            return f"pair: {pair}"
        case _:
            return "not a pair"


def match_nested(data) -> str:
    """Match nested structures."""
    match data:
        case {"user": {"name": name, "address": {"city": city}}}:
            return f"{name} from {city}"
        case {"user": {"name": name}}:
            return f"user {name}"
        case [[a, b], [c, d]]:
            return f"2x2 matrix: {a},{b},{c},{d}"
        case _:
            return "unknown structure"


def match_command(cmd: list) -> str:
    """Match command patterns with guards."""
    match cmd:
        case ["quit"]:
            return "quitting"
        case ["go", direction] if direction in ("north", "south", "east", "west"):
            return f"going {direction}"
        case ["go", direction]:
            return f"invalid direction: {direction}"
        case ["take", item, count] if isinstance(count, int) and count > 0:
            return f"taking {count} {item}"
        case ["take", item]:
            return f"taking {item}"
        case _:
            return "unknown command"


def main():
    # Literal matching
    assert match_literal(0) == "zero"
    assert match_literal(1) == "one"
    assert match_literal("hello") == "greeting"
    assert match_literal(999) == "unknown"

    # HTTP status matching
    assert match_http_status(200) == "OK"
    assert match_http_status(404) == "Not Found"
    assert match_http_status(999) == "Unknown"

    # Point/tuple matching
    assert match_point((0, 0)) == "origin"
    assert match_point((0, 5)) == "y-axis at 5"
    assert match_point((3, 0)) == "x-axis at 3"
    assert match_point((2, 4)) == "point (2, 4)"

    # Sequence matching
    assert match_sequence([]) == "empty"
    assert match_sequence([1]) == "single: 1"
    assert match_sequence([1, 2]) == "pair: 1, 2"
    assert match_sequence([1, 2, 3, 4]) == "first: 1, second: 2, rest: [3, 4]"

    # Dictionary matching
    assert match_mapping({"type": "user", "name": "Alice", "age": 30}) == "user Alice age 30"
    assert match_mapping({"type": "user", "name": "Bob"}) == "user Bob"
    assert match_mapping({"type": "product", "name": "Item", "price": 100}) == "product Item $100"
    assert match_mapping({"type": "unknown"}) == "unknown type: unknown"

    # Class matching
    assert match_class(Point(0, 0)) == "origin point"
    assert match_class(Point(0, 5)) == "y-axis point at 5"
    assert match_class(Point(5, 5)) == "diagonal point at 5"
    assert match_class(Point(3, 7)) == "point at (3, 7)"
    assert match_class(Circle(Point(0, 0), 10)) == "centered circle r=10"
    assert match_class(Circle(Point(1, 2), 5)) == "circle at (1, 2) r=5"

    # Guard clauses
    assert match_with_guard(-5) == "negative"
    assert match_with_guard(0) == "zero"
    assert match_with_guard(5) == "small positive"
    assert match_with_guard(50) == "medium positive"
    assert match_with_guard(500) == "large positive"

    # OR patterns
    assert match_or_pattern(0) == "small"
    assert match_or_pattern(4) == "medium"
    assert match_or_pattern("b") == "early letter"
    assert match_or_pattern(100) == "other"

    # AS patterns
    assert match_as_pattern([1, 5]) == "ascending pair: [1, 5]"
    assert match_as_pattern([5, 1]) == "pair: [5, 1]"

    # Nested matching
    assert match_nested({"user": {"name": "Alice", "address": {"city": "NYC"}}}) == "Alice from NYC"
    assert match_nested([[1, 2], [3, 4]]) == "2x2 matrix: 1,2,3,4"

    # Command matching
    assert match_command(["quit"]) == "quitting"
    assert match_command(["go", "north"]) == "going north"
    assert match_command(["go", "up"]) == "invalid direction: up"
    assert match_command(["take", "sword"]) == "taking sword"
    assert match_command(["take", "coins", 5]) == "taking 5 coins"


if __name__ == "__main__":
    main()
