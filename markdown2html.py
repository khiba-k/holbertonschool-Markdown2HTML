"""
Script to convert markdown to html.
"""

import sys
from pathlib import Path

def main():
    """Converts a markdown file to an HTML file.

    This script takes two command-line arguments:
    1. Markdown file name.
    2. Output path HTML file name.

    It checks if the correct number of arguments are provided and whether the markdown
    file exists. If the file is missing or the arguments are incorrect, the script exits
    with an error message.

    Returns:
        None: The function prints the status to the console and exits on error.
    """
    
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Missing {sys.argv[1]}")
        sys.exit(1)

if __name__ == "__main__":
    main()

