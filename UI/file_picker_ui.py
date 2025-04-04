import customtkinter as ck
from tkinter import filedialog, messagebox
import os
from pathlib import Path

ck.set_default_color_theme("green")
ck.set_appearance_mode("light")

selected_folders = set()
selected_files = set()

def open_folder():
    """Opens folder dialog and updates UI with selected folder and it's files."""
    print("Entered open_folder")
    global selected_files, selected_folders  

    folder_path = filedialog.askdirectory(title="Select Folder for analysis")

    if folder_path and folder_path not in selected_folders:
        selected_folders.add(folder_path)  # Use a set to prevent duplicates

        for root_dir, _, files in os.walk(folder_path):
            for file in files:
                selected_files.add(os.path.join(root_dir, file))  # Store unique files

        # Clear previous UI elements
        for widget in scrollable_frame.winfo_children():
            widget.destroy() 
        
        # Display selected folders
        for folder in selected_folders:
            folder_label = ck.CTkLabel(scrollable_frame, text=f"Selected Folder: {folder}", anchor="w", justify="left")
            folder_label.pack(fill="x", padx=10, pady=5)

        # Display total file count
        file_count_label = ck.CTkLabel(scrollable_frame, text=f"Total Files: {len(selected_files)}", anchor="w", justify="left")
        file_count_label.pack(fill="x", padx=10, pady=5)

        # Display selected files
        for file in selected_files:
            file_label = ck.CTkLabel(scrollable_frame, text=file, anchor="w", justify="left")
            file_label.pack(fill="x", padx=10, pady=2)

def submit_files():
    """Returns selected files and closes UI."""
    print("Entered submit_files")
    if selected_files:
        root.destroy()  # Close the application window
    return list(selected_files)

def on_window_close():
    """Handles window closing event with a confirmation dialog."""
    print("Window close event triggered.")
    confirm = messagebox.askyesno("Exit Confirmation", "Are you sure you want to close without submitting?")
    if confirm:
        print("Window closed without submitting files.")
        selected_files.clear()  # Clear the selected files
        selected_folders.clear()  # Clear the selected folders
        root.destroy()  # Close the application window
    else:
        print("Close action canceled.")
        root.destroy()

def launch_file_picker():
    """
    Launches the file picker UI with a scrollable frame.
    
    return: List of paths to selected files    
    """
    print("Entered launch_file_picker")
    global scrollable_frame, root
    
    root = ck.CTk()
    root.title("Folder Picker")
    root.geometry("500x400")
    
    root.protocol("WM_DELETE_WINDOW", on_window_close)  # Handle close event

    # Create button to open file dialog
    open_button = ck.CTkButton(root, text="Choose Folder", command=open_folder)
    open_button.pack(pady=10)

    # Create a scrollable frame inside the window
    scrollable_frame = ck.CTkScrollableFrame(root, width=480, height=200)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Create submit button
    submit_button = ck.CTkButton(root, text="Submit files for analysis", command=submit_files)
    submit_button.pack(pady=10)

    # Run the application
    root.mainloop()

    #Return the selected files, with them being normalised first.
    return [str(Path(file).resolve()) for file in selected_files]

# Only run UI if script is executed directly
if __name__ == "__main__":
    launch_file_picker()
