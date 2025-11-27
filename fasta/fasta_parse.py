# Python3
# -*- coding: utf-8 -*-
# fasta_parse.py
# Module for parsing FASTA files
# Author: Daniel Anderson, created on 11/24/2025
# Do not copy or distribute without permission, all rights reserved.

from utils.debug import *
import re

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
                    log_verbose_info(f"Found sequence ID: {sequence_id}")
                    sequence_lines = []
                else:
                    sequence_lines.append(line)
                    log_verbose_info(f"Appending sequence line: {line}")
            if sequence_id is not None:
                sequences[sequence_id] = ''.join(sequence_lines)
                log_verbose_info(f"Final sequence for ID {sequence_id}: {sequences[sequence_id][:15]}...")
        
        # keep parsed sequences on the parser instance so sequence_search can use them
        self.sequences = sequences
        return self.sequences
    
    def sequence_search(self, query_sequence):
        """
        Searches for a specific DNA sequence in the parsed sequences.
        """
        matching_ids = []
        for seq_id, sequence in self.sequences.items():
            if query_sequence in sequence:
                matching_ids.append(seq_id)
                log_verbose_info(f"Query sequence found in ID: {seq_id}")
        return matching_ids 
    
    
    def find_sequence_indexes(self, matching_ids, query_sequence):
        """
        Finds the start and end indexes of the query sequence in the matching sequences.
        """
        indexes = {}
        for seq_id in matching_ids:
            sequence = self.sequences.get(seq_id, "")

            matches = [m.start() for m in re.finditer(re.escape(query_sequence), sequence)]

            if matches:
                # convert to (start, end) tuples:
                ranges = [(i, i + len(query_sequence)) for i in matches]
                count = len(ranges)
                indexes[seq_id] = {
                    "count": count,
                    "ranges": ranges
                }
                log_verbose_info(f"Indexes for ID {seq_id}: {ranges}")

        return indexes