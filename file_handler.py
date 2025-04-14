# File handling (reading of the paths given)

import json
import os

# Define file extensions that are relevant for processing
RELEVANT_EXTENSIONS = {".py", ".cs", ".java", ".js", ".ts", ".cpp", ".c", ".h", ".hpp", ".go", ".rs", ".swift", ".kt", ".cshtml"}

def process_files(file_paths):
  """
    Reads one or multiple files and returns a JSON object with relative paths and contents.

    param input: List containing file paths

    return: List of single JSON object that is a files: path, name, and contents.
  """
  try:
    all_files_data = []  # Store data for multiple files

    # Get base directory (assumes all files are within a common root folder aka the project itself)
    base_dir = os.path.commonpath(file_paths)

    for file_name in file_paths:
        # Extract file extension and check if it's relevant
        _, file_extension = os.path.splitext(file_name)
        
        if file_extension.lower() not in RELEVANT_EXTENSIONS:
          print(f"Skipping irrelevant file: {file_name} \n")
          continue  # Skip the file
      
        print(f"Processing file: {file_name} \n\n\n")

        # Check if file exists
        if not os.path.exists(file_name):
            print(f"Error: File not found -> {file_name}")
            continue  # Skip missing files instead of stopping

        # Compute relative path
        relative_path = os.path.relpath(file_name, base_dir)

        # Read file content line by line
        with open(file_name, "r", encoding="utf-8", errors="replace") as file:
            lines = [line.rstrip('\n') + "\n" for line in file]  # Strip all newlines if there are multible, and add only one to the end of line.

        # Format JSON for each file
        json_output = {
            "file_path": relative_path,  # Store relative path instead of absolute
            "file_name": os.path.basename(file_name),
            "contents": "".join(lines)  # Merge lines while keeping newlines
        }

        all_files_data.append(json_output)  # Add file data to list

    print(f"All files processed successfully. Processing a total of {len(all_files_data)} files.")

    return all_files_data  # Return the full list of JSON objects

  except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return None  # Return None in case of an error
