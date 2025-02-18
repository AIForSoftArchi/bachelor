# LLM API interaction

## loading secrets
from dotenv import load_dotenv
import os

### Load environment variables from .env
load_dotenv()

### Access API key
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")


## Claude API
import anthropic # type: ignore


### checking if the API key is correctly loaded

if anthropic_api_key:
    print("API Key Loaded Successfully!")
else:
    raise ValueError("API Key Not Found! Make sure to set it in the .env file.")


def ClaudeAPI(input):
    client = anthropic.Anthropic(api_key=anthropic_api_key)

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0,
        system="You are a world-class programmer. Respond only with code.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": input
                    }
                ]
            }
        ]
    )
    print(message.content)


ClaudeAPI("Make a function that finds the square root of a given number, and has error handling.")
