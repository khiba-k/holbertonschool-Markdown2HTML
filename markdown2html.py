"""Script to convert markdown to html.
"""
import sys
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Missing {sys.argv[1]}")
        sys.exit(1)
