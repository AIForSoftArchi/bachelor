import os
from pathlib import Path


def get_files_from_repo_root() :
   """
   This function gets all file paths, from the repo root, when run by a github actions command.

   return: List of paths, found from the repo root.
   """
   found_files = set()
   # Find the root of the repository.
   repo_root = os.environ.get("GITHUB_WORKSPACE", os.getcwd())
   print(f"The found Repo root is: {repo_root}")
   
   # walk through the subfolders and files, and add them accordingly
   # here root_dir is the folder that currently is being scanned.
   for root_dir, _, files in os.walk(repo_root):
            for file in files:
                found_files.add(os.path.join(root_dir, file))  # Store unique files

   #Return the found files, with them being normalised first.
   return [str(Path(file).resolve()) for file in found_files]