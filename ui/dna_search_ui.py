from tkinter import Tk, Label, Entry, Button, Text, END, messagebox

MAIN_LABEL_TEXT = "Enter DNA Sequence:"
APP_NAME = "DNA Sequence Searcher"

class DNASearchUI:

    """
    A simple GUI for searching DNA sequences.
    Attributes:
        master (Tk): The main window of the application.

    Methods:

    Use: 
        ui = DNASearchUI(controller)
        ui.run()
    """

    def __init__(self, controller):
        # not inheriting from Tk directly, so no super init

        self.controller = controller
        # ensure controller knows about this UI (safe even if app.py also sets it)
        if self.controller:
            self.controller.ui = self

        self.master = Tk()
        self.master.title(APP_NAME)

        self.label = Label(self.master, text=MAIN_LABEL_TEXT)
        self.label.pack()
        # entry for DNA sequence
        self.entry = Entry(self.master, width=60)
        self.entry.pack(padx=8, pady=(4, 8))

        # buttons
        self.button_frame = None
        self.search_button = Button(self.master, text="Search", command=self._on_search)
        self.search_button.pack(side='left', padx=8, pady=4)

        self.reset_button = Button(self.master, text="Reset", command=self._on_reset)
        self.reset_button.pack(side='left', padx=8, pady=4)
        
        self.import_button = Button(self.master, text="Import FASTA", command=self._on_import)
        self.import_button.pack(side='left', padx=8, pady=4)

        # results display
        self.result_text = Text(self.master, height=15, width=80)
        self.result_text.pack(padx=8, pady=8)

        # allow Enter key to trigger search
        self.master.bind('<Return>', lambda event: self._on_search())

    def _on_search(self):
        if not self.controller:
            messagebox.showerror("Controller missing", "No controller attached to the UI.")
            return
        self.controller.search_dna_sequence()

    def _on_reset(self):
        if not self.controller:
            messagebox.showerror("Controller missing", "No controller attached to the UI.")
            return
        self.controller.reset()

    def _on_import(self):
        if not self.controller:
            messagebox.showerror("Controller missing", "No controller attached to the UI.")
            return
        # Assuming controller has an import_fasta method
        if hasattr(self.controller, 'import_fasta'):
            self.controller.import_fasta()
        else:
            messagebox.showerror("Not Implemented", "Import FASTA functionality is not implemented in the controller.")

    def _on_load(self):
        if not self.controller:
            messagebox.showerror("Controller missing", "No controller attached to the UI.")
            return
        # Assuming controller has a load method
        if hasattr(self.controller, 'load'):
            self.controller.load()
        else:
            messagebox.showerror("Not Implemented", "Load functionality is not implemented in the controller.")

    def run(self):
        """Start the Tk main loop."""
        self.master.mainloop()

    def set_result_text(self, text):
        """Set the result text area content."""
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, text)

    def append_result_text(self, text):
        """Append text to the result text area."""
        self.result_text.insert(END, text)




