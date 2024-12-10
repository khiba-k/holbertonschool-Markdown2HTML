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

    #Checks if there are two args provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html" , file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]
    
    #Checks if the file exists
    if not os.path.exists(md_file):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)
if __name__ == "__main__":
    main()
