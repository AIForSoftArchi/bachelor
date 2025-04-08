import os
from pathlib import Path


def get_files_from_repo_root() :
   """
   This function gets all file paths, from the repo root, when run by a github actions command.

   return: List of paths, found from the repo root.
   """
   found_files = set()

   # Find the root of the repository.
   repo_root = Path(os.environ.get("GITHUB_WORKSPACE", os.getcwd())).resolve()
   print(f"The found Repo root is: {repo_root}")

   # List of folder names we want to include
   desired_folders = getArchAnalSpecification(repo_root)
   desired_folders = { (Path(folder)) for folder in desired_folders }
   
   # walk through the subfolders and files, and add them accordingly
   # here root_dir is the folder that currently is being scanned.
   # If no specifications of files are set, then the whole folder will be run through
   # (It has been assumed that if a specification of folder is set, then no files directly put in the repository root will be saved)
   if len(desired_folders) > 0 :
        for root_dir, dirs, files in os.walk(repo_root):
                    
                    root_path = Path(root_dir).resolve()
                    relative_path = root_path.relative_to(repo_root)

                    # Check if current folder is one of or inside any desired folder
                    collect_files = any(
                        relative_path == d or relative_path.is_relative_to(d)
                        for d in desired_folders
                    )

                    # Check if we should keep walking deeper
                    keep_walking = any(
                        d == relative_path or d.is_relative_to(relative_path) or relative_path.is_relative_to(d)
                        for d in desired_folders
                    )

                    if collect_files:
                        for file in files:
                            found_files.add(os.path.join(root_dir, file))  # Store unique files

                    #Stop the os.walk from going deeper and searching on.
                    #Unless we are in the root folder, then we want to keep searching. (i.e. the ' relative_path != "." ' check.)
                    if not keep_walking and relative_path != Path('.') :
                        dirs.clear()
                        continue
   else :
        for root_dir, _, files in os.walk(repo_root):
            for file in files:
                found_files.add(os.path.join(root_dir, file))  # Store unique files
             

   #Return the found files, with them being normalised first.
   return [str(Path(file).resolve()) for file in found_files]

def getArchAnalSpecification(repo_root):
    """
    Reads desired folder names from a file named 'ArchAnalSpec' located in the repo root.
    Each line in the file represents a relative folder path (e.g., 'Application/Models').

    Return: A set of Path objects representing the desired folders.
    """
    spec_file = Path(repo_root / "ArchAnalSpec.txt").resolve()
    if not spec_file.exists():
        print(f"No ArchAnalSpec file found at {spec_file}")
        return set()

    with spec_file.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    folders = {
        Path(line.strip()) for line in lines
        if line.strip() and not line.strip().startswith("#") # Ignore comments in the file
    }

    return folders