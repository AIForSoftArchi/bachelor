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


# Define an Enum for API choices
from enum import Enum
class APIChoice(Enum):
    CLAUDE = "Claude"
    CHATGPT = "ChatGPT"

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
        max_tokens=8192,
        temperature=0,
        system=f"You are a world-class programmer. {assistant_settings}",
        messages= input_list
    )

def CreateComplianceReportSyntax(input_list, chosen_API=APIChoice.CLAUDE):
    """
    This function is for checking the syntx of code

    input:
        input_list: List of Json file objects, that is one or more user and assistant text messages
        chosen_API: ENum, which API should be used to create this. Default is Claude.

    returns: A list with a TextBlock inside it, where the textblock is a list of what is synactically wrong with the code.
    """
    if chosen_API == APIChoice.CLAUDE:
        return ClaudeAPI(input_list, """You are also a master at analysing the compliance of code, 
                         in accordance to if it is syntactically correct.
                         You shall return a list of what is syntactically wrong with the code given to you, and return nothing else than the list, 
                         where each point in the list corresponds to one single syntactically incorrect mistake. 
                         Do not mix content between files, unless doing so for the purpose of upholding the principles of software architecture, 
                         and explicitly asked to do so.""")
    elif chosen_API == APIChoice.CHATGPT:
        raise NotImplementedError("ChatGPT support is not implemented yet.")
    
    else:
        raise ValueError(f"Invalid API choice: {chosen_API}")

def CreateComplianceReportArchitecture(input_list, chosen_API=APIChoice.CLAUDE):
    """
    This function is for creating the Compliance report

    input:
        input_list: List of Json file objects, that is one or more user and assistant text messages
        chosen_API: ENum, which API should be used to create this. Default is Claude.

    returns: an Compliance report from Claude(A list with a TextBlock inside it), or None if error occurs
    """
    if chosen_API == APIChoice.CLAUDE:
        return ClaudeAPI(
            input_list, 
            """I will give you some code files, where I will start by giving the relative path, and then the code. 
            Each file starts with '### START FILE: <filename> ###' and ends with '### END FILE: <filename> ###'. 
            You should now decide if these files and their placement in the folders have compliance of the code architecture "Onion", 
            in accordance to if it upholds these standards. You shall return a list of what is wrong according to the "Onion" 
            architecture with the code given to you, and return nothing else than the list, 
            where each point in the list corresponds to one single violation of the Onion architecture.
            This list should be as exhaustive as possible, but also as concise as possible. 
            You should be focusing on dependency flow, layer responsibilities, and domain isolation. 
            Your analysis will be precise and actionable, highlighting only genuine architectural violations, 
            and naming the exact files involved, and the specific principle being violated. 
            If no violations are found, return "No violations found.", and nothing else than this. """)
    elif chosen_API == APIChoice.CHATGPT:
        raise NotImplementedError("ChatGPT support is not implemented yet.")
    
    else:
        raise ValueError(f"Invalid API choice: {chosen_API}")
    

def CreateCodeArchitectureFix(input_list, chosen_API=APIChoice.CLAUDE):
    """
    This function is for correcting the violations, found from the complaince report.

    input:
        input_list: List of Json file objects, that is a previous conversation with an AI, that has user and assistant text messages.
        chosen_API: ENum, which API should be used to create this. Default is Claude.

    returns: The corrected code from Claude(A list with a TextBlock inside it), or None if error occurs
    """
    if chosen_API == APIChoice.CLAUDE:
        return ClaudeAPI(input_list, """I earlier gave you some code files, where I started by giving the relative path, and then the code. 
                         You then gave feedback on what architecture violations existed in accordance to the "Onion" Architecture.
                         You shall now return a corrected version of the code, where the points, that was asked to be fixed by the user, is given back to you. 
                         You shall NOT change anything in the code, that is not part of one of the points specified by the user.
                         You shall return all the code files given to you originally, also the ones that you have not made any architecturally changes to, but also the ones you have made architecturally changes to.
                         You shall also return the relative paths of all the files, both the ones you have changed the location of due to architectural changes, and the ones you haven't.
                         You shall start by giving the relative paths, and then the code.
                         You shall NOT return anything other than specified here, so no explaination of why this is done, or anything like this.
                         If no points are given by the user, return "No changes to the code" """)
    elif chosen_API == APIChoice.CHATGPT:
        raise NotImplementedError("ChatGPT support is not implemented yet.")
    
    else:
        raise ValueError(f"Invalid API choice: {chosen_API}")