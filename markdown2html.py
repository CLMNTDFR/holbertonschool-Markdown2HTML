#!/usr/bin/python3
"""
Markdown to HTML converter script
"""

import sys
import os


def convert_markdown_heading_to_html(lines):
    """
    Convert Markdown heading syntax to HTML.

    Args:
        lines (list): List of lines from the Markdown file.

    Returns:
        list: List of converted lines with HTML headings.
    """
    converted_lines = []
    for line in lines:
        for i in range(6, 0, -1):
            # Exactly i hashes followed by a space
            if line.startswith("#" * i + " "):
                line = f"<h{i}>{line[i+1:].strip()}</h{i}>\n"
                break
        converted_lines.append(line)
    return converted_lines


def convert_markdown_ul_list_to_html(lines):
    """
    Convert Markdown unordered list syntax to HTML.

    Args:
        lines (list): List of lines from the Markdown file.

    Returns:
        list: List of converted lines with HTML unordered list.
    """
    in_list = False
    html_lines = []

    for line in lines:
        if line.startswith("- "):  # If the line starts with '- '
            line_content = line[2:].strip()  # Extract text after the dash
            if not in_list:
                # Open a <ul> tag for the list
                html_lines.append("<ul>\n")
                in_list = True
            # Convert each item to <li>
            html_lines.append(f"   <li>{line_content}</li>\n")
        else:
            if in_list:
                # Close the <ul> tag at the end of the list
                html_lines.append("</ul>\n")
                in_list = False
            # Add the line without modification
            html_lines.append(line)

    if in_list:
        html_lines.append("</ul>\n")

    return html_lines


def convert_markdown_ol_list_to_html(lines):
    """
    Convert Markdown ordered list syntax to HTML.

    Args:
        lines (list): List of lines from the Markdown file.

    Returns:
        list: List of converted lines with HTML ordered list.
    """
    in_list = False
    html_lines = []

    for line in lines:
        if line.lstrip().startswith(
            tuple(f"{i}. " for i in range(1, 10))
        ):  # If line starts with '1. ', '2. ', etc.
            line_content = line.split(". ", 1)[
                1
            ].strip()  # Extract text after the number and dot
            if not in_list:
                # Open an <ol> tag for the list
                html_lines.append("<ol>\n")
                in_list = True
            # Convert each item to <li>
            html_lines.append(f"   <li>{line_content}</li>\n")
        else:
            if in_list:
                # Close the <ol> tag at the end of the list
                html_lines.append("</ol>\n")
                in_list = False
            # Add the line without modification
            html_lines.append(line)

    if in_list:
        html_lines.append("</ol>\n")

    return html_lines


def main():
    """
    Main function that verifies arguments, file existence
    and converts Markdown to HTML.
    """
    # Check if the number of arguments is sufficient
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    # Get the file names from the arguments
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        exit(1)

    # Read the content of the Markdown file
    with open(markdown_file, "r") as md:
        lines = md.readlines()

    # Convert Markdown headings to HTML
    converted_lines = convert_markdown_heading_to_html(lines)

    # Convert Markdown unordered lists to HTML
    converted_lines = convert_markdown_ul_list_to_html(converted_lines)

    # Convert Markdown ordered lists to HTML
    converted_lines = convert_markdown_ol_list_to_html(converted_lines)

    # Write the converted lines to the HTML file
    with open(html_file, "w") as html:
        html.writelines(converted_lines)

    exit(0)


if __name__ == "__main__":
    main()
