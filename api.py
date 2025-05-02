# File for LLM API interaction. 

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


### Checks if the API key is loaded correctly
if not anthropic_api_key:
    raise ValueError("anthropic API Key Not Found! Make sure to set it in the .env file.")


# Define an Enum for API choices
from enum import Enum
class APIChoice(Enum):
    CLAUDE = "Claude"
    CHATGPT = "ChatGPT"
    # Other API options should be added here.

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

def ClaudeAPI(input_list, assistant_settings=None):
    """
    This function is for calling the ClaudeAPI

    input:
        input_list: List of Json file objects, that is one or more user and assistant text messages
        assistant_settings: String, Extra parameters on how the API should either behave or respond. Default is None

    returns: an response from Claude, or None if error occurs
    """
    client = anthropic.Anthropic(api_key=anthropic_api_key)

    return error_handling_wrapper(
        client.messages.create,
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        temperature=0,
        system=f"{assistant_settings}",
        messages= input_list
    )

DEFAULT_SYSTEM_PROMPT = """You are a world-class software architect. I will give you some code files, where I will start by giving the relative path, and then the code. 
            Each file starts with '### START FILE: <filename> ###' and ends with '### END FILE: <filename> ###'. 
            You should now decide if these files and their placement in the folders have compliance of the code architecture "Onion", 
            in accordance to if it upholds these standards. You shall return a list of what is wrong according to the "Onion" 
            architecture with the code given to you, and return nothing else than the list, 
            where each point in the list corresponds to one single violation of the Onion architecture.
            This list should be as exhaustive as possible, but also as concise as possible. 
            Your analysis will be precise and actionable, highlighting only genuine architectural violations, 
            and naming the exact files involved, and the specific principle being violated. 
            If no violations are found, return "No violations found.", and how the code adheres to the onion architecture. """

def AnalyzeArchitectureAdherence(input_list, chosen_API=APIChoice.CLAUDE, system_prompt=DEFAULT_SYSTEM_PROMPT):
    """
    This function is for calling the API that will analyse the code from the prompt in the input_list.

    input:
        input_list: List of Json file objects, that is one or more user and assistant text messages
        chosen_API: ENum, which API should be used to create this. Default is Claude.
        system_prompt: How the API should behave, via a system prompt. Default is the string DEFAULT_SYSTEM_PROMPT

    returns: an assesment of if the codebase adheres to a specified architecture, in an API response(A list with a TextBlock inside it), or None if error occurs
    """
    if chosen_API == APIChoice.CLAUDE:
        return ClaudeAPI(input_list, system_prompt)
    elif chosen_API == APIChoice.CHATGPT:
        raise NotImplementedError("ChatGPT support is not implemented yet.")
    else:
        raise ValueError(f"Invalid API choice: {chosen_API}")
    