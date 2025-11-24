# Python3
# -*- coding: utf-8 -*-
# fasta_parse.py
# Module for parsing FASTA files
# Author: Daniel Anderson, created on 11/24/2025
# Do not copy or distribute without permission, all rights reserved.

from utils.debug import *

class FastaParser:
    """
    A class to parse FASTA files and extract sequences.
    Attributes:
        file_path (str): Path to the FASTA file.
        sequences (dict): Dictionary to hold sequence IDs and their corresponding sequences.
    
    Methods:
        load(): Parses the FASTA file and returns a dictionary of sequences.
    
    Useage:
        parser = FastaParser("path/to/fasta/file.fasta")
        sequences = parser.load()
        
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.sequences = {}

    def load(self):
        """
        Parses a FASTA file and returns a dictionary with sequence IDs as keys
        and sequences as values.

        :param file_path: Path to the FASTA file
        :return: Dictionary of sequences
        """
        sequences = {}

        with open(self.file_path, 'r') as fasta_file:
            sequence_id = None
            sequence_lines = []

            for line in fasta_file:
                line = line.strip()
                if line.startswith('>'):
                    if sequence_id is not None:
                        sequences[sequence_id] = ''.join(sequence_lines)
                    id_bound = line.find(' ', 1)
                    sequence_id = line[1:id_bound] if id_bound != -1 else line[1:]  # Remove '>' character, get ID only
                    log_debug_info(f"Found sequence ID: {sequence_id}")
                    sequence_lines = []
                else:
                    sequence_lines.append(line)
                    log_debug_info(f"Appending sequence line: {line}")
            if sequence_id is not None:
                sequences[sequence_id] = ''.join(sequence_lines)
                log_debug_info(f"Final sequence for ID {sequence_id}: {sequences[sequence_id]}")
            
        return sequences