import os
import sys
from dotenv import load_dotenv
from openai import OpenAI


class ConfigError(Exception):
    """Raised when environment setup or required variables are missing"""
    pass


class APIResponseError(Exception):
    """Raised when the API response is invalid or missing expected data"""
    pass


def load_env_variable() -> str:
    """Loads an environment variable or raises a RuntimeError if missing"""
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if api_key is None:
        raise ConfigError(
            "OPENROUTER_API_KEY environment variable is missing")
    return api_key


def main() -> None:
    api_key = load_env_variable()
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    prompt_content = (
        "Why is Boot.dev such a great place to learn backend "
        "development? Use one paragraph maximum."
    )

    response = client.chat.completions.create(
          model="openrouter/free",
          messages=[{"role": "user", "content": prompt_content}]
          )

    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    if response.usage.completion_tokens is None:
        raise APIResponseError("Response tokens are missing in the response.")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    try:
        main()
    except ConfigError as e:
        print(f"Environment Setup Failure: {e}", file=sys.stderr)
        sys.exit(1)
    except APIResponseError as e:
        print(f"API Response Failure: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
