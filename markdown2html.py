#!/usr/bin/python3
"""
Script to convert markdown to html.
"""

import sys
import os

def convertor(md_file, html_file):
    """
    Converts a markdown file to an HTML file.
    """
    with open(md_file, "r", encoding="utf-8") as md:
        md_content = md.read()

    with open(html_file, "a", encoding="utf-8") as html:
        for line in md_content.split("\n"):
            if line.startswith("######"):
                html_line = f"<h6>{line[6:].strip()}</h6>"
            elif line.startswith("#####"):
                html_line = f"<h5>{line[5:].strip()}</h5>"
            elif line.startswith("####"):
                html_line = f"<h4>{line[4:].strip()}</h4>"
            elif line.startswith("###"):
                html_line = f"<h3>{line[3:].strip()}</h3>"
            elif line.startswith("##"):
                html_line = f"<h2>{line[2:].strip()}</h2>"
            elif line.startswith("#"):
                html_line = f"<h1>{line[1:].strip()}</h1>"
            else:
                continue

            html.write(html_line + "\n")

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

    convertor(md_file, html_file)

    sys.exit(0)
if __name__ == "__main__":
    main()
