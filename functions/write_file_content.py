import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    """Writes content to a file within the working directory."""
    working_directory_path = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(
        os.path.join(working_directory_path, file_path)
    )
    is_valid_target_file_path = os.path.commonpath(
        [working_directory_path, target_file_path]
    ) == working_directory_path

    if not is_valid_target_file_path:
        return (f'Error: Cannot write to "{file_path}" as it is '
                'outside the permitted working directory')
    if os.path.isdir(target_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    try:
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        with open(target_file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return (f'Successfully wrote to "{file_path}" '
                f'({len(content)} characters written)')
    except PermissionError:
        return f"Error: writing to {file_path} failed. Permission denied."
    except UnicodeEncodeError:
        return f"Error: writing to {file_path} failed. Invalid characters."
    except OSError as e:
        return f"Error: System hardware/disk failure: {e.strerror}"


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a specified file within the working directory, creating directories as needed. Returns success or error messages based on the operation.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The textual content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
