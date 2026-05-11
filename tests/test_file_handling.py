"""Tests for file handling module."""

from pathlib import Path

from pyguide.advanced.file_handling import (
    main as file_main,
    write_file,
    read_file,
    append_file,
    read_lines,
    write_lines,
    write_binary,
    read_binary,
    PathLibDemo,
    create_temp_directory,
    cleanup_path,
)


class TestFileHandlingModule:
    """Tests for the file handling demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        file_main()

    def test_write_and_read_file(self):
        """write_file and read_file should work together."""
        temp_dir = create_temp_directory()
        try:
            filepath = str(temp_dir / "test.txt")
            write_file(filepath, "test content")
            assert read_file(filepath) == "test content"
        finally:
            cleanup_path(temp_dir)

    def test_append_file(self):
        """append_file should add content to existing file."""
        temp_dir = create_temp_directory()
        try:
            filepath = str(temp_dir / "append.txt")
            write_file(filepath, "first")
            append_file(filepath, " second")
            assert read_file(filepath) == "first second"
        finally:
            cleanup_path(temp_dir)

    def test_read_lines(self):
        """read_lines should return list of lines."""
        temp_dir = create_temp_directory()
        try:
            filepath = str(temp_dir / "lines.txt")
            write_file(filepath, "line1\nline2\nline3")
            lines = read_lines(filepath)
            assert lines == ["line1", "line2", "line3"]
        finally:
            cleanup_path(temp_dir)

    def test_write_lines(self):
        """write_lines should write list of lines."""
        temp_dir = create_temp_directory()
        try:
            filepath = str(temp_dir / "wlines.txt")
            write_lines(filepath, ["a", "b", "c"])
            lines = read_lines(filepath)
            assert lines == ["a", "b", "c"]
        finally:
            cleanup_path(temp_dir)

    def test_binary_operations(self):
        """Binary read/write should preserve bytes."""
        temp_dir = create_temp_directory()
        try:
            filepath = str(temp_dir / "binary.bin")
            data = bytes([0, 1, 255, 128])
            write_binary(filepath, data)
            assert read_binary(filepath) == data
        finally:
            cleanup_path(temp_dir)

    def test_pathlib_text(self):
        """PathLibDemo should handle text files."""
        temp_dir = create_temp_directory()
        try:
            path = temp_dir / "pathlib.txt"
            PathLibDemo.write_text(path, "pathlib text")
            assert PathLibDemo.read_text(path) == "pathlib text"
        finally:
            cleanup_path(temp_dir)

    def test_pathlib_bytes(self):
        """PathLibDemo should handle binary files."""
        temp_dir = create_temp_directory()
        try:
            path = temp_dir / "pathlib.bin"
            data = b"\x00\x01\x02"
            PathLibDemo.write_bytes(path, data)
            assert PathLibDemo.read_bytes(path) == data
        finally:
            cleanup_path(temp_dir)

    def test_path_info(self):
        """get_path_info should return correct info."""
        temp_dir = create_temp_directory()
        try:
            path = temp_dir / "info.txt"
            path.write_text("content")
            info = PathLibDemo.get_path_info(path)
            assert info["name"] == "info.txt"
            assert info["stem"] == "info"
            assert info["suffix"] == ".txt"
            assert info["exists"] is True
            assert info["is_file"] is True
            assert info["is_dir"] is False
        finally:
            cleanup_path(temp_dir)

    def test_path_info_nonexistent(self):
        """get_path_info should handle nonexistent paths."""
        path = Path("/nonexistent/path.txt")
        info = PathLibDemo.get_path_info(path)
        assert info["exists"] is False
        assert info["is_file"] is False
        assert info["is_dir"] is False

    def test_create_temp_directory(self):
        """create_temp_directory should create a directory."""
        temp_dir = create_temp_directory()
        try:
            assert temp_dir.exists()
            assert temp_dir.is_dir()
        finally:
            cleanup_path(temp_dir)

    def test_cleanup_path_file(self):
        """cleanup_path should remove files."""
        temp_dir = create_temp_directory()
        filepath = temp_dir / "to_delete.txt"
        filepath.write_text("delete me")
        assert filepath.exists()
        cleanup_path(filepath)
        assert not filepath.exists()
        cleanup_path(temp_dir)

    def test_cleanup_path_directory(self):
        """cleanup_path should remove directories recursively."""
        temp_dir = create_temp_directory()
        sub = temp_dir / "sub"
        sub.mkdir()
        (sub / "file.txt").write_text("nested")
        cleanup_path(temp_dir)
        assert not temp_dir.exists()

    def test_path_manipulation(self):
        """Path parts should be accessible."""
        path = Path("/home/user/file.txt")
        assert path.name == "file.txt"
        assert path.stem == "file"
        assert path.suffix == ".txt"
        assert path.parent == Path("/home/user")

    def test_path_joining(self):
        """Paths should be joinable with /."""
        base = Path("/home")
        full = base / "user" / "file.txt"
        assert str(full) == "/home/user/file.txt"
