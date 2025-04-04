# Bachelor project, spring semester 2025
# Created by Mads Nørklit Jensen & Casper Storm Frøding
# Supervisor: Paolo Tell
# University: IT-University of Copenhagen

# Our entry point for the execution
import customtkinter as ck
import file_handler as fh
import parser
import api
import os
from UI.file_picker_ui import launch_file_picker  # Import the function
from UI.report_ui import run_failure_report

def main():
  print("Main started\n")
  
  print("\nOpening file picker\n")
  selected_files = launch_file_picker()
  print("\n File picker closed \n")
  
  # Check if no files are selected, and terminate if true.
  if not selected_files:
      print("No files selected. Exiting...")
      return
  
  # Call function with the file paths, and get the files contents.
  tempList = fh.process_files(selected_files)

  # make the prompt into a string, and the format of a prompt.
  promptString = parser.strutureJSONToString(tempList)
  finalPrompt = parser.StringToPrompt(promptString)

  # Here is the call to the API, that returns an answer
  answer = api.CreateComplianceReportArchitecture(finalPrompt)

  # Extract the text from the response
  answerText = parser.ListWithTextBlockToString(answer.content)


  # Printing the answer into terminal
  print(answerText)

# This ensures that main() only runs when the script is executed directly
if __name__ == "__main__":
    main()
