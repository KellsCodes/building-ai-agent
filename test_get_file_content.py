import sys
from functions.get_file_content import get_file_content


def test_get_file_content() -> None:
    """Executes the test suites mapping over various file inputs."""

    """Test case 1: lorem.txt"""
    result_lorem = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result_lorem)}")
    print(f"lorem.txt truncated: {'truncated' in result_lorem}")
    # print()

    """Test case 2: main.py"""
    result_main = get_file_content("calculator", "main.py")
    print(result_main)
    # print()

    """Test case 3: pkg/calculator.py"""
    result_calc = get_file_content("calculator", "pkg/calculator.py")
    print(result_calc)
    # print()

    """Test case 4: /bin/cat"""
    result_cat = get_file_content("calculator", "/bin/cat")
    print(result_cat)
    # print()

    """Test case 5: pkg/does_not_exist.py"""
    result_missing = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result_missing)
    # print()


if __name__ == "__main__":
    try:
        test_get_file_content()
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
