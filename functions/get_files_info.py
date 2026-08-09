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
            return (f'Error: Cannot list "{directory}" '
                    'as it is outside the permitted working directory')

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        else:
            return f'Success: "{directory}" is within the working directory'
    except NotADirectoryError:
        return f'Error: "{directory}" is not a directory'
    except PermissionError:
        return f'Error: Permission denied to access "{directory}"'
    except OSError as e:
        return f'Error: OS level failure: {e.strerror}'
