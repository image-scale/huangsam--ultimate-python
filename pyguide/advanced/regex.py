"""
Regular expressions (regex) provide powerful pattern matching capabilities
for searching, extracting, and manipulating text. Python's re module
implements Perl-style regular expressions.

This module demonstrates:
1. Basic matching with search, match, and fullmatch
2. Finding all matches with findall and finditer
3. Capture groups and named groups
4. Substitution with sub and subn
5. Splitting strings with split
6. Pattern compilation for efficiency
7. Common regex patterns
"""

import re


def basic_search():
    """Demonstrate re.search for finding patterns anywhere in text."""
    text = "The quick brown fox jumps over the lazy dog"

    match = re.search(r"fox", text)
    assert match is not None
    assert match.group() == "fox"
    assert match.start() == 16
    assert match.end() == 19

    no_match = re.search(r"cat", text)
    assert no_match is None

    return True


def basic_match():
    """Demonstrate re.match for matching at the start of text."""
    text = "Hello World"

    match = re.match(r"Hello", text)
    assert match is not None
    assert match.group() == "Hello"

    no_match = re.match(r"World", text)
    assert no_match is None

    return True


def full_match():
    """Demonstrate re.fullmatch for matching entire string."""
    text = "hello123"

    match = re.fullmatch(r"hello\d+", text)
    assert match is not None

    no_match = re.fullmatch(r"hello", text)
    assert no_match is None

    return True


def find_all():
    """Demonstrate re.findall for finding all matches."""
    text = "cat bat rat sat mat"

    matches = re.findall(r"\w+at", text)
    assert matches == ["cat", "bat", "rat", "sat", "mat"]

    numbers = "Phone: 555-1234, Fax: 555-5678"
    phone_numbers = re.findall(r"\d{3}-\d{4}", numbers)
    assert phone_numbers == ["555-1234", "555-5678"]

    return True


def find_iter():
    """Demonstrate re.finditer for iterating over matches."""
    text = "cat bat rat"

    matches = list(re.finditer(r"\w+at", text))
    assert len(matches) == 3
    assert matches[0].group() == "cat"
    assert matches[1].start() == 4
    assert matches[2].end() == 11

    return True


def capture_groups():
    """Demonstrate capture groups."""
    text = "John Smith, Jane Doe, Bob Wilson"

    pattern = r"(\w+) (\w+)"
    matches = re.findall(pattern, text)
    assert matches == [("John", "Smith"), ("Jane", "Doe"), ("Bob", "Wilson")]

    match = re.search(pattern, text)
    assert match.group(0) == "John Smith"
    assert match.group(1) == "John"
    assert match.group(2) == "Smith"
    assert match.groups() == ("John", "Smith")

    return True


def named_groups():
    """Demonstrate named capture groups."""
    text = "Email: user@example.com"

    pattern = r"(?P<local>\w+)@(?P<domain>\w+\.\w+)"
    match = re.search(pattern, text)

    assert match.group("local") == "user"
    assert match.group("domain") == "example.com"
    assert match.groupdict() == {"local": "user", "domain": "example.com"}

    return True


def substitution():
    """Demonstrate re.sub for substitution."""
    text = "Hello World, Hello Python"

    result = re.sub(r"Hello", "Hi", text)
    assert result == "Hi World, Hi Python"

    result_once = re.sub(r"Hello", "Hi", text, count=1)
    assert result_once == "Hi World, Hello Python"

    def upper_match(m):
        return m.group().upper()

    result_func = re.sub(r"\b\w+\b", upper_match, "hello world")
    assert result_func == "HELLO WORLD"

    return True


def subn_with_count():
    """Demonstrate re.subn which returns replacement count."""
    text = "cat bat rat"

    result, count = re.subn(r"at", "ot", text)
    assert result == "cot bot rot"
    assert count == 3

    return True


def split_text():
    """Demonstrate re.split for splitting text."""
    text = "word1, word2; word3. word4"

    parts = re.split(r"[,;.]\s*", text)
    assert parts == ["word1", "word2", "word3", "word4"]

    limited = re.split(r"[,;.]\s*", text, maxsplit=2)
    assert limited == ["word1", "word2", "word3. word4"]

    return True


def compile_pattern():
    """Demonstrate pattern compilation for efficiency."""
    pattern = re.compile(r"\d+")

    assert pattern.search("abc123def").group() == "123"
    assert pattern.findall("1 2 3 4 5") == ["1", "2", "3", "4", "5"]
    assert pattern.sub("X", "a1b2c3") == "aXbXcX"

    return True


def regex_flags():
    """Demonstrate regex flags."""
    text = "Hello WORLD"

    case_sensitive = re.search(r"world", text)
    assert case_sensitive is None

    case_insensitive = re.search(r"world", text, re.IGNORECASE)
    assert case_insensitive is not None

    multiline_text = "line1\nline2\nline3"
    starts = re.findall(r"^line\d", multiline_text, re.MULTILINE)
    assert starts == ["line1", "line2", "line3"]

    verbose_pattern = re.compile(
        r"""
        \d{3}    # area code
        -        # separator
        \d{4}    # number
        """,
        re.VERBOSE,
    )
    assert verbose_pattern.match("555-1234") is not None

    return True


def common_patterns():
    """Demonstrate common regex patterns."""
    email = "test.user@example.com"
    email_pattern = r"[\w.+-]+@[\w-]+\.[\w.-]+"
    assert re.match(email_pattern, email) is not None

    phone = "123-456-7890"
    phone_pattern = r"\d{3}-\d{3}-\d{4}"
    assert re.match(phone_pattern, phone) is not None

    ip = "192.168.1.1"
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    assert re.match(ip_pattern, ip) is not None

    url = "https://www.example.com/path"
    url_pattern = r"https?://[\w./]+"
    assert re.match(url_pattern, url) is not None

    date = "2024-12-25"
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    assert re.match(date_pattern, date) is not None

    return True


def special_characters():
    """Demonstrate special regex characters."""
    text = "hello $100.00 (price)"

    escaped = re.escape("$100.00")
    assert re.search(escaped, text) is not None

    assert re.search(r"\bprice\b", text) is not None

    assert re.search(r"\s", text) is not None

    assert re.findall(r"\d+", text) == ["100", "00"]

    assert len(re.findall(r"\W", "a1!b2@c3#")) == 3

    return True


def lookahead_lookbehind():
    """Demonstrate lookahead and lookbehind assertions."""
    text = "foo1 bar2 foo3 bar4"

    lookahead = re.findall(r"\w+(?=\d)", text)
    assert lookahead == ["foo", "bar", "foo", "bar"]

    neg_lookahead = re.findall(r"foo(?!\d)", "foo foobar foo1")
    assert len(neg_lookahead) == 2

    lookbehind = re.findall(r"(?<=foo)\d", "foo1 bar2 foo3")
    assert lookbehind == ["1", "3"]

    return True


def main():
    # Basic search
    assert basic_search()

    # Match at start
    assert basic_match()

    # Full match
    assert full_match()

    # Find all matches
    assert find_all()

    # Iterate over matches
    assert find_iter()

    # Capture groups
    assert capture_groups()

    # Named groups
    assert named_groups()

    # Substitution
    assert substitution()

    # Subn with count
    assert subn_with_count()

    # Splitting text
    assert split_text()

    # Compiled patterns
    assert compile_pattern()

    # Regex flags
    assert regex_flags()

    # Common patterns
    assert common_patterns()

    # Special characters
    assert special_characters()

    # Lookahead and lookbehind
    assert lookahead_lookbehind()


if __name__ == "__main__":
    main()
