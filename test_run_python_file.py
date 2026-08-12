from functions.run_python_file import run_python_file


def run_tests(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> None:
    """Run the file functions and print the output."""
    result = run_python_file(working_directory, file_path, args)
    print(result)


def test_run_python_file():
    run_tests("calculator", "main.py")
    run_tests("calculator", "main.py", ["3 + 5"])
    run_tests("calculator", "tests.py")
    run_tests("calculator", "../main.py")
    run_tests("calculator", "nonexistent.py")
    run_tests("calculator", "lorem.txt")


if __name__ == "__main__":
    test_run_python_file()
