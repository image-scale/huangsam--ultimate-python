"""
The datetime module provides classes for manipulating dates and times.
Understanding timezone-aware vs naive datetimes is crucial for building
applications that work correctly across different timezones.

This module demonstrates:
1. Creating datetime objects
2. Date and time arithmetic with timedelta
3. Timezone handling (naive vs aware)
4. Formatting and parsing datetime strings
5. Working with dates and times separately
"""

from datetime import datetime, date, time, timedelta, timezone


def create_datetime():
    """Demonstrate creating datetime objects."""
    now = datetime.now()
    assert isinstance(now, datetime)

    specific = datetime(2024, 6, 15, 14, 30, 45)
    assert specific.year == 2024
    assert specific.month == 6
    assert specific.day == 15
    assert specific.hour == 14
    assert specific.minute == 30
    assert specific.second == 45

    from_timestamp = datetime.fromtimestamp(0, tz=timezone.utc)
    assert from_timestamp.year == 1970

    return True


def datetime_arithmetic():
    """Demonstrate datetime arithmetic with timedelta."""
    dt = datetime(2024, 1, 15, 12, 0, 0)

    one_day = timedelta(days=1)
    tomorrow = dt + one_day
    assert tomorrow.day == 16

    one_week = timedelta(weeks=1)
    next_week = dt + one_week
    assert next_week.day == 22

    hours = timedelta(hours=5, minutes=30)
    later = dt + hours
    assert later.hour == 17
    assert later.minute == 30

    delta = datetime(2024, 1, 20) - datetime(2024, 1, 15)
    assert delta.days == 5

    return True


def timezone_handling():
    """Demonstrate timezone-aware vs naive datetimes."""
    naive = datetime.now()
    assert naive.tzinfo is None

    utc_aware = datetime.now(tz=timezone.utc)
    assert utc_aware.tzinfo is timezone.utc

    local_as_utc = naive.replace(tzinfo=timezone.utc)
    assert local_as_utc.tzinfo is timezone.utc

    utc_dt = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    est = timezone(timedelta(hours=-5))
    est_dt = utc_dt.astimezone(est)
    assert est_dt.hour == 7

    return True


def epoch_conversion():
    """Demonstrate conversion to/from Unix timestamps."""
    dt = datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    epoch = dt.timestamp()
    assert epoch == 1704067200.0

    from_epoch = datetime.fromtimestamp(epoch, tz=timezone.utc)
    assert from_epoch == dt

    now_epoch = datetime.now(tz=timezone.utc).timestamp()
    assert now_epoch > 0

    return True


def format_datetime():
    """Demonstrate datetime formatting."""
    dt = datetime(2024, 6, 15, 14, 30, 45)

    iso_format = dt.isoformat()
    assert iso_format == "2024-06-15T14:30:45"

    custom = dt.strftime("%Y-%m-%d %H:%M:%S")
    assert custom == "2024-06-15 14:30:45"

    readable = dt.strftime("%B %d, %Y at %I:%M %p")
    assert readable == "June 15, 2024 at 02:30 PM"

    date_only = dt.strftime("%Y-%m-%d")
    assert date_only == "2024-06-15"

    time_only = dt.strftime("%H:%M:%S")
    assert time_only == "14:30:45"

    return True


def parse_datetime():
    """Demonstrate parsing datetime strings."""
    iso_str = "2024-06-15T14:30:45"
    dt = datetime.fromisoformat(iso_str)
    assert dt.year == 2024
    assert dt.month == 6

    custom_str = "15/06/2024 14:30"
    dt2 = datetime.strptime(custom_str, "%d/%m/%Y %H:%M")
    assert dt2.day == 15
    assert dt2.hour == 14

    date_str = "2024-06-15"
    dt3 = datetime.strptime(date_str, "%Y-%m-%d")
    assert dt3.month == 6

    return True


def date_and_time_objects():
    """Demonstrate separate date and time objects."""
    d = date(2024, 6, 15)
    assert d.year == 2024
    assert d.month == 6
    assert d.day == 15

    today = date.today()
    assert isinstance(today, date)

    t = time(14, 30, 45)
    assert t.hour == 14
    assert t.minute == 30

    dt = datetime.combine(d, t)
    assert dt.year == 2024
    assert dt.hour == 14

    dt2 = datetime(2024, 6, 15, 14, 30, 45)
    assert dt2.date() == d
    assert dt2.time() == t

    return True


def date_comparison():
    """Demonstrate date/time comparison."""
    dt1 = datetime(2024, 1, 1)
    dt2 = datetime(2024, 6, 15)
    dt3 = datetime(2024, 1, 1)

    assert dt1 < dt2
    assert dt2 > dt1
    assert dt1 == dt3
    assert dt1 <= dt3
    assert dt2 >= dt1

    today = date.today()
    yesterday = today - timedelta(days=1)
    assert yesterday < today

    return True


def timedelta_operations():
    """Demonstrate timedelta operations."""
    delta = timedelta(days=5, hours=3, minutes=30)
    assert delta.days == 5
    assert delta.seconds == 3 * 3600 + 30 * 60

    total = delta.total_seconds()
    assert total == 5 * 86400 + 3 * 3600 + 30 * 60

    doubled = delta * 2
    assert doubled.days == 10

    half = delta / 2
    assert half.days == 2

    negative = -delta
    assert negative.days == -6

    return True


def main():
    # Creating datetime objects
    assert create_datetime()

    # Datetime arithmetic
    assert datetime_arithmetic()

    # Timezone handling
    assert timezone_handling()

    # Epoch conversion
    assert epoch_conversion()

    # Formatting
    assert format_datetime()

    # Parsing
    assert parse_datetime()

    # Date and time objects
    assert date_and_time_objects()

    # Comparisons
    assert date_comparison()

    # Timedelta operations
    assert timedelta_operations()

    # Naive datetime has no timezone
    naive = datetime.now()
    assert naive.tzinfo is None

    # UTC datetime has timezone
    utc = datetime.now(timezone.utc)
    assert utc.tzinfo is timezone.utc

    # Cannot subtract naive from aware
    error_raised = False
    try:
        _ = utc - naive
    except TypeError:
        error_raised = True
    assert error_raised


if __name__ == "__main__":
    main()
