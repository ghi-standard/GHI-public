from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Union

import requests

BASE_URL = "http://127.0.0.1:8000/v1/ghi"


def _get(path: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Helper HTTP GET sur l'API sandbox locale.

    Nécessite que le moteur sandbox tourne en local sur 127.0.0.1:8000.
    """
    url = f"{BASE_URL}/{path}"
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    return resp.json()


def test_snapshot_basic_structure():
    """
    Le snapshot global doit exposer les champs clés du modèle v1.1.
    """
    data = _get("snapshot")
    assert isinstance(data, dict)

    # Champs de métadonnées principaux
    assert "timestamp_utc" in data
    assert "engine_sandbox_version" in data

    # Champs de coût globaux (min / avg / max)
    for key in ("global_min_cost_usd", "global_avg_cost_usd", "global_max_cost_usd"):
        assert key in data

    min_cost = data["global_min_cost_usd"]
    avg_cost = data["global_avg_cost_usd"]
    max_cost = data["global_max_cost_usd"]

    assert min_cost <= avg_cost <= max_cost


def test_regions_non_empty():
    """
    L'endpoint /regions doit renvoyer un objet avec au moins une région.
    """
    payload = _get("regions")
    assert isinstance(payload, dict)

    assert "regions" in payload
    regions = payload["regions"]
    assert isinstance(regions, list)
    assert len(regions) > 0

    # Champ de comptage cohérent
    if "region_count" in payload:
        assert payload["region_count"] == len(regions)


def test_single_region_detail():
    """
    Chaque région doit contenir des champs de base (id, name).
    """
    payload = _get("regions")
    regions = payload["regions"]
    first = regions[0]

    assert "id" in first
    assert "name" in first
    assert isinstance(first["id"], str)
    assert isinstance(first["name"], str)


def test_history_monotonic_timestamps():
    """
    L'historique global doit être trié par date croissante.
    """
    history = _get("history")
    assert isinstance(history, dict)
    assert "points" in history

    points = history["points"]
    assert isinstance(points, list)
    assert len(points) > 0

    dates = [p["date"] for p in points]
    # Format attendu : YYYY-MM-DD → comparaison lexicographique suffisante
    assert dates == sorted(dates)


def test_metadata_object():
    """
    L'endpoint /metadata doit exposer les informations de version de l'API sandbox.
    """
    meta = _get("metadata")
    assert isinstance(meta, dict)

    # API v1.1 active
    assert meta.get("api_current") == "1.1"
    assert "api_supported" in meta
    assert "available_endpoints" in meta

    endpoints = meta["available_endpoints"]
    assert "/v1/ghi/snapshot" in endpoints
    assert "/v1/ghi/history" in endpoints
    assert "/v1/ghi/regions" in endpoints