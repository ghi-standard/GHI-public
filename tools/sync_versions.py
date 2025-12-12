#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # racine repo
LAYOUT = ROOT / "layout.html"                       # ajuste si besoin
TARGET_DIR = ROOT                                   # ou ROOT/"public" selon ton repo

def extract_versions(layout_text: str) -> dict:
    def grab(pattern: str, label: str) -> str:
        m = re.search(pattern, layout_text, flags=re.IGNORECASE)
        if not m:
            raise RuntimeError(f"Impossible de trouver {label} dans le layout.")
        return m.group(1)

    return {
        "API": grab(r"\bAPI\s*(v[0-9]+(?:\.[0-9]+)*)\b", "API vX.Y"),
        "METHODOLOGY": grab(r"\bMethodology\s*(v[0-9]+(?:\.[0-9]+)*)\b", "Methodology vX.Y"),
        "ENGINE": grab(r"\bEngine\s*(v[0-9]+(?:\.[0-9]+(?:-[a-z0-9._-]+)?)?)\b", "Engine vX.Y(-suffix)"),
        "GHI": grab(r"\bGHI\s*(v[0-9]+(?:\.[0-9]+)*)\b", "GHI vX.Y"),
    }

def patch_content(html: str, v: dict) -> str:
    # Remplacements “en dur” -> versions layout
    html = re.sub(r"\bAPI\s*v[0-9]+(?:\.[0-9]+)*\b", f"API {v['API']}", html, flags=re.IGNORECASE)
    html = re.sub(r"\bMethodology\s*v[0-9]+(?:\.[0-9]+)*\b", f"Methodology {v['METHODOLOGY']}", html, flags=re.IGNORECASE)
    html = re.sub(r"\bEngine\s*v[0-9]+(?:\.[0-9]+(?:-[a-z0-9._-]+)?)?\b", f"Engine {v['ENGINE']}", html, flags=re.IGNORECASE)

    # Cas fréquent dans tes tableaux : “GHI v1.x (example)”
    html = re.sub(r"\bGHI\s*v[0-9]+(?:\.[0-9]+)?(?:\.[0-9]+)?(?:\.x|x)\b", f"GHI {v['GHI']}", html, flags=re.IGNORECASE)
    html = re.sub(r"\bGHI\s*v[0-9]+(?:\.[0-9]+)*\b", f"GHI {v['GHI']}", html, flags=re.IGNORECASE)

    return html

def main():
    layout_text = LAYOUT.read_text(encoding="utf-8")
    versions = extract_versions(layout_text)

    files = sorted(TARGET_DIR.rglob("*.content.html"))
    if not files:
        raise RuntimeError("Aucun fichier *.content.html trouvé.")

    changed = 0
    for f in files:
        old = f.read_text(encoding="utf-8")
        new = patch_content(old, versions)
        if new != old:
            f.write_text(new, encoding="utf-8")
            changed += 1

    print("Versions détectées depuis layout:")
    for k, val in versions.items():
        print(f"  - {k}: {val}")
    print(f"Fichiers modifiés: {changed}/{len(files)}")

if __name__ == "__main__":
    main()