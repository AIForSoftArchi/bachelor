# LLM API interaction

## Claude API
import anthropic # type: ignore

def ClaudeAPI(input):
    client = anthropic.Anthropic()

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
