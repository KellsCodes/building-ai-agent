import os
from dotenv import load_dotenv


def load_env_variable() -> str:
    """Loads an environment variable or raises a RuntimeError if missing"""
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError(
            "OPENROUTER_API_KEY environment variable is missing")
    return api_key


def main() -> None:
    api_key = load_env_variable()
    print(f"Loaded API Key: {api_key}")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")