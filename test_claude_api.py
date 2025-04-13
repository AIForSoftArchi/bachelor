# Supporting file for testing of the errors from the API.

# Import necessary modules
import anthropic
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")


def error_handling_wrapper(api_function, *args, **kwargs):
    """
    Generic error handling wrapper for all kinds of API calls
    """
    try:
        response = api_function(*args, **kwargs)
        return response

    except anthropic.APIConnectionError:
        print("Error: Failed to connect to Anthropic API. Check your internet connection.")

    except anthropic.APIStatusError as e:
        print(f"Anthropic API responded with an error: {e}")

    except anthropic.APIError as e:
        print(f"Anthropic API responded with an error: {e}")

    except requests.exceptions.ConnectionError:
        print("Error: Network connection issue. Check your internet connection.")

    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error : {e.response.status_code} - {e.response.text}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None  # Return None if an error occurs


def trigger_errors(test_mode):
    """
    Modify API call parameters to intentionally trigger errors
    """
    if test_mode == "no_api_key":
        return "", "claude-3-5-sonnet-20241022", 1000  # No API key
    elif test_mode == "invalid_api_key":
        return "invalid-key", "claude-3-5-sonnet-20241022", 1000
    elif test_mode == "invalid_model":
        return anthropic_api_key, "invalid-model", 1000  # Invalid model
    elif test_mode == "timeout":
        return anthropic_api_key, "claude-3-5-sonnet-20241022", 1000, 0.001  # Force timeout
    elif test_mode == "bad_request":
        return anthropic_api_key, "claude-3-5-sonnet-20241022", -10  # Invalid max_tokens
    else:
        return anthropic_api_key, "claude-3-5-sonnet-20241022", 1000  # Default (No error)


def ClaudeAPI(input_text, test_mode=None):
    """
    Calls the Claude API and allows error testing.
    """
    # Get test parameters
    api_key, model, max_tokens, *timeout = trigger_errors(test_mode)

    client = anthropic.Anthropic(api_key=api_key, timeout=timeout[0] if timeout else None)

    return error_handling_wrapper(
        client.messages.create,
        model=model,
        max_tokens=max_tokens,
        temperature=0,
        system="You are a world-class programmer. Respond only with code.",
        messages=[{
            "role": "user",
            "content": [{"type": "text", "text": input_text}]
        }]
    )


### **Testing Different Error Cases** ###
if __name__ == "__main__":
    # List of test modes to check error handling
    test_modes = [
        None,  # Normal API call (should succeed)
        "no_api_key",  # No API key
        "invalid_api_key",  # Invalid API key
        "invalid_model",  # Invalid model
        "timeout",  # Request timeout
        "bad_request",  # Invalid max_tokens
    ]

    for mode in test_modes:
        print(f"\n--- Testing Mode: {mode if mode else 'Normal API Call'} ---")
        response = ClaudeAPI("Write a Python function to calculate factorial.", test_mode=mode)
        if response:
            print("✅ API Response:", response.content)
        else:
            print("❌ API call failed.")
