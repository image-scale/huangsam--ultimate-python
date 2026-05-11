"""
Demonstration of Python string operations.

Strings are immutable sequences of characters. Python provides rich
string manipulation methods and formatting capabilities.
"""


def main() -> None:
    # String creation
    single = 'hello'
    double = "world"
    triple = """multi
line"""

    # String concatenation
    combined = single + " " + double
    assert combined == "hello world"

    # String repetition
    repeated = "ab" * 3
    assert repeated == "ababab"

    # Indexing and slicing
    text = "Python"
    assert text[0] == 'P'
    assert text[-1] == 'n'
    assert text[0:2] == 'Py'
    assert text[2:] == 'thon'
    assert text[::-1] == 'nohtyP'

    # String length
    assert len(text) == 6

    # Membership testing
    assert 'th' in text
    assert 'xyz' not in text

    # Case methods
    s = "Hello World"
    assert s.lower() == "hello world"
    assert s.upper() == "HELLO WORLD"
    assert s.title() == "Hello World"
    assert s.capitalize() == "Hello world"
    assert s.swapcase() == "hELLO wORLD"

    # Strip methods
    padded = "  hello  "
    assert padded.strip() == "hello"
    assert padded.lstrip() == "hello  "
    assert padded.rstrip() == "  hello"

    # Strip with specific characters
    dashes = "---hello---"
    assert dashes.strip('-') == "hello"

    # Split and join
    sentence = "one,two,three"
    parts = sentence.split(',')
    assert parts == ['one', 'two', 'three']

    joined = '-'.join(parts)
    assert joined == "one-two-three"

    # Split with whitespace
    words = "hello   world   python".split()
    assert words == ['hello', 'world', 'python']

    # Replace
    text = "hello world"
    assert text.replace('world', 'python') == "hello python"
    assert text.replace('l', 'L', 1) == "heLlo world"  # limit=1

    # Find and index
    text = "hello world"
    assert text.find('o') == 4  # first occurrence
    assert text.find('xyz') == -1  # not found
    assert text.index('o') == 4
    # text.index('xyz') would raise ValueError

    # rfind - find from right
    assert text.rfind('o') == 7

    # Count occurrences
    assert text.count('o') == 2
    assert text.count('l') == 3

    # Starts/ends with
    filename = "document.txt"
    assert filename.startswith('doc')
    assert filename.endswith('.txt')
    assert filename.endswith(('.txt', '.pdf'))  # tuple of options

    # Check string contents
    assert "123".isdigit()
    assert "abc".isalpha()
    assert "abc123".isalnum()
    assert "   ".isspace()
    assert "hello".islower()
    assert "HELLO".isupper()

    # String formatting - f-strings
    name = "Alice"
    age = 30
    message = f"My name is {name} and I am {age} years old"
    assert message == "My name is Alice and I am 30 years old"

    # f-string expressions
    x, y = 10, 20
    assert f"{x} + {y} = {x + y}" == "10 + 20 = 30"

    # Formatting numbers
    pi = 3.14159
    assert f"{pi:.2f}" == "3.14"
    assert f"{1000:,}" == "1,000"
    assert f"{42:05d}" == "00042"  # zero-padded

    # format() method
    template = "Hello, {}!"
    assert template.format("World") == "Hello, World!"

    template = "{name} is {age} years old"
    assert template.format(name="Bob", age=25) == "Bob is 25 years old"

    # % formatting (older style)
    assert "Hello, %s!" % "World" == "Hello, World!"
    assert "%d items" % 5 == "5 items"

    # zfill - pad with zeros
    num = "42"
    assert num.zfill(5) == "00042"

    # center, ljust, rjust
    word = "hi"
    assert word.center(6) == "  hi  "
    assert word.ljust(5) == "hi   "
    assert word.rjust(5) == "   hi"

    # Splitting lines
    multiline = "line1\nline2\nline3"
    lines = multiline.splitlines()
    assert lines == ['line1', 'line2', 'line3']

    # Partition
    email = "user@example.com"
    before, sep, after = email.partition('@')
    assert before == "user"
    assert sep == "@"
    assert after == "example.com"

    # Strings are immutable
    s = "hello"
    # s[0] = 'H'  # would raise TypeError
    new_s = 'H' + s[1:]
    assert new_s == "Hello"
    assert s == "hello"  # original unchanged


if __name__ == "__main__":
    main()
