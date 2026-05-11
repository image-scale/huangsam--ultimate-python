"""Module runner that discovers and executes all modules with main() functions."""

from importlib import import_module
from inspect import isfunction, signature
from pkgutil import walk_packages

from pyguide import __name__ as pkg_name
from pyguide import __path__ as pkg_path


ANSI_GREEN = "\033[92m"
ANSI_BOLD = "\033[1m"
ANSI_RESET = "\033[0m"
ENTRY_POINT = "main"


def format_bold(text: str) -> str:
    """Return text with bold ANSI formatting."""
    return f"{ANSI_BOLD}{text}{ANSI_RESET}"


def format_success(text: str) -> str:
    """Return text with green bold ANSI formatting."""
    return f"{ANSI_GREEN}{format_bold(text)}{ANSI_RESET}"


def run_all_modules() -> list[str]:
    """Discover and run all modules with a main() function.

    Returns a list of module names that were successfully executed.
    """
    executed = []

    print(format_bold(f"Starting {pkg_name} runner"))

    for module_info in walk_packages(pkg_path, prefix=f"{pkg_name}."):
        try:
            mod = import_module(module_info.name)
        except (ImportError, SyntaxError) as err:
            print(f"-> Skipping {module_info.name}: {err}")
            continue

        if not hasattr(mod, ENTRY_POINT):
            continue

        entry_fn = getattr(mod, ENTRY_POINT)

        if not isfunction(entry_fn):
            continue

        params = signature(entry_fn).parameters
        if len(params) != 0:
            continue

        print(f"-> Running {mod.__name__}:{ENTRY_POINT}", end="")
        entry_fn()
        print(" [OK]")
        executed.append(mod.__name__)

    print(format_success(f"Completed {pkg_name} runner"))

    return executed


def main() -> None:
    """Entry point for running all study guide modules."""
    run_all_modules()


if __name__ == "__main__":
    main()
