# File handling (read/write)

import json
import os

def process_files(file_paths, output_file="file_for_parser.json"):
  """
    Reads one or multiple files and returns a JSON object with relative paths and contents.

    param input: List containing file paths

    return: List of a single JSON object that is the prompt.
  """
  try:
    all_files_data = []  # Store data for multiple files

    # Get base directory (assumes all files are within a common root folder aka the project itself)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for file_name in file_paths:
        print(f"Processing file: {file_name}")

        # Check if file exists
        if not os.path.exists(file_name):
            print(f"Error: File not found -> {file_name}")
            continue  # Skip missing files instead of stopping

        # Compute relative path
        relative_path = os.path.relpath(file_name, base_dir)
        print(f"Relative path: {relative_path}")

        # Read file content line by line
        with open(file_name, "r", encoding="utf-8") as file:
            lines = [line.rstrip('\n') + "\n" for line in file]  # Preserve newlines

        # Format JSON for each file
        json_output = {
            "file_path": relative_path,  # Store relative path instead of absolute
            "file_name": os.path.basename(file_name),
            "contents": "".join(lines)  # Merge lines while keeping newlines
        }

        all_files_data.append(json_output)  # Add file data to list

    # Write the complete output once, not inside the loop (is only for testing purpose)
    with open(output_file, "w", encoding="utf-8") as jsonfile:
        json.dump(all_files_data, jsonfile, indent=4)

    print(f"All files processed successfully.")

    return all_files_data  # Return the full list of JSON objects

  except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return None  # Return None in case of an error
