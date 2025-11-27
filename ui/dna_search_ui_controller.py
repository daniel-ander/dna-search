"""
Controller module for DNA search UI components.
"""

from tkinter import END, filedialog, messagebox
from fasta.fasta_parse import FastaParser
import pprint

class DNASearchUIController:
    """
    Controller for managing interactions in the DNA search UI.

    Attributes:
        ui (DNASearchUI): The UI instance being controlled.

    Methods:
        search_dna_sequence: Handles the DNA sequence search logic.
    """
    def __init__(self, ui):
        self.ui = ui

    def reset(self):
        """
        Resets the UI components to their default state.
        """
        self.ui.entry.delete(0, END)
        self.ui.result_text.delete(1.0, END)

    def display_fasta_sequences(self, file_path):
        """
        Loads the contents of the FASTA file into the UI text window
        """

        sequences = {}
        # create and keep the parser so searches can use it later
        self.parser = FastaParser(file_path)
        sequences = self.parser.load()
        pretty = pprint.pformat(sequences, indent=4)
        self.ui.set_result_text(pretty)

    def import_fasta(self):
        """
        Opens a file dialog to import a FASTA file and display its sequences.

        """
        file_path = filedialog.askopenfilename(
            title="Select FASTA File",
            filetypes=[("FASTA files", "*.fasta *.fa"), ("All files", "*.*")]
        )
        if file_path:
            self.display_fasta_sequences(file_path)

    def search_dna_sequence(self):
        """
        Searches for the DNA sequence entered in the UI.
        """
        dna_sequence = self.ui.entry.get().strip()
        if not dna_sequence:
            messagebox.showwarning("Input Error", "Please enter a DNA sequence to search.")
            return

        self.ui.set_result_text(f"Searching for DNA sequence: {dna_sequence}\n\n")
        # ensure we have a parser instance
        if not hasattr(self, "parser"):
            messagebox.showwarning("No FASTA", "Please import a FASTA file before searching.")
            return

        found_ids = self.parser.sequence_search(dna_sequence)
        if found_ids:
            self.ui.set_result_text("Found in IDs:\n" + "\n".join(found_ids))
            indexes = self.parser.find_sequence_indexes(found_ids, dna_sequence)
            pretty_indexes = pprint.pformat(indexes, indent=4)
            self.ui.append_result_text("\n\nIndexes:\n" + pretty_indexes)
        else:
            self.ui.set_result_text("No matching sequences found.")