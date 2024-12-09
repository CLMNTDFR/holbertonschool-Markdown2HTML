#!/usr/bin/python3
"""
Markdown to HTML converter script - Task 0.
"""

import sys
import os

def main():
    """
    Main function that verifies arguments and file existence.
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

    # Aucun traitement nécessaire dans la tâche 0
    exit(0)


if __name__ == "__main__":
    main()
