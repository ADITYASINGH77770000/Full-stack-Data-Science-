from __future__ import annotations
from typing import Dict, Any, List
import random

ASSIGNEES = ["Teva", "Sandoz", "Sun", "Lupin", "Pfizer", "Merck"]


def search_patents(molecule: str) -> Dict[str, Any]:
    random.seed("pat-" + molecule)
    results: List[Dict[str, Any]] = []
    for i in range(random.randint(3, 8)):
        results.append({
            "patent_id": f"US{random.randint(8000000, 12000000)}",
            "title": f"Formulation of {molecule} for new use {i+1}",
            "assignee": random.choice(ASSIGNEES),
            "filing_year": random.randint(2010, 2024),
            "expiry_year": random.randint(2025, 2040),
            "status": random.choice(["active", "expired", "pending"]),
            "fto_flag": random.choice(["low", "medium", "high"]),
        })
    return {"molecule": molecule, "patents": results}
