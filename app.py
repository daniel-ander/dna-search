# This will serve as the entry point for the application
# Flask is a lightweight WSGI web application framework in Python

from ui.dna_search_ui import DNASearchUI
from ui.dna_search_ui_controller import DNASearchUIController

if __name__ == "__main__":
    controller = DNASearchUIController(None)
    app = DNASearchUI(controller)
    app.run()