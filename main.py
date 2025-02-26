# Bachelor project, spring semester 2025
# Created by Mads Nørklit Jensen & Casper Storm Frøding
# Supervisor: Paolo Tell
# University: IT-University of Copenhagen

# Our entry point for the execution

import file_handler as fh
import parser
import api
import os
from UI.file_picker_ui import launch_file_picker  # Import the function

def main():
  print("Main started")

  # Dynamically determine the base directory of the script
  base_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the script's directory
  
  selected_files = launch_file_picker()
  
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

  print(finalPrompt)

  answer = api.CreateComplianceReportArchitecture(finalPrompt)

  print(answer)

  answerText = parser.ListWithTextBlockToString(answer.content)

  reportList = parser.split_numbered_points(answerText)

  # Display the results
  for point in reportList:
    print(f"{point}\n")

## Can be deleted whenever
def TestingCodeGeneration():
    FingAround = [{'role': 'user', 'content': """I have 1 files I am giving you here. First I will give you the relative paths for the files, and then I will give the code in these files. \ntestFiles\\todolist.cs \n\n And following is the code from the files. Each file starts with \'### START FILE: <filename> ###\' and ends with \'### END FILE: <filename> ###\'. \n\n### START 
                   FILE: todolist.cs ###\nusing System;\nusing System.Collections.Generic;\nusing System.IO;\n\nclass ToDoListApp\n{\n    static string filePath = "tasks.txt";\n    static List<string> tasks = new List<string>();\n\n    static void Main()\n    {\n        LoadTasks();\n    
                       while (true)\n        {\n            Console.Clear();\n            Console.WriteLine("To-Do List Application");\n            Console.WriteLine("1. Add Task");\n            Console.WriteLine("2. Remove Task");\n            Console.WriteLine("3. View Tasks");\n       
                        Console.WriteLine("4. Exit");\n            Console.Write("Choose an option: ");\n\n  
                             string choice = Console.ReadLine();\n            switch (choice)\n            {\n                case "1": AddTask(); break;\n                case "2": RemoveTask(); break;\n                case "3": ViewTasks(); break;\n                case "4": SaveTasks(); 
                   return;\n                default: Console.WriteLine("Invalid option. Press Enter to try again."); Console.ReadLine(); break;\n            }\n        }\n    }\n\n    static void AddTask()\n    {\n        Console.Write("Enter new task: ");\n        string task = Console.ReadLine();\n        if (!string.IsNullOrWhiteSpace(task))\n        {\n            tasks.Add(task);\n            Console.WriteLine("Task added successfully!");\n        }\n        else\n        {\n            Console.WriteLine("Task cannot be empty!";\n        }\n       
                    Console.ReadLine();\n    }\n\n    static void RemoveTask()\n    {\n        ViewTasks();\n        Console.Write("Enter task number to remove: ");\n        if (int.TryParse(Console.ReadLine(), out int index) && index > 0 && index <= tasks.Count)\n        {\n            tasks.RemoveAt(index - 1);\n            Console.WriteLine("Task removed successfully!");\n 
       }\n        else\n        {\n            Console.WriteLine("Invalid task number!");\n        }\n        Console.ReadLine();\n    }\n\n    static void ViewTasks()\n    {\n    
    Console.WriteLine("\\nYour Tasks:");\n        if (tasks.Count == 0)\n        {\n      
      Console.WriteLine("No tasks available.");\n        }\n        else\n        {\n     
       for (int i = 0; i < tasks.Count; i++)\n            {\n                Console.WriteLine($"{i + 1}. {tasks[i]}");\n            }\n        }\n        Console.WriteLine("\\nPress Enter to continue...");\n        Console.ReadLine();\n    }\n\n    static void SaveTasks()\n    {\n        File.WriteAllLines(filePath, tasks);\n        Console.WriteLine("Tasks saved successfully!");\n    }\n\n    static void LoadTasks()\n    {\n        if (File.Exists(filePath))\n        {\n            tasks = new List<string>(File.ReadAllLines(filePath));\n        }\n    }\n}\n \n### END FILE: todolist.cs ###\n\n"""}, 
       {"role": "assistant", "content":"""1. The code violates the Onion Architecture by mixing UI concerns (Console operations), business logic, and data persistence (File I/O) in a single class (ToDoListApp), whereas these should be separated into distinct layers.\n\n2. Direct file system access (File.WriteAllLines and File.ReadAllLines) in the same class as business logic violates the dependency rule of Onion Architecture, as infrastructure concerns should be in the outer layer.\n\n3. The tasks List<string> represents domain data but is directly manipulated alongside UI and infrastructure code, violating domain isolation principles of Onion Architecture.\n\n4. The application lacks proper interfaces and dependency inversion, as required by Onion Architecture, with direct concrete implementations instead of abstractions.\n\n5. Business rules and use cases (task management) are not properly encapsulated in a separate application service layer, instead being mixed with UI code in the Main method."""},
       {"role": "user", "content":"""Please fix point 2"""}]
    FingAnswer = api.CreateCodeArchitectureFix(FingAround)

    answer_str = str(FingAnswer.content)

    print(answer_str)
    return answer_str

# This ensures that main() only runs when the script is executed directly
if __name__ == "__main__":
    main()
