#!/usr/bin/env python3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(BASE_DIR, "public")

layout_path = os.path.join(PUBLIC, "layout.html")

# Charger layout.html
with open(layout_path, "r", encoding="utf-8") as f:
    layout = f.read()

# Repérer le marqueur de contenu
PLACEHOLDER = "<!-- PAGE_CONTENT -->"

# Lister tous les fichiers *.content.html dans public/
content_files = [
    f for f in os.listdir(PUBLIC)
    if f.endswith(".content.html")
]

print("📄 Pages détectées :", content_files)

for content_file in content_files:
    page_name = content_file.replace(".content.html", ".html")

    print(f"⚙ Génération : {page_name}")

    # Charger le contenu spécifique
    with open(os.path.join(PUBLIC, content_file), "r", encoding="utf-8") as f:
        content_html = f.read()

    # Injecter dans layout
    final_page = layout.replace(PLACEHOLDER, content_html)

    # Sauvegarder dans un fichier final
    with open(os.path.join(PUBLIC, page_name), "w", encoding="utf-8") as f:
        f.write(final_page)

print("✔ Toutes les pages ont été générées avec succès !")