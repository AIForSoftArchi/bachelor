#Parsing of the response from the API.

def StringToPrompt(input):
    """
        Creates the prompt that the API should use.

        param input: String for the prompt

        return: List of a single JSON object that is the prompt.
    """
    return [{"role": "user", "content": input } ]

def strutureJSONToString(input):
    """ 
        This function prepares the code and code structure for the API.

        input: A list of JSON objects

        output: A string

    """
    # Sort by file_path to ensure deterministic order
    input = sorted(input, key=lambda x: x["file_path"])

    amountOfElements = len(input)
    finalstring = f"I have {amountOfElements} files I am giving you here. First I will give you the relative paths for the files, and then I will give the code in these files. \n"

    # Give the relative paths
    for file in input:
        finalstring = finalstring + f"{file['file_path']} \n"
    

    finalstring = finalstring + "\n And following is the code from the files. \n\n"


    # Give the code from each file.
    for file in input:
        finalstring = finalstring + f"### START FILE: {file['file_name']} ###\n{file['contents']} \n### END FILE: {file['file_name']} ###\n\n"


    return finalstring

def ListWithTextBlockToString(theList):
    """
    extracts the text from a List with a TextBlock object inside it.

    param theList: List with a TextBlock object inside it

    output: A string
    """
    return theList[0].text
