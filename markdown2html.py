#!/usr/bin/python3
"""
Advanced script to convert markdown to html with improved text formatting.
"""

import sys
import os
import re

def convert_text_formatting(line):
    """
    Convert markdown text formatting to HTML.
    Supports bold (**text** or __text__) and italic (*text* or _text_).
    Handles formatting within words.
    """
    # Bold formatting first
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.*?)__', r'<b>\1</b>', line)
    
    # Italic formatting
    line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
    line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)
    
    return line

def convertor(md_file, html_file):
    """
    Converts a markdown file to an HTML file with advanced formatting.
    """
    with open(md_file, "r", encoding="utf-8") as md:
        md_content = md.read()

    with open(html_file, "w", encoding="utf-8") as h:
        is_ul = False
        is_ol = False
        is_p = False
        
        # Loop through md content
        lines = md_content.split("\n")
        for i, line in enumerate(lines):
            html_line = ""

            # Checks for headers
            if line.startswith("######"):
                html_line = f"<h6>{convert_text_formatting(line[6:].strip())}</h6>"
                is_ul = is_ol = is_p = False
            elif line.startswith("#####"):
                html_line = f"<h5>{convert_text_formatting(line[5:].strip())}</h5>"
                is_ul = is_ol = is_p = False
            elif line.startswith("####"):
                html_line = f"<h4>{convert_text_formatting(line[4:].strip())}</h4>"
                is_ul = is_ol = is_p = False
            elif line.startswith("###"):
                html_line = f"<h3>{convert_text_formatting(line[3:].strip())}</h3>"
                is_ul = is_ol = is_p = False
            elif line.startswith("##"):
                html_line = f"<h2>{convert_text_formatting(line[2:].strip())}</h2>"
                is_ul = is_ol = is_p = False
            elif line.startswith("#"):
                html_line = f"<h1>{convert_text_formatting(line[1:].strip())}</h1>"
                is_ul = is_ol = is_p = False
            
            # Unordered list
            elif line.startswith("-"):
                if not is_ul:
                    h.write("<ul>\n")
                    is_ul = True
                    is_ol = is_p = False
                html_line = f"<li>{convert_text_formatting(line[1:].strip())}</li>"
            
            # Ordered list
            elif line.startswith("*"):
                if not is_ol:
                    h.write("<ol>\n")
                    is_ol = True
                    is_ul = is_p = False
                html_line = f"<li>{convert_text_formatting(line[1:].strip())}</li>"
            
            # Empty lines
            elif not line.strip():
                # Close existing lists or paragraphs
                if is_ul:
                    h.write("</ul>\n")
                    is_ul = False
                if is_ol:
                    h.write("</ol>\n")
                    is_ol = False
                if is_p:
                    h.write("</p>\n")
                    is_p = False
                continue
            
            # Paragraphs
            else:
                # Close existing lists
                if is_ul:
                    h.write("</ul>\n")
                    is_ul = False
                if is_ol:
                    h.write("</ol>\n")
                    is_ol = False
                
                # Start or continue paragraph
                if not is_p:
                    h.write("<p>\n")
                    is_p = True
                
                # Check if this is a continuation of previous paragraph
                if i > 0 and lines[i-1].strip() and not lines[i-1].startswith(("#", "-", "*")):
                    h.write("\t<br/>\n")
                
                # Convert text formatting and write line
                formatted_line = convert_text_formatting(line.strip())
                html_line = f"\t{formatted_line}"

            # Write line if not empty
            if html_line:
                h.write(html_line + "\n")

        # Close any open tags at end of file
        if is_ul:
            h.write("</ul>\n")
        if is_ol:
            h.write("</ol>\n")
        if is_p:
            h.write("</p>\n")

def main():
    """
    Converts a markdown file to an HTML file.
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(md_file):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    convertor(md_file, html_file)

    sys.exit(0)

if __name__ == "__main__":
    main()