import os
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    working_directory_path = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(
        os.path.join(working_directory_path, file_path)
    )
    valid_target_file_path = os.path.commonpath(
        [working_directory_path, target_file_path]
    ) == working_directory_path

    if not valid_target_file_path:
        return (f'Error: Cannot read "{file_path}" as it is '
                'outside the permitted working directory')

    try:
        if not os.path.isfile(target_file_path):
            return ('Error: File not found or is not a '
                    f'regular file: "{file_path}"')
        # content = ""
        with open(target_file_path, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)
            """Check for more content and indicate if truncation occurred."""
            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at '
                    f'{MAX_CHARS} characters]')
        return content
    except UnicodeDecodeError:
        return f'Error: Cannot decode "{file_path}" as text'
    except OSError as e:
        return f'Error: OS level failure: {e.strerror}'


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads file contents in a specified directory relative "
        "to the working directory, returns the content with or without "
        "truncation based on character limit.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the "
                    "working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}
