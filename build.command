#!/bin/bash
cd "$(dirname "$0")"
python3 build_pages.py
echo "✔ Pages générées."
read -p "Appuyez sur Entrée pour fermer..."