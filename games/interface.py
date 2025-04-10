"""
GUI applications using Tkinter.
Contains basic examples and a more advanced GUI application.
"""

import tkinter as tk
from tkinter import messagebox


class BasicGUI:
    """Basic GUI demonstration using Tkinter."""
    
    def __init__(self):
        """Initialize a new basic GUI window."""
        # Create the main window
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Basic GUI Demo")
        
        # Create a label widget
        self.label = tk.Label(self.root, text="Hello World", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)
        
        # Create a text widget
        self.textbox = tk.Text(self.root, height=3, font=('Arial', 16))
        self.textbox.pack(padx=10)
        
        # Create an entry widget
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        
        # Create a button
        self.button = tk.Button(self.root, text="CLICK ME", font=('Arial', 18))
        self.button.pack(padx=10, pady=10)
        
        # Create a frame for grid layout
        self.button_frame = tk.Frame(self.root)
        
        # Configure grid columns
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.button_frame.columnconfigure(2, weight=1)
        
        # Create grid buttons
        self._create_grid_buttons()
        
        # Add the frame to the main window
        self.button_frame.pack(fill='x')
        
        # Create a positioned button
        self.positioned_button = tk.Button(self.root, text="Positioned Button")
        self.positioned_button.place(x=200, y=330, height=100, width=100)
    
    def _create_grid_buttons(self):
        """Create buttons in a grid layout."""
        # Row 0
        self.btn1 = tk.Button(self.button_frame, text="1", font=('Arial', 18))
        self.btn1.grid(row=0, column=0, sticky=tk.E+tk.W)
        
        self.btn2 = tk.Button(self.button_frame, text="2", font=('Arial', 18))
        self.btn2.grid(row=0, column=1, sticky=tk.E+tk.W)
        
        self.btn3 = tk.Button(self.button_frame, text="3", font=('Arial', 18))
        self.btn3.grid(row=0, column=2, sticky=tk.E+tk.W)
        
        # Row 1
        self.btn4 = tk.Button(self.button_frame, text="4", font=('Arial', 18))
        self.btn4.grid(row=1, column=0, sticky=tk.E+tk.W)
        
        self.btn5 = tk.Button(self.button_frame, text="5", font=('Arial', 18))
        self.btn5.grid(row=1, column=1, sticky=tk.E+tk.W)
        
        self.btn6 = tk.Button(self.button_frame, text="6", font=('Arial', 18))
        self.btn6.grid(row=1, column=2, sticky=tk.E+tk.W)
    
    def run(self):
        """Start the GUI main loop."""
        self.root.mainloop()


class AdvancedGUI:
    """Advanced GUI with menus, events, and interactive features."""
    
    def __init__(self):
        """Initialize a new advanced GUI window."""
        # Create the main window
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Advanced GUI Demo")
        
        # Create menubar
        self._create_menubar()
        
        # Create main widgets
        self._create_widgets()
        
        # Bind events
        self._bind_events()
    
    def _create_menubar(self):
        """Create menu bar with dropdown menus."""
        self.menubar = tk.Menu(self.root)
        
        # File menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Close", command=self._on_closing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit without prompt", command=exit)
        
        # Action menu
        self.action_menu = tk.Menu(self.menubar, tearoff=0)
        self.action_menu.add_command(label="Show Message", command=self._show_message)
        
        # Add menus to menubar
        self.menubar.add_cascade(menu=self.file_menu, label="File")
        self.menubar.add_cascade(menu=self.action_menu, label="Action")
        
        # Configure the window to use this menubar
        self.root.config(menu=self.menubar)
    
    def _create_widgets(self):
        """Create the main UI widgets."""
        # Label
        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        
        # Text box
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)
        
        # Checkbox
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(
            self.root, 
            text="Show MessageBox", 
            font=('Arial', 16),
            variable=self.check_state
        )
        self.check.pack(padx=10, pady=10)
        
        # Show message button
        self.message_button = tk.Button(
            self.root, 
            text="Show Message", 
            font=('Arial', 18), 
            command=self._show_message
        )
        self.message_button.pack(padx=10, pady=10)
        
        # Clear button
        self.clear_button = tk.Button(
            self.root, 
            text="Clear", 
            font=('Arial', 18), 
            command=self._clear
        )
        self.clear_button.pack(padx=10, pady=10)
    
    def _bind_events(self):
        """Bind event handlers to widgets."""
        # Bind key press event to textbox
        self.textbox.bind("<KeyPress>", self._shortcut)
        
        # Set up window close protocol
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
    
    def _show_message(self):
        """Show the message from the textbox."""
        message = self.textbox.get('1.0', tk.END)
        
        if self.check_state.get() == 0:
            # Print to console
            print(message)
        else:
            # Show in message box
            messagebox.showinfo(title="Message", message=message)
    
    def _shortcut(self, event):
        """Handle keyboard shortcuts."""
        if event.keysym == "Return":
            self._show_message()
    
    def _clear(self):
        """Clear the textbox content."""
        self.textbox.delete('1.0', tk.END)
    
    def _on_closing(self):
        """Handle window closing event."""
        if messagebox.askyesno(title="Quit?", message="Do you really want to close this window?"):
            self._on_closing2()
    
    def _on_closing2(self):
        """Second confirmation for window closing."""
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
            self._on_closing3()
    
    def _on_closing3(self):
        """Final confirmation for window closing."""
        if messagebox.askyesno(title="Quit?", message="This is your last chance to stay"):
            self.root.destroy()
    
    def run(self):
        """Start the GUI main loop."""
        self.root.mainloop()


def run_gui(gui_type):
    """
    Create and run a GUI application.
    
    Args:
        gui_type (str): 'basic' for BasicGUI, 'advanced' for AdvancedGUI
    """
    if gui_type.lower() == 'basic':
        app = BasicGUI()
    elif gui_type.lower() == 'advanced':
        app = AdvancedGUI()
    else:
        print(f"Unknown GUI type: {gui_type}")
        return
    
    app.run()


if __name__ == "__main__":
    print("Select GUI type:")
    print("1. Basic GUI")
    print("2. Advanced GUI")
    
    try:
        choice = int(input("Enter choice (1 or 2): "))
        if choice == 1:
            run_gui('basic')
        elif choice == 2:
            run_gui('advanced')
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number")