def garden_operations():
    """Demonstrate handling common Python errors in garden operations."""
    print("=== Garden Error Types Demo ===")
    try:
        x = int("abc")
    except ValueError:
        print("\nTesting ValueError...")
        print("Caught ValueError: invalid literal for int()")
    try:
        1 / 0
    except ZeroDivisionError:
        print("\nTesting ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero")

    try:
        open("missing.txt")
    except FileNotFoundError:
        print("\nTesting FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        x = {"plant": "rose"}
        x["missing_plant"]
    except KeyError:
        print("\nTesting KeyError...")
        print("Caught KeyError: 'missing\\_plant'")
    print("\nTesting multiple errors together...")
    try:
        int("abc")
        1 / 0
        open("missing.txt")
        d = {"plant": "rose"}
        d["missing_plant"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types():
    """Run garden_operations and confirm all errors are tested."""
    garden_operations()
    print("\nAll error types tested successfully!")


test_error_types()
