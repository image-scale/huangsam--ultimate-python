"""Tests for datetime and pattern matching modules."""

from datetime import datetime, date, time, timedelta, timezone

from pyguide.advanced.date_time import (
    main as datetime_main,
    create_datetime,
    datetime_arithmetic,
    timezone_handling,
    epoch_conversion,
    format_datetime,
    parse_datetime,
    date_and_time_objects,
    date_comparison,
    timedelta_operations,
)
from pyguide.advanced.pattern_matching import (
    main as pattern_main,
    match_literal,
    match_http_status,
    match_point,
    match_sequence,
    match_mapping,
    match_class,
    match_with_guard,
    match_or_pattern,
    match_as_pattern,
    match_nested,
    match_command,
    Point,
    Circle,
)


class TestDateTimeModule:
    """Tests for the datetime demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        datetime_main()

    def test_create_datetime(self):
        """create_datetime should work."""
        assert create_datetime()

    def test_datetime_arithmetic(self):
        """datetime_arithmetic should work."""
        assert datetime_arithmetic()

    def test_timezone_handling(self):
        """timezone_handling should work."""
        assert timezone_handling()

    def test_epoch_conversion(self):
        """epoch_conversion should work."""
        assert epoch_conversion()

    def test_format_datetime(self):
        """format_datetime should work."""
        assert format_datetime()

    def test_parse_datetime(self):
        """parse_datetime should work."""
        assert parse_datetime()

    def test_date_and_time_objects(self):
        """date_and_time_objects should work."""
        assert date_and_time_objects()

    def test_date_comparison(self):
        """date_comparison should work."""
        assert date_comparison()

    def test_timedelta_operations(self):
        """timedelta_operations should work."""
        assert timedelta_operations()

    def test_naive_datetime(self):
        """Naive datetime should have no tzinfo."""
        dt = datetime.now()
        assert dt.tzinfo is None

    def test_utc_datetime(self):
        """UTC datetime should have timezone."""
        dt = datetime.now(timezone.utc)
        assert dt.tzinfo is timezone.utc

    def test_timedelta_addition(self):
        """Timedelta should add to datetime."""
        dt = datetime(2024, 1, 1)
        result = dt + timedelta(days=5)
        assert result.day == 6

    def test_datetime_subtraction(self):
        """Subtracting datetimes gives timedelta."""
        dt1 = datetime(2024, 1, 10)
        dt2 = datetime(2024, 1, 1)
        delta = dt1 - dt2
        assert delta.days == 9

    def test_strftime(self):
        """strftime should format datetime."""
        dt = datetime(2024, 6, 15, 14, 30)
        assert dt.strftime("%Y-%m-%d") == "2024-06-15"

    def test_strptime(self):
        """strptime should parse datetime."""
        dt = datetime.strptime("2024-06-15", "%Y-%m-%d")
        assert dt.year == 2024
        assert dt.month == 6


class TestPatternMatchingModule:
    """Tests for the pattern matching demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        pattern_main()

    def test_match_literal(self):
        """match_literal should match literals."""
        assert match_literal(0) == "zero"
        assert match_literal(1) == "one"
        assert match_literal("hello") == "greeting"
        assert match_literal(999) == "unknown"

    def test_match_http_status(self):
        """match_http_status should classify status codes."""
        assert match_http_status(200) == "OK"
        assert match_http_status(404) == "Not Found"
        assert match_http_status(500) == "Internal Server Error"

    def test_match_point(self):
        """match_point should match tuple points."""
        assert match_point((0, 0)) == "origin"
        assert match_point((0, 5)) == "y-axis at 5"
        assert match_point((3, 0)) == "x-axis at 3"
        assert match_point((2, 4)) == "point (2, 4)"

    def test_match_sequence(self):
        """match_sequence should match lists."""
        assert match_sequence([]) == "empty"
        assert match_sequence([1]) == "single: 1"
        assert match_sequence([1, 2]) == "pair: 1, 2"

    def test_match_sequence_rest(self):
        """match_sequence should capture rest."""
        result = match_sequence([1, 2, 3, 4, 5])
        assert "rest: [3, 4, 5]" in result

    def test_match_mapping(self):
        """match_mapping should match dicts."""
        assert "user Alice age 30" in match_mapping(
            {"type": "user", "name": "Alice", "age": 30}
        )

    def test_match_mapping_partial(self):
        """match_mapping should match partial dicts."""
        assert "user Bob" == match_mapping({"type": "user", "name": "Bob"})

    def test_match_class_point(self):
        """match_class should match Point objects."""
        assert match_class(Point(0, 0)) == "origin point"
        assert match_class(Point(5, 5)) == "diagonal point at 5"

    def test_match_class_circle(self):
        """match_class should match Circle objects."""
        assert match_class(Circle(Point(0, 0), 10)) == "centered circle r=10"

    def test_match_with_guard(self):
        """match_with_guard should use guard clauses."""
        assert match_with_guard(-5) == "negative"
        assert match_with_guard(0) == "zero"
        assert match_with_guard(50) == "medium positive"

    def test_match_or_pattern(self):
        """match_or_pattern should match alternatives."""
        assert match_or_pattern(0) == "small"
        assert match_or_pattern(4) == "medium"
        assert match_or_pattern("a") == "early letter"

    def test_match_as_pattern(self):
        """match_as_pattern should capture with as."""
        assert "ascending" in match_as_pattern([1, 5])

    def test_match_nested(self):
        """match_nested should match nested structures."""
        data = {"user": {"name": "Alice", "address": {"city": "NYC"}}}
        assert match_nested(data) == "Alice from NYC"

    def test_match_command(self):
        """match_command should parse commands."""
        assert match_command(["quit"]) == "quitting"
        assert match_command(["go", "north"]) == "going north"
        assert match_command(["take", "sword"]) == "taking sword"

    def test_match_command_guard(self):
        """match_command should use guards."""
        assert match_command(["go", "up"]) == "invalid direction: up"
        assert match_command(["take", "coins", 5]) == "taking 5 coins"
