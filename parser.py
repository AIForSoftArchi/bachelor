#Parsing of the response from the API.

## for Reg-ex parsing
import re

def StringToPrompt(input):
    """
        Creates the prompt that the API should use.

        param input: String for the prompt

        return: List of a single JSON object that is the prompt.
    """
    return [{"role": "user", "content": input } ]

def StringToJSONList(inputString, seperator = None):
    tempList = inputString.splitlines()
    


def strutureJSONToString(input):
    """ 
        This function prepares the code and code structure for the API.

        input: A list of JSON objects

        output: A string

    """
    amountOfElements = len(input)
    finalstring = f"I have {amountOfElements} files I am giving you here. First I will give you the relative paths for the files, and then I will give the code in these files. \n"

    # Give the relative paths
    for file in input:
        finalstring = finalstring + f"{file['file_path']} \n"
    

    finalstring = finalstring + "\n And following is the code from the files. Each file starts with '### START FILE: <filename> ###' and ends with '### END FILE: <filename> ###'. \n\n"


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


def split_numbered_points(text):
    """
    Splits a string into a list based on numbers followed by a dot.

    Args:
        text (string): The input string to split.

    Returns:
        list: A list of points extracted from the string.
    """

    pattern = r"(?<!\d)(\d+\.\s.*?)(?=\n\d+\.\s|\Z)"

    # Find all numbered points in the text
    points = re.findall(pattern, text, re.DOTALL)

    return [point.strip() for point in points]
