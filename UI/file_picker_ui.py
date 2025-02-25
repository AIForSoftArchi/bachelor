import customtkinter as ck
from tkinter import filedialog, messagebox

ck.set_default_color_theme("green")
ck.set_appearance_mode("light")

selected_files = []

def open_files():
    """Opens file dialog and updates UI with selected files."""
    global selected_files   
    file_paths = filedialog.askopenfilenames(title="Select Files for analysis")
    if file_paths:
        selected_files.extend(file_paths)  # Stores the selected files
        unique_files = set(selected_files)  # Remove duplicates
        selected_files = list(unique_files)  # Convert back to a list
        
        # Clear previous file labels
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        
        # Display selected files in scrollable frame
        for file in unique_files:
            file_label = ck.CTkLabel(scrollable_frame, text=file, anchor="w", justify="left")
            file_label.pack(fill="x", padx=10, pady=2)

def submit_files():
    """Returns selected files and closes UI."""
    if selected_files:
        print("Files Submitted:", selected_files)  # Process files as needed
        root.destroy()  # Close the application window
    return selected_files

def on_window_close():
    """Handles window closing event with a confirmation dialog."""
    confirm = messagebox.askyesno("Exit Confirmation", "Are you sure you want to close without submitting?")
    if confirm:
        print("Window closed without submitting files.")
        selected_files.clear()  # Clear the selected files
        root.destroy()  # Close the application window
    else:
        print("Close action canceled.")

def launch_file_picker():
    """
        Launches the file picker UI with a scrollable frame.
        
        return: List of paths to selected files    
    """
    global root, scrollable_frame

    # Create main window
    root = ck.CTk()  
    root.title("Multi-File Picker")
    root.geometry("500x400")
    
    root.protocol("WM_DELETE_WINDOW", on_window_close)  # Handle close event

    # Create button to open file dialog
    open_button = ck.CTkButton(root, text="Choose Files", command=open_files)
    open_button.pack(pady=10)

    # Create a scrollable frame inside the window
    scrollable_frame = ck.CTkScrollableFrame(root, width=480, height=200)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Create submit button
    submit_button = ck.CTkButton(root, text="Submit files for analysis", command=submit_files)
    submit_button.pack(pady=10)

    # Run application
    root.mainloop()

    return selected_files  # Return selected files after UI closes

# Only run UI if script is executed directly
if __name__ == "__main__":
    launch_file_picker()
