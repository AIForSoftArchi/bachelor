# Bachelor project, spring semester 2025
# Created by Mads Nørklit Jensen & Casper Storm Frøding
# Supervisor: Paolo Tell
# University: IT-University of Copenhagen

# Our entry point for the execution
import customtkinter as ck
import file_handler as fh
import file_path_getter as fpg
import parser
import api
import os
import sys
from UI.file_picker_ui import launch_file_picker  # Import the function
from UI.report_ui import run_failure_report

is_pipeline_run = bool

def main():
  print("Main started\n")

  # Check if run locally or pipeline
  is_pipeline_run = os.environ.get("GITHUB_ACTIONS") == "true"

  # get files either from choice(if not github actions), or from working directory (if run by github actions)
  if is_pipeline_run:
     # Getting the working directory, and getting the files from this directory.
     selected_files = fpg.get_files_from_repo_root()
  else:
     print("\nOpening file picker\n")
     selected_files = launch_file_picker()
     print("\n File picker closed \n")
     
  # Check if no files are selected, and terminate if true.
  if not selected_files:
    print("No files selected. Exiting...")
    if is_pipeline_run:
       sys.exit(1)
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


  # Printing the answer into terminal, and setting status
  report_status(answerText)

def report_status(response):
    if response == "No violations found." :
        print("✅ No violations found.")
        if is_pipeline_run :
          sys.exit(0)
    else:
        print(f"❌ Found these violations in the project:\n")
        print(response)
        if is_pipeline_run :
          sys.exit(1)

# This ensures that main() only runs when the script is executed directly
if __name__ == "__main__":
    main()
