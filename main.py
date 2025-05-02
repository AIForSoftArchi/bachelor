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

is_pipeline_run = False # False as standard.

def main():
  print("Main started\n")

  # Check if run locally or pipeline
  global is_pipeline_run
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
    if is_pipeline_run:
       print(f"::error:: No files selected!\n")
       sys.exit(1)
    print("No files selected. Exiting...")
    return
  
  # Call function with the file paths, and get the files contents.
  tempList = fh.process_files(selected_files)

  if tempList == None:
    if is_pipeline_run:
      print(f"::error:: An error occured during file reading!\n")
      sys.exit(1)
    print("An error occured during file reading!")
    return

  # make the prompt into a string, and the format of a prompt.
  promptString = parser.strutureJSONToString(tempList)
  finalPrompt = parser.StringToPrompt(promptString)

  # Here is the call to the API, that returns an answer
  answer = api.AnalyzeArchitectureAdherence(finalPrompt)

  # Check if the response from the API, is empty, due to an error.
  if answer == None :
    if is_pipeline_run:
       print(f"::error:: An error occured, that made the API return None.!\n")
       sys.exit(1)
    print("An error occured, that made the API return None.")
    return

  # Extract the text from the response
  answerText = parser.ListWithTextBlockToString(answer.content)


  # Printing the answer into terminal, and setting status
  report_status(answerText)

def report_status(response):
    """ This function checks the type of response recieved, and prints accordingly """
    if "No violations found" in response :
        if is_pipeline_run :
          print("::notice:: ✅ No violations found.")
          write_summary("✅ No violations found. \n" + response)
          sys.exit(0)
        print("✅ No violations found. \n")
        print(response)
    else:
        if is_pipeline_run :
          print("❌ Found architectural violations in the project!\n")
          write_summary("❌ Found these violations in the project:\n" + response)
          sys.exit(1)
        print("❌ Found architectural violations in the project!\n")
        print(response)

def write_summary(summary_text: str):
    """ Creates the Github Summary, for the pipeline. """
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path and summary_text:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write("```\n")
            f.write(summary_text)
            f.write("\n```\n")



# This ensures that main() only runs when the script is executed directly
if __name__ == "__main__":
    main()
