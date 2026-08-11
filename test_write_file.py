import sys
from functions.write_file_content import write_file


def run_tests(working_directory: str, file_path: str, content: str) -> None:
    """Helper function to execute the file writing."""
    result = write_file(working_directory, file_path, content)
    print(result)
    print()


def test_write_file() -> None:
    """Test suites for write_file function."""
    run_tests("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    run_tests("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    run_tests("calculator", "/tmp/temp.txt", "this should not be allowed")


if __name__ == "__main__":
    try:
        test_write_file()
    except Exception as e:
        print(f"Error: Test execution failed: {e}", file=sys.stderr)
        sys.exit(1)
