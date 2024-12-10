#!/usr/bin/python3
"""
Script to convert markdown to html.
"""

import sys
import os

def set_ul_false(is_ul, h):
    """
    Closes an unordered list if it's open.
    """
    if is_ul:
        h.write("</ul>\n")
        is_ul = False
    return is_ul

def set_ol_false(is_ol, h):
    """
    Closes an unordered list if it's open.
    """
    if is_ol:
        h.write("</ol>\n")
        is_ol = False
    return is_ol

def convertor(md_file, html_file):
    """
    Converts a markdown file to an HTML file.
    """
    with open(md_file, "r", encoding="utf-8") as md:
        md_content = md.read()

    with open(html_file, "a", encoding="utf-8") as h:
        is_ul = False
        is_ol = False
        for line in md_content.split("\n"):
            html_line = ""

            if line.startswith("-"):
                is_ol = set_ol_false(is_ol, h)
                if not is_ul:
                    h.write("<ul>\n")
                    is_ul = True
                html_line = f"<li>{line[1:].strip()}</li>"
            elif line.startswith("*"):
                is_ul = set_ul_false(is_ul, h)
                if not is_ol:
                    h.write("<ol>\n")
                    is_ol = True
                html_line = f"<li>{line[1:].strip()}</li>"
            elif line.startswith("######"):
                is_ul = set_ul_false(is_ul, h)
                is_ol = set_ol_false(is_ol, h)
                html_line = f"<h6>{line[6:].strip()}</h6>"
            elif line.startswith("#####"):
                is_ul = set_ul_false(is_ul, h)
                is_ol = set_ol_false(is_ol, h)
                html_line = f"<h5>{line[5:].strip()}</h5>"
            elif line.startswith("####"):
                is_ul = set_ul_false(is_ul, h)
                html_line = f"<h4>{line[4:].strip()}</h4>"
            elif line.startswith("###"):
                is_ul = set_ul_false(is_ul, h)
                is_ol = set_ol_false(is_ol, h)
                html_line = f"<h3>{line[3:].strip()}</h3>"
            elif line.startswith("##"):
                is_ul = set_ul_false(is_ul, h)
                is_ol = set_ol_false(is_ol, h)
                html_line = f"<h2>{line[2:].strip()}</h2>"
            elif line.startswith("#"):
                is_ul = set_ul_false(is_ul, h)
                is_ol = set_ol_false(is_ol, h)
                html_line = f"<h1>{line[1:].strip()}</h1>"
            else:
                is_ul = set_ul_false(is_ul, h)
                is_ol = set_ol_false(is_ol, h)
                if line.strip():
                    html_line = f"<p>{line.strip()}</p>"

            if html_line:
                h.write(html_line + "\n")

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
