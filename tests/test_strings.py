"""Tests for strings module."""

from pyguide.data_structures.strings import main as strings_main


class TestStringsModule:
    """Tests for the strings demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        strings_main()

    def test_string_concatenation(self):
        """Strings should concatenate with +."""
        assert "hello" + " " + "world" == "hello world"

    def test_string_repetition(self):
        """Strings should repeat with *."""
        assert "ab" * 3 == "ababab"

    def test_string_slicing(self):
        """String slicing should work correctly."""
        s = "Python"
        assert s[0] == 'P'
        assert s[-1] == 'n'
        assert s[0:2] == 'Py'
        assert s[::-1] == 'nohtyP'

    def test_case_methods(self):
        """Case conversion methods should work."""
        s = "Hello World"
        assert s.lower() == "hello world"
        assert s.upper() == "HELLO WORLD"

    def test_strip_methods(self):
        """Strip methods should remove whitespace."""
        s = "  hello  "
        assert s.strip() == "hello"
        assert s.lstrip() == "hello  "
        assert s.rstrip() == "  hello"

    def test_split_join(self):
        """Split and join should work correctly."""
        parts = "a,b,c".split(',')
        assert parts == ['a', 'b', 'c']
        assert '-'.join(parts) == "a-b-c"

    def test_replace(self):
        """Replace should substitute substrings."""
        s = "hello world"
        assert s.replace('world', 'python') == "hello python"

    def test_find(self):
        """Find should locate substrings."""
        s = "hello world"
        assert s.find('o') == 4
        assert s.find('xyz') == -1

    def test_startswith_endswith(self):
        """startswith/endswith should check prefixes/suffixes."""
        s = "document.txt"
        assert s.startswith('doc')
        assert s.endswith('.txt')

    def test_fstring_formatting(self):
        """F-strings should format correctly."""
        name = "Alice"
        age = 30
        assert f"{name} is {age}" == "Alice is 30"
