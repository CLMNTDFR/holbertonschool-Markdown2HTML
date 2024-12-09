#!/usr/bin/python3
"""
Markdown to HTML converter script.
"""

import sys
import os

def main():
    # Vérifie si le nombre d'arguments est suffisant
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Récupère les noms des fichiers en argument
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Vérifie si le fichier Markdown existe
    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Si toutes les vérifications passent, termine sans erreur
    sys.exit(0)

if __name__ == "__main__":
    main()
