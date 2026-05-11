"""Tests for mocking module."""

from unittest.mock import Mock, MagicMock, patch, create_autospec

from pyguide.advanced.mocking import (
    main as mocking_main,
    DatabaseConnection,
    EmailService,
    UserNotifier,
    fetch_data_from_api,
    process_user_data,
    basic_mock_usage,
    magic_mock_usage,
    return_value_configuration,
    side_effect_exception,
    side_effect_function,
    patch_function_example,
    patch_object_example,
    property_mock_example,
    call_assertions,
    spec_based_mocking,
    mock_context_manager,
    dependency_injection_testing,
)


class TestMockingModule:
    """Tests for the mocking demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        mocking_main()

    def test_database_connection(self):
        """DatabaseConnection should work normally."""
        db = DatabaseConnection("localhost", 5432)
        assert not db.is_connected
        db.connect()
        assert db.is_connected
        assert db.fetch_user(1)["id"] == 1

    def test_email_service(self):
        """EmailService should return success."""
        service = EmailService()
        assert service.send("test@test.com", "Subject", "Body") is True

    def test_user_notifier(self):
        """UserNotifier should use email service."""
        mock_email = Mock(spec=EmailService)
        mock_email.send.return_value = True
        notifier = UserNotifier(mock_email)
        assert notifier.notify("user@test.com", "Hello") is True

    def test_fetch_data_from_api(self):
        """fetch_data_from_api should return dict."""
        result = fetch_data_from_api("http://example.com")
        assert "url" in result
        assert result["status"] == "ok"

    def test_basic_mock_usage(self):
        """basic_mock_usage should demonstrate Mock."""
        assert basic_mock_usage()

    def test_magic_mock_usage(self):
        """magic_mock_usage should demonstrate MagicMock."""
        assert magic_mock_usage()

    def test_return_value_configuration(self):
        """return_value_configuration should work."""
        assert return_value_configuration()

    def test_side_effect_exception(self):
        """side_effect_exception should demonstrate exceptions."""
        assert side_effect_exception()

    def test_side_effect_function(self):
        """side_effect_function should work."""
        assert side_effect_function()

    def test_patch_function_example(self):
        """patch_function_example should patch functions."""
        assert patch_function_example()

    def test_patch_object_example(self):
        """patch_object_example should patch methods."""
        assert patch_object_example()

    def test_property_mock_example(self):
        """property_mock_example should mock properties."""
        assert property_mock_example()

    def test_call_assertions(self):
        """call_assertions should track calls."""
        assert call_assertions()

    def test_spec_based_mocking(self):
        """spec_based_mocking should enforce spec."""
        assert spec_based_mocking()

    def test_mock_context_manager(self):
        """mock_context_manager should work with with statement."""
        assert mock_context_manager()

    def test_dependency_injection_testing(self):
        """dependency_injection_testing should demonstrate DI."""
        assert dependency_injection_testing()

    def test_mock_call_count(self):
        """Mock should track call count."""
        mock = Mock()
        mock.method()
        mock.method()
        assert mock.method.call_count == 2

    def test_mock_return_value(self):
        """Mock should return configured value."""
        mock = Mock()
        mock.get_value.return_value = 42
        assert mock.get_value() == 42

    def test_mock_side_effect_list(self):
        """Mock should iterate through side_effect list."""
        mock = Mock()
        mock.next_value.side_effect = [1, 2, 3]
        assert mock.next_value() == 1
        assert mock.next_value() == 2
        assert mock.next_value() == 3

    def test_magic_mock_len(self):
        """MagicMock should support __len__."""
        mock = MagicMock()
        mock.__len__.return_value = 10
        assert len(mock) == 10

    def test_patch_decorator(self):
        """patch should work as context manager."""
        from pyguide.advanced import mocking

        with patch.object(mocking, "fetch_data_from_api") as mock:
            mock.return_value = {"patched": True}
            result = mocking.fetch_data_from_api("test")
            assert result == {"patched": True}

    def test_autospec_creates_spec(self):
        """create_autospec should match original interface."""
        mock_db = create_autospec(DatabaseConnection, instance=True)
        mock_db.connect.return_value = True
        assert mock_db.connect() is True
