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
  print("Main started")
  
  root = ck.CTk()
  # Dynamically determine the base directory of the script
  base_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the script's directory
  
  print("Opening file picker")
  selected_files = launch_file_picker(root)
  print("File picker closed")
  
  if not selected_files:
      print("No files selected. Exiting...")
      return
  
  relative_paths = []
  for path in selected_files:
      try: 
          relative_path = os.path.relpath(path, base_dir)
          relative_paths.append(relative_path)
      except ValueError:
          print(f"Warning: Could not convert {path} to a relative path.")
          relative_paths.append(path)  # Fallback to absolute if an error occurs
  
  print("Processing files:")
  for path in relative_paths:
      print(f" - {path}")
      
  # Generate full file paths dynamically
  file_paths = [os.path.join(base_dir, rel_path) for rel_path in relative_paths]

  # Call function with dynamically generated file paths
  tempList = fh.process_files(file_paths)

  promptString = parser.strutureJSONToString(tempList)

  finalPrompt = parser.StringToPrompt(promptString)

  answer = api.CreateComplianceReportArchitecture(finalPrompt)

  answerText = parser.ListWithTextBlockToString(answer.content)

  reportList = parser.split_numbered_points(answerText)
  
  run_failure_report(reportList)    

# This ensures that main() only runs when the script is executed directly
if __name__ == "__main__":
    main()