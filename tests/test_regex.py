"""Tests for regex module."""

import re

from pyguide.advanced.regex import (
    main as regex_main,
    basic_search,
    basic_match,
    full_match,
    find_all,
    find_iter,
    capture_groups,
    named_groups,
    substitution,
    subn_with_count,
    split_text,
    compile_pattern,
    regex_flags,
    common_patterns,
    special_characters,
    lookahead_lookbehind,
)


class TestRegexModule:
    """Tests for the regex demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        regex_main()

    def test_basic_search(self):
        """basic_search should find patterns."""
        assert basic_search()

    def test_basic_match(self):
        """basic_match should match at start."""
        assert basic_match()

    def test_full_match(self):
        """full_match should match entire string."""
        assert full_match()

    def test_find_all(self):
        """find_all should find all matches."""
        assert find_all()

    def test_find_iter(self):
        """find_iter should iterate over matches."""
        assert find_iter()

    def test_capture_groups(self):
        """capture_groups should extract groups."""
        assert capture_groups()

    def test_named_groups(self):
        """named_groups should support named captures."""
        assert named_groups()

    def test_substitution(self):
        """substitution should replace patterns."""
        assert substitution()

    def test_subn_with_count(self):
        """subn_with_count should return count."""
        assert subn_with_count()

    def test_split_text(self):
        """split_text should split by pattern."""
        assert split_text()

    def test_compile_pattern(self):
        """compile_pattern should precompile patterns."""
        assert compile_pattern()

    def test_regex_flags(self):
        """regex_flags should demonstrate flags."""
        assert regex_flags()

    def test_common_patterns(self):
        """common_patterns should validate common formats."""
        assert common_patterns()

    def test_special_characters(self):
        """special_characters should handle special chars."""
        assert special_characters()

    def test_lookahead_lookbehind(self):
        """lookahead_lookbehind should work."""
        assert lookahead_lookbehind()

    def test_search_returns_match_object(self):
        """re.search should return Match object."""
        match = re.search(r"\d+", "abc123def")
        assert match is not None
        assert match.group() == "123"

    def test_findall_with_groups(self):
        """findall with groups returns tuple list."""
        result = re.findall(r"(\w+)@(\w+)", "a@b c@d")
        assert result == [("a", "b"), ("c", "d")]

    def test_sub_with_function(self):
        """sub should accept function."""
        result = re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "a1b2c3")
        assert result == "a2b4c6"

    def test_case_insensitive_flag(self):
        """IGNORECASE flag should ignore case."""
        assert re.search(r"hello", "HELLO", re.IGNORECASE) is not None

    def test_multiline_flag(self):
        """MULTILINE flag should affect ^ and $."""
        text = "a\nb\nc"
        matches = re.findall(r"^\w", text, re.MULTILINE)
        assert matches == ["a", "b", "c"]

    def test_word_boundary(self):
        """Word boundary should match word edges."""
        assert re.search(r"\bword\b", "a word here") is not None
        assert re.search(r"\bword\b", "awordhere") is None

    def test_character_class(self):
        """Character classes should match sets."""
        assert re.findall(r"[aeiou]", "hello") == ["e", "o"]
        assert re.findall(r"[^aeiou]", "hello") == ["h", "l", "l"]

    def test_quantifiers(self):
        """Quantifiers should control repetition."""
        assert re.match(r"a+", "aaa").group() == "aaa"
        assert re.match(r"a*", "").group() == ""
        assert re.match(r"a?", "a").group() == "a"
        assert re.match(r"a{2,3}", "aaaa").group() == "aaa"
