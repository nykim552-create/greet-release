"""Print a greeting for a name given on the command line."""

import sys


def greet(name: str, punctuation: str = "!") -> str:
    """Return a greeting for name; a blank name becomes world."""
    if not name.strip():
        name = "world"
    return f"Hello, {name}{punctuation}"


def main() -> int:
    """Print a greeting for the first argument, or world."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


def test_greet_blank() -> None:
    assert greet(" ") == "Hello, world!"


def test_greet_punctuation() -> None:
    assert greet("Hee", ".") == "Hello, Hee."


if __name__ == "__main__":
    raise SystemExit(main())
