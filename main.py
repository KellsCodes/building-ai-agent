import os
import sys
import argparse
import json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions


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
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument(
        "user_prompt", type=str, help="The prompt to send to the chatbot"
    )
    # Pass optional verbose parameter
    parser.add_argument(
        "--verbose", action="store_true", help="Enable verbose output"
    )
    args = parser.parse_args()
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions,
    )

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        if response.usage.completion_tokens is None:
            raise APIResponseError(
                "Response tokens are missing in the response."
            )
        print(f"Response tokens: {response.usage.completion_tokens}")
    print("Response:")
    print(response.choices[0].message.content)
    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(
                f"Calling function: {tool_call.function.name}({function_args})"
            )


if __name__ == "__main__":
    try:
        main()
    except ConfigError as e:
        print(f"Error: Environment Setup Failure: {e}", file=sys.stderr)
        sys.exit(1)
    except APIResponseError as e:
        print(f"Error: API Response Failure: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
