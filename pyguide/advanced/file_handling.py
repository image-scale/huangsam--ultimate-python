"""
File handling in Python provides multiple ways to read, write, and
manipulate files. This module demonstrates:

1. Traditional file operations with open()
2. Modern pathlib operations
3. Binary file handling
4. Context managers for safe file handling
5. File system operations (paths, directories)
6. Reading files line by line
"""

import tempfile
from pathlib import Path


def write_file(filepath: str, content: str) -> None:
    """Write content to a file (overwrites existing)."""
    with open(filepath, "w") as f:
        f.write(content)


def read_file(filepath: str) -> str:
    """Read entire content from a file."""
    with open(filepath, "r") as f:
        return f.read()


def append_file(filepath: str, content: str) -> None:
    """Append content to a file."""
    with open(filepath, "a") as f:
        f.write(content)


def read_lines(filepath: str) -> list[str]:
    """Read file line by line, stripping newlines."""
    with open(filepath, "r") as f:
        return [line.rstrip("\n") for line in f]


def write_lines(filepath: str, lines: list[str]) -> None:
    """Write lines to a file with newlines."""
    with open(filepath, "w") as f:
        for line in lines:
            f.write(line + "\n")


def write_binary(filepath: str, data: bytes) -> None:
    """Write binary data to a file."""
    with open(filepath, "wb") as f:
        f.write(data)


def read_binary(filepath: str) -> bytes:
    """Read binary data from a file."""
    with open(filepath, "rb") as f:
        return f.read()


class PathLibDemo:
    """Demonstrates pathlib operations."""

    @staticmethod
    def write_text(path: Path, content: str) -> None:
        """Write text using pathlib."""
        path.write_text(content)

    @staticmethod
    def read_text(path: Path) -> str:
        """Read text using pathlib."""
        return path.read_text()

    @staticmethod
    def write_bytes(path: Path, data: bytes) -> None:
        """Write bytes using pathlib."""
        path.write_bytes(data)

    @staticmethod
    def read_bytes(path: Path) -> bytes:
        """Read bytes using pathlib."""
        return path.read_bytes()

    @staticmethod
    def get_path_info(path: Path) -> dict:
        """Get information about a path."""
        return {
            "name": path.name,
            "stem": path.stem,
            "suffix": path.suffix,
            "parent": str(path.parent),
            "exists": path.exists(),
            "is_file": path.is_file() if path.exists() else False,
            "is_dir": path.is_dir() if path.exists() else False,
        }


def create_temp_directory() -> Path:
    """Create a temporary directory for testing."""
    return Path(tempfile.mkdtemp())


def cleanup_path(path: Path) -> None:
    """Remove a file or directory."""
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        for child in path.iterdir():
            cleanup_path(child)
        path.rmdir()


def main():
    # Create temp directory for file operations
    temp_dir = create_temp_directory()

    try:
        # Traditional file writing and reading
        text_file = str(temp_dir / "sample.txt")
        write_file(text_file, "Hello, World!")
        content = read_file(text_file)
        assert content == "Hello, World!"

        # Appending to files
        append_file(text_file, "\nSecond line")
        content = read_file(text_file)
        assert content == "Hello, World!\nSecond line"

        # Reading lines
        lines = read_lines(text_file)
        assert lines == ["Hello, World!", "Second line"]

        # Writing multiple lines
        lines_file = str(temp_dir / "lines.txt")
        write_lines(lines_file, ["Line 1", "Line 2", "Line 3"])
        read_back = read_lines(lines_file)
        assert read_back == ["Line 1", "Line 2", "Line 3"]

        # Binary file operations
        binary_file = str(temp_dir / "data.bin")
        binary_data = bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F])
        write_binary(binary_file, binary_data)
        read_data = read_binary(binary_file)
        assert read_data == binary_data
        assert read_data.decode("utf-8") == "Hello"

        # Pathlib text operations
        pathlib_file = temp_dir / "pathlib.txt"
        PathLibDemo.write_text(pathlib_file, "Pathlib content")
        assert PathLibDemo.read_text(pathlib_file) == "Pathlib content"

        # Pathlib binary operations
        pathlib_bin = temp_dir / "pathlib.bin"
        PathLibDemo.write_bytes(pathlib_bin, b"\x00\x01\x02\x03")
        assert PathLibDemo.read_bytes(pathlib_bin) == b"\x00\x01\x02\x03"

        # Path information
        info = PathLibDemo.get_path_info(pathlib_file)
        assert info["name"] == "pathlib.txt"
        assert info["stem"] == "pathlib"
        assert info["suffix"] == ".txt"
        assert info["exists"] is True
        assert info["is_file"] is True
        assert info["is_dir"] is False

        # Directory operations with pathlib
        sub_dir = temp_dir / "subdir"
        sub_dir.mkdir()
        assert sub_dir.exists()
        assert sub_dir.is_dir()

        # File in subdirectory
        sub_file = sub_dir / "nested.txt"
        sub_file.write_text("Nested content")
        assert sub_file.read_text() == "Nested content"

        # List directory contents
        files_in_temp = list(temp_dir.iterdir())
        assert len(files_in_temp) >= 5

        # Path manipulation
        path = Path("/home/user/documents/file.txt")
        assert path.name == "file.txt"
        assert path.stem == "file"
        assert path.suffix == ".txt"
        assert path.parent == Path("/home/user/documents")
        assert path.parts == ("/", "home", "user", "documents", "file.txt")

        # Joining paths
        base = Path("/home/user")
        full = base / "documents" / "file.txt"
        assert str(full) == "/home/user/documents/file.txt"

        # Relative path parts
        relative = Path("foo/../bar/file.txt")
        assert relative.parts == ("foo", "..", "bar", "file.txt")

        # File modes with open
        mode_file = str(temp_dir / "mode.txt")
        with open(mode_file, "w", encoding="utf-8") as f:
            f.write("UTF-8 content")
        with open(mode_file, "r", encoding="utf-8") as f:
            assert f.read() == "UTF-8 content"

        # Seek and tell
        with open(mode_file, "r") as f:
            assert f.tell() == 0
            f.seek(5)
            assert f.tell() == 5
            assert f.read(3) == " co"

    finally:
        # Clean up
        cleanup_path(temp_dir)
        assert not temp_dir.exists()


if __name__ == "__main__":
    main()
