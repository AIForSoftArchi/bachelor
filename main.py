# Bachelor project, spring semester 2025
# Created by Mads Nørklit Jensen & Casper Storm Frøding
# Supervisor: Paolo Tell
# University: IT-University of Copenhagen

# Our entry point for the execution

import file_handler as fh
import parser
import api
import os

def main():
  print("Main started")
  
  # Dynamically determine the base directory of the script
  base_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the script's directory

  # Define a list of relative paths (this should probably be done dynamically based on the base_dir)
  relative_paths = [
      "architectureViolation\Domain\entities\Customer.cs",
      "architectureViolation\Application\Services\CustomerService.cs",
      "architectureViolation\Infrastructure\Data\CustomerRepository.cs"
  ]

  # Generate full file paths dynamically
  file_paths = [os.path.join(base_dir, rel_path) for rel_path in relative_paths]

  print("Processing files:")
  for path in file_paths:
      print(f" - {path}")

  # Call function with dynamically generated file paths
  tempList = fh.process_files(file_paths)

  promptString = parser.strutureJSONToString(tempList)

  finalPrompt = parser.StringToPrompt(promptString)

  answer = api.CreateComplianceReportArchitecture(finalPrompt)

  print(answer.content)
    

# This ensures that main() only runs when the script is executed directly
if __name__ == "__main__":
    main()