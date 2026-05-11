"""
The unittest.mock module provides tools for testing code in isolation by
replacing dependencies with mock objects. This is essential for testing
code that depends on external systems, network calls, or complex state.

This module demonstrates:
1. Basic Mock and MagicMock usage
2. Configuring return values and side effects
3. Patching objects and functions
4. Asserting call behavior
5. PropertyMock for mocking properties
6. Spec-based mocking for safety
"""

from unittest.mock import (
    Mock,
    MagicMock,
    patch,
    PropertyMock,
    call,
    create_autospec,
)


class DatabaseConnection:
    """Simulated database connection for demonstration."""

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self._connected = False

    @property
    def is_connected(self) -> bool:
        return self._connected

    def connect(self) -> bool:
        self._connected = True
        return True

    def disconnect(self) -> None:
        self._connected = False

    def execute(self, query: str) -> list:
        if not self._connected:
            raise RuntimeError("Not connected")
        return [{"result": "data"}]

    def fetch_user(self, user_id: int) -> dict:
        if not self._connected:
            raise RuntimeError("Not connected")
        return {"id": user_id, "name": f"User {user_id}"}


class EmailService:
    """Simulated email service."""

    def send(self, to: str, subject: str, body: str) -> bool:
        return True

    def send_bulk(self, recipients: list, subject: str, body: str) -> int:
        return len(recipients)


def fetch_data_from_api(url: str) -> dict:
    """Simulated API call."""
    return {"url": url, "status": "ok"}


def process_user_data(db: DatabaseConnection, user_id: int) -> str:
    """Process user data using database connection."""
    user = db.fetch_user(user_id)
    return f"Processed: {user['name']}"


class UserNotifier:
    """Notifies users via email."""

    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def notify(self, user_email: str, message: str) -> bool:
        return self.email_service.send(user_email, "Notification", message)


def basic_mock_usage():
    """Demonstrate basic Mock usage."""
    mock = Mock()

    mock.some_method()
    mock.some_method.assert_called_once()

    mock.another_method("arg1", "arg2")
    mock.another_method.assert_called_with("arg1", "arg2")

    mock.attr = "value"
    assert mock.attr == "value"

    return True


def magic_mock_usage():
    """Demonstrate MagicMock with magic methods."""
    magic = MagicMock()

    assert len(magic) == 0

    magic.__len__.return_value = 5
    assert len(magic) == 5

    magic.__str__.return_value = "MagicMock object"
    assert str(magic) == "MagicMock object"

    magic.__iter__.return_value = iter([1, 2, 3])
    assert list(magic) == [1, 2, 3]

    return True


def return_value_configuration():
    """Demonstrate configuring return values."""
    mock = Mock()

    mock.get_data.return_value = {"key": "value"}
    assert mock.get_data() == {"key": "value"}

    mock.compute.return_value = 42
    assert mock.compute() == 42

    mock.get_item.side_effect = [1, 2, 3]
    assert mock.get_item() == 1
    assert mock.get_item() == 2
    assert mock.get_item() == 3

    return True


def side_effect_exception():
    """Demonstrate side_effect for exceptions."""
    mock = Mock()

    mock.dangerous_call.side_effect = ValueError("Mock error")

    raised = False
    try:
        mock.dangerous_call()
    except ValueError as e:
        raised = True
        assert "Mock error" in str(e)

    assert raised
    return True


def side_effect_function():
    """Demonstrate side_effect with a function."""
    mock = Mock()

    def custom_side_effect(x):
        return x * 2

    mock.process.side_effect = custom_side_effect
    assert mock.process(5) == 10
    assert mock.process(3) == 6

    return True


def patch_function_example():
    """Demonstrate patching a function."""
    with patch(
        "pyguide.advanced.mocking.fetch_data_from_api"
    ) as mock_fetch:
        mock_fetch.return_value = {"mocked": True}
        result = fetch_data_from_api("http://example.com")
        assert result == {"mocked": True}
        mock_fetch.assert_called_once_with("http://example.com")

    return True


def patch_object_example():
    """Demonstrate patching object methods."""
    db = DatabaseConnection("localhost", 5432)

    with patch.object(db, "fetch_user") as mock_fetch:
        mock_fetch.return_value = {"id": 1, "name": "Mocked User"}
        result = db.fetch_user(1)
        assert result["name"] == "Mocked User"

    return True


def property_mock_example():
    """Demonstrate PropertyMock for mocking properties."""
    db = DatabaseConnection("localhost", 5432)

    with patch.object(
        DatabaseConnection,
        "is_connected",
        new_callable=PropertyMock,
        return_value=True,
    ):
        assert db.is_connected is True

    return True


def call_assertions():
    """Demonstrate call assertions."""
    mock = Mock()

    mock.method("a")
    mock.method("b")
    mock.method("c")

    assert mock.method.call_count == 3

    mock.method.assert_any_call("b")

    expected_calls = [call("a"), call("b"), call("c")]
    mock.method.assert_has_calls(expected_calls)

    return True


def spec_based_mocking():
    """Demonstrate spec-based mocking for safety."""
    mock_db = create_autospec(DatabaseConnection, instance=True)

    mock_db.connect.return_value = True
    mock_db.fetch_user.return_value = {"id": 1, "name": "Test"}

    assert mock_db.connect() is True
    assert mock_db.fetch_user(1)["name"] == "Test"

    try:
        mock_db.nonexistent_method()
        return False
    except AttributeError:
        pass

    return True


def mock_context_manager():
    """Demonstrate mocking context managers."""
    mock_cm = MagicMock()

    mock_cm.__enter__.return_value = "resource"
    mock_cm.__exit__.return_value = False

    with mock_cm as resource:
        assert resource == "resource"

    mock_cm.__enter__.assert_called_once()
    mock_cm.__exit__.assert_called_once()

    return True


def dependency_injection_testing():
    """Demonstrate testing with mocked dependencies."""
    mock_email = Mock(spec=EmailService)
    mock_email.send.return_value = True

    notifier = UserNotifier(mock_email)
    result = notifier.notify("user@example.com", "Hello!")

    assert result is True
    mock_email.send.assert_called_once_with(
        "user@example.com", "Notification", "Hello!"
    )

    return True


def main():
    # Basic mock usage
    assert basic_mock_usage()

    # MagicMock with magic methods
    assert magic_mock_usage()

    # Configuring return values
    assert return_value_configuration()

    # Side effects for exceptions
    assert side_effect_exception()

    # Side effects with functions
    assert side_effect_function()

    # Patching functions
    assert patch_function_example()

    # Patching object methods
    assert patch_object_example()

    # Mocking properties
    assert property_mock_example()

    # Call assertions
    assert call_assertions()

    # Spec-based mocking
    assert spec_based_mocking()

    # Mock context managers
    assert mock_context_manager()

    # Dependency injection testing
    assert dependency_injection_testing()


if __name__ == "__main__":
    main()
