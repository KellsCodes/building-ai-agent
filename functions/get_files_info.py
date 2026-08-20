import os


def get_files_info(working_directory: str, directory: str) -> str:
    try:
        working_directory_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(
            os.path.join(working_directory_path, directory)
        )
        valid_target_dir = (
            os.path.commonpath([working_directory_path, target_dir]
                               ) == working_directory_path
        )

        if not valid_target_dir:
            return (f'   Error: Cannot list "{directory}" '
                    'as it is outside the permitted working directory')

        if not os.path.isdir(target_dir):
            return f'   Error: "{directory}" is not a directory'
        else:
            items_summary = []
            for item in os.listdir(target_dir):
                full_path = os.path.join(target_dir, item)
                is_dir = os.path.isdir(full_path)
                try:
                    size = os.path.getsize(full_path)
                except OSError:
                    size = 0
                items_summary.append(
                    f" - {item}: file_size={size} bytes, is_dir={is_dir}")
            return "\n".join(items_summary)

    except NotADirectoryError:
        return f'   Error: "{directory}" is not a directory'
    except PermissionError:
        return f'   Error: Permission denied to access "{directory}"'
    except OSError as e:
        return f'   Error: OS level failure: {e.strerror}'


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
