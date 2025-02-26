import customtkinter as ck

ck.set_default_color_theme("green")
ck.set_appearance_mode("light")

class ScrollableFrame(ck.CTkScrollableFrame):
    def __init__(self, master, title, failures):
        super().__init__(master, label_text=title)
        
        self.grid_columnconfigure(0, weight=1)
        self.failures = failures
        self.checkboxes = []
        
        for i, failure in enumerate(self.failures):
            checkbox = ck.CTkCheckBox(self, text=failure)  # Removed wraplength
            checkbox.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            self.checkboxes.append(checkbox)
    
    def get_selected_failures(self):
        """Returns a list of selected failure descriptions."""
        return [cb.cget("text") for cb in self.checkboxes if cb.get() == 1]

class App(ck.CTk):
    def __init__(self, failure_list, root=None):
        super().__init__()
        
        self.title("Compliance Report for Software Architecture")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1, pad=20)
        self.grid_rowconfigure(0, weight=1, pad=20)

        # Pass correct parameter name
        self.scrollable_checkbox_frame = ScrollableFrame(self, title="Detected Compliance Failures", failures=failure_list)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # Placeholder button for future report generation
        self.button = ck.CTkButton(self, text="Generate Report", command=self.generate_report)
        self.button.grid(row=3, column=0, padx=20, pady=20)
    
    def generate_report(self):
        """Placeholder function for generating the report."""
        print("Report generation functionality will be implemented later.")
        
def run_failure_report(failure_list):
    """Function to start the application from another script."""
    
    
    print("Before app with failure list")
    app = App(failure_list)
    print("After app with failure list")
    app.mainloop() 
    print("After mainloop")

# Only run UI if script is executed directly
if __name__ == "__main__":
    run_failure_report()

