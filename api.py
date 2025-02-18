# LLM API interaction

## For error handling
import requests

## loading secrets
from dotenv import load_dotenv
import os

### Load environment variables from .env
load_dotenv()

### Access API key
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")


## Claude API
import anthropic


### checking if the API key is correctly loaded
if not anthropic_api_key:
    raise ValueError("anthropic API Key Not Found! Make sure to set it in the .env file.")


def error_handling_wrapper(api_function, *args, **kwargs):
    """
    Generic error handling wrapper for all kinds of API calls

    param api_function: The API function to execute
    param args: Positional arguments for the API function
    param kwargs: Keyword arguments for the API function
    
    return: API response or None if an error occurs
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

def ClaudeAPI(input_json, assistant_settings=None):
    """
    This function is for calling the ClaudeAPI

    input:
        input_json: Json file, that is one or more user and assistant text messagess
        assistant_settings: String, Extra parameters on how the API should either behave or respond. Default is None

    returns: an response from Claude, or None if error occurs
    """
    client = anthropic.Anthropic(api_key=anthropic_api_key)

    return error_handling_wrapper(
        client.messages.create,
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0,
        system=f"You are a world-class programmer. {assistant_settings}",
        messages=[
            input_json
        ]
    )


testResponse = ClaudeAPI({"role": "user", "content": "Make a *What's up world* print function" }, "Respond only with code")
if testResponse:
    print(testResponse.content)
else:
    print("Claude API call failed.")
