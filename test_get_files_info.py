import sys
from functions.get_files_info import get_files_info


def run_tests(working_directory: str, directory: str) -> None:
    """Helper function to execute the path check and prints it's results."""
    result = get_files_info(working_directory, directory)
    print(f"Testing ({working_directory}, {directory}) --> {result}")


def test_get_files_info() -> None:
    """Executes the test suites mapping over various directory inputs."""
    run_tests("calculator", ".")
    run_tests("calculator", "/bin")
    run_tests("calculator", "../")
    run_tests("calculator", "main.py")
    # assert get_files_info("/home/user", "documents") == 'Success: "documents" is within the working directory'
    # assert get_files_info("/home/user", "../etc") == 'Error: Cannot list "../etc" as it is outside the permitted working directory'
    # assert get_files_info("/home/user", "non_existent_dir") == 'Error: "non_existent_dir" is not a directory'


if __name__ == "__main__":
    try:
        test_get_files_info()
    except Exception as e:
        print(f"Error: Test execution failed: {e}", file=sys.stderr)
        sys.exit(1)
