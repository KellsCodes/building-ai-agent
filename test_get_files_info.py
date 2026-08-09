import sys
import os
from functions.get_files_info import get_files_info


def run_tests(working_directory: str, directory: str) -> None:
    """Helper function to execute the path check and prints it's results."""
    working_directory_path = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(
        working_directory_path, directory))
    result = get_files_info(working_directory, directory)
    is_current_path = (
        os.path.commonpath([working_directory_path, target_dir])
        == working_directory_path
    )

    if is_current_path:
        print("Result for current directory:")
        print(result, "\n")
    else:
        print(f"Result for '{directory}' directory:")
        print(result, "\n")


def test_get_files_info() -> None:
    """Executes the test suites mapping over various directory inputs."""
    run_tests("calculator", ".")
    run_tests("calculator", "pkg")
    run_tests("calculator", "/bin")
    run_tests("calculator", "../")
    run_tests("calculator", "main.py")


if __name__ == "__main__":
    try:
        test_get_files_info()
    except Exception as e:
        print(f"Error: Test execution failed: {e}", file=sys.stderr)
        sys.exit(1)
