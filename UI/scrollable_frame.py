import customtkinter as ctk

class ScrollableWindow(ctk.CTk):
    def __init__(self, title="Scrollable Window", width=500, height=400):
        super().__init__()

        self.title(title)
        self.geometry(f"{width}x{height}")

        # Create a canvas and a scrollbar
        self.canvas = ctk.CTkCanvas(self, bg="gray17", highlightthickness=0)
        self.scrollbar = ctk.CTkScrollbar(self, orientation="vertical", command=self.canvas.yview)

        # Create a frame inside the canvas
        self.scrollable_frame = ctk.CTkFrame(self.canvas)
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)

        # Window layout
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack elements
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Bind scrolling events
        self.bind_mouse_scroll()

        # Check if scrolling is necessary
        self.update_scrollbar_visibility()

    def on_frame_configure(self, event=None):
        """Adjust canvas scroll region when frame size changes."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.update_scrollbar_visibility()

    def update_scrollbar_visibility(self):
        """Show scrollbar only when necessary."""
        canvas_height = self.canvas.winfo_height()
        frame_height = self.scrollable_frame.winfo_reqheight()

        if frame_height > canvas_height:
            self.scrollbar.pack(side="right", fill="y")  # Show scrollbar
        else:
            self.scrollbar.pack_forget()  # Hide scrollbar

    def bind_mouse_scroll(self):
        """Enable scrolling with mouse wheel and touchpad (cross-platform)."""
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_scroll)  # Windows & macOS
        self.canvas.bind_all("<Button-4>", self.on_mouse_scroll)  # Linux (Scroll Up)
        self.canvas.bind_all("<Button-5>", self.on_mouse_scroll)  # Linux (Scroll Down)

    def on_mouse_scroll(self, event):
        """Handle mouse wheel & touchpad scrolling."""
        if event.num == 4:  # Linux scroll up
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:  # Linux scroll down
            self.canvas.yview_scroll(1, "units")
        else:  # Windows/macOS scroll
            direction = -1 if event.delta > 0 else 1  # Invert for macOS
            self.canvas.yview_scroll(direction, "units")

    def add_content(self, widget):
        """Allows external scripts to add widgets to the scrollable frame."""
        widget.pack(pady=5, padx=10)
        self.scrollable_frame.update_idletasks()
        self.update_scrollbar_visibility()

# Only runs if executed directly (for testing)
if __name__ == "__main__":
    app = ScrollableWindow(title="Test Window")

    # Example: Adding labels dynamically (for testing)
    for i in range(50):
        label = ctk.CTkLabel(app.scrollable_frame, text=f"Label {i+1}", padx=10, pady=5)
        app.add_content(label)

    app.mainloop()
