"""
Demonstration of Python's walrus operator (assignment expressions).

The walrus operator := allows assignment within expressions, reducing
code duplication and making certain patterns more concise. Introduced
in Python 3.8 (PEP 572).
"""


def main() -> None:
    # Basic walrus operator - assigns and returns the value
    if (n := 10) > 5:
        result = n * 2
    assert n == 10
    assert result == 20

    # Without walrus operator, you'd need two statements:
    # n = 10
    # if n > 5:
    #     result = n * 2

    # Walrus in a while loop - read and check in one expression
    data = [1, 2, 3, 4, 5]
    index = 0
    total = 0
    while (value := data[index] if index < len(data) else None) is not None:
        total += value
        index += 1
    assert total == 15

    # Walrus in list comprehension - compute once, use twice
    numbers = [1, 2, 3, 4, 5]
    results = [(x, squared) for x in numbers if (squared := x ** 2) > 5]
    assert results == [(3, 9), (4, 16), (5, 25)]

    # Walrus for avoiding repeated function calls
    def expensive_calculation(x):
        return x * x + 2 * x + 1

    values = [1, 2, 3, 4, 5]
    filtered = [y for x in values if (y := expensive_calculation(x)) > 10]
    assert filtered == [16, 25, 36]

    # Walrus in conditional expression
    def get_config():
        return {"debug": True}

    config = get_config()
    message = "Debug on" if (debug := config.get("debug")) else "Debug off"
    assert debug is True
    assert message == "Debug on"

    # Walrus in regex matching
    import re
    text = "Hello 123 World"
    if (match := re.search(r"\d+", text)) is not None:
        number = match.group()
    assert number == "123"

    # Walrus for processing input iteratively
    lines = ["line1", "line2", "", "line4"]
    processed = []
    idx = 0
    while idx < len(lines) and (line := lines[idx]):
        processed.append(line.upper())
        idx += 1
    assert processed == ["LINE1", "LINE2"]

    # Walrus to avoid nested conditions
    data = {"user": {"name": "Alice", "age": 30}}

    if (user := data.get("user")) and (name := user.get("name")):
        greeting = f"Hello, {name}!"
    else:
        greeting = "Hello, guest!"
    assert greeting == "Hello, Alice!"


if __name__ == "__main__":
    main()
