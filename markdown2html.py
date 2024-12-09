#!/usr/bin/python3
"""
Markdown to HTML converter script - Task 2.
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
            # Exactement i dièses suivis d'un espace
            if line.startswith('#' * i + ' '):
                line = f'<h{i}>{line[i+1:].strip()}</h{i}>\n'
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
        if line.startswith('- '):  # Si la ligne commence par '- '
            line_content = line[2:].strip()  # Extrait le texte après le tiret
            if not in_list:
                # Ouvre une balise <ul> pour la liste
                html_lines.append('<ul>\n')
                in_list = True
            # Convertit chaque élément en <li>
            html_lines.append(f'   <li>{line_content}</li>\n')
        else:
            if in_list:
                # Ferme la balise <ul> à la fin de la liste
                html_lines.append('</ul>\n')
                in_list = False
            # Ajoute la ligne sans modification si ce n'est pas un élément de liste
            html_lines.append(line)

    if in_list:  # Si la liste se termine par un élément sans une ligne vide après
        html_lines.append('</ul>\n')

    return html_lines


def main():
    """
    Main function that verifies arguments, file existence
    and converts Markdown to HTML.
    """
    # Vérifie si le nombre d'arguments est suffisant
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
               file=sys.stderr)
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

    # Convertit les listes non ordonnées Markdown en HTML
    converted_lines = convert_markdown_ul_list_to_html(converted_lines)

    # Écrit les résultats dans le fichier HTML
    with open(html_file, 'w') as html:
        html.writelines(converted_lines)

    exit(0)


if __name__ == "__main__":
    main()
