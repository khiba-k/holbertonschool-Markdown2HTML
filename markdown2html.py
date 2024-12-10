#!/usr/bin/python3
"""
Script to convert markdown to html.
"""

import sys
import os

def main():
    """
    Converts a markdown file to an HTML file.
    """

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html" , file=sys.stderr)
        sys.exit(1)

    file_path = os.path.exists(sys.argv[1])
    if not file_path:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)
if __name__ == "__main__":
    main()
