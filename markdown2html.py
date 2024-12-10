#!/usr/bin/python3
"""
Script to convert markdown to html.
"""

import sys
import os

if __name__ == "__main__":
    """Converts a markdown file to an HTML file.

    This script takes two command-line arguments:
    1. Markdown file name.
    2. Output path HTML file name.
    
    """

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html" , file=sys.stderr)
        sys.exit(1)

    file_path = os.path.exists(sys.argv[1])
    if not file_path:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

