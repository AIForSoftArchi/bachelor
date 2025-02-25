import customtkinter as ck
from tkinter import filedialog

ck.set_default_color_theme("green")
ck.set_appearance_mode("light")

selected_files = []

def open_files():
    """Opens file dialog and updates UI with selected files."""
    global selected_files   
    file_paths = filedialog.askopenfilenames(title="Select Files for analysis")
    if file_paths:
        selected_files.extend(file_paths) # Stores the selected files
        unique_files = set(selected_files)  # Remove duplicates
        selected_files = list(unique_files)  # Convert back to a list
        file_label.configure(text="Selected:\n" + "\n".join(unique_files))

def submit_files():
    """Returns selected files and closes UI."""
    if selected_files:
        print("Files Submitted:", selected_files)  # Process files as needed
        root.destroy()  # Close the application window
    return selected_files
        
def launch_file_picker():
    """
        Launches the file picker UI.
        
        return: List of paths to selected files    
    """
    global root, file_label

    # Create main window
    root = ck.CTk()
    root.title("Multi-File Picker")
    root.geometry("500x300")

    # Create button to open file dialog
    open_button = ck.CTkButton(root, text="Choose Files", command=open_files)
    open_button.pack(pady=20)

    # Label to show selected files
    file_label = ck.CTkLabel(root, text="No files selected", wraplength=480, justify="left")
    file_label.pack(pady=10)

    # Create submit button
    submit_button = ck.CTkButton(root, text="Submit files for analysis", command=submit_files)
    submit_button.pack(pady=20)

    # Run application
    root.mainloop()

    return selected_files  # Return selected files after UI closes

# Only run UI if script is executed directly (not when imported)
if __name__ == "__main__":
    launch_file_picker()