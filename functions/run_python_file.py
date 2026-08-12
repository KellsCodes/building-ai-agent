import os
import subprocess


def run_python_file(
    working_directory: str,
    file_path: str,
    args: list[str] | None = None
) -> str:
    """Run the file functions and return the output."""
    working_directory_path = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(
        os.path.join(working_directory_path, file_path))
    is_valid_target_file_path = os.path.commonpath(
        [working_directory_path, target_file_path]) == working_directory_path

    if not is_valid_target_file_path:
        return (f'Error: Cannot execute "{file_path}" as it is outside '
                'the permitted working directory')
    if not os.path.isfile(target_file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    try:
        command = ["python", target_file_path]
        if args:
            command.extend(args)

        working_dir = os.path.dirname(target_file_path)
        result = subprocess.run(
            command,
            cwd=working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )

        """Build the output string"""
        output = []

        """check if both output streams are completely empty"""
        if result.returncode != 0:
            output.append(
                f"Error: Process exited with code {result.returncode}")

        """Check if both output streams are completely empty"""
        if not result.stdout and not result.stderr:
            output.append("No output produced")
        else:
            """Append standard output if contents exists"""
            if result.stdout:
                output.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output)

    except Exception as e:
        return f'Error: executing Python file: {e}'
