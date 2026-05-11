"""Tests for the module runner."""

import sys
from inspect import signature
from io import StringIO
from unittest.mock import patch

import pytest

from pyguide import __name__ as pkg_name, __path__ as pkg_path
from runner import (
    ENTRY_POINT,
    format_bold,
    format_success,
    run_all_modules,
    main,
)


class TestPackageImport:
    """Tests for package import functionality."""

    def test_package_has_name(self):
        """Package should have __name__ attribute."""
        assert pkg_name == "pyguide"

    def test_package_has_path(self):
        """Package should have __path__ attribute."""
        assert pkg_path is not None
        assert len(pkg_path) > 0


class TestFormatFunctions:
    """Tests for ANSI formatting functions."""

    def test_format_bold_adds_ansi_codes(self):
        """format_bold should wrap text in bold ANSI codes."""
        result = format_bold("test")
        assert "\033[1m" in result
        assert "\033[0m" in result
        assert "test" in result

    def test_format_success_adds_green_bold(self):
        """format_success should wrap text in green bold ANSI codes."""
        result = format_success("test")
        assert "\033[92m" in result
        assert "\033[1m" in result
        assert "test" in result


class TestRunAllModules:
    """Tests for the run_all_modules function."""

    def test_returns_list(self):
        """run_all_modules should return a list."""
        result = run_all_modules()
        assert isinstance(result, list)

    def test_handles_empty_package(self):
        """run_all_modules should handle package with no submodules."""
        result = run_all_modules()
        assert isinstance(result, list)

    def test_prints_start_and_complete_messages(self, capsys):
        """Runner should print start and complete messages."""
        run_all_modules()
        output = capsys.readouterr().out
        assert f"Starting {pkg_name}" in output
        assert f"Completed {pkg_name}" in output


class TestRunnerMain:
    """Tests for the main entry point."""

    def test_main_calls_run_all_modules(self):
        """main() should call run_all_modules()."""
        with patch("runner.run_all_modules") as mock_run:
            mock_run.return_value = []
            main()
            mock_run.assert_called_once()

    def test_main_has_no_parameters(self):
        """main() function should have zero parameters."""
        params = signature(main).parameters
        assert len(params) == 0


class TestEntryPointConstant:
    """Tests for the ENTRY_POINT constant."""

    def test_entry_point_is_main(self):
        """ENTRY_POINT should be 'main'."""
        assert ENTRY_POINT == "main"
