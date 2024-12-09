#!/usr/bin/python3
"""
Markdown to HTML converter script - Task 1.
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
        for i in range(6, 0, -1):  # Vérifie les niveaux de titre de # à ######
            # Exactement i dièses suivis d'un espace
            if line.startswith('#' * i + ' '):
                line = f'<h{i}>{line[i+1:].strip()}</h{i}>\n'
                break
        converted_lines.append(line)
    return converted_lines


def main():
    """
    Main function that verifies arguments, file existence, and converts Markdown to HTML.
    """
    # Vérifie si le nombre d'arguments est suffisant
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    # Récupère les noms des fichiers en argument
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Vérifie si le fichier Markdown existe
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        exit(1)

    # Lit le contenu du fichier Markdown
    with open(markdown_file, 'r') as md:
        lines = md.readlines()

    # Convertit les en-têtes Markdown en HTML
    converted_lines = convert_markdown_heading_to_html(lines)

    # Écrit les résultats dans le fichier HTML
    with open(html_file, 'w') as html:
        html.writelines(converted_lines)

    exit(0)


if __name__ == "__main__":
    main()
