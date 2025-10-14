from __future__ import annotations
from typing import Dict, Any
import random

THERAPIES = [
    "Respiratory", "Cardiology", "Oncology", "Endocrinology", "Gastroenterology",
]

MOLECULES = [
    "Budesonide", "Metformin", "Atorvastatin", "Pembrolizumab", "Omeprazole",
]


def get_market_overview(therapy_area: str) -> Dict[str, Any]:
    random.seed(therapy_area)
    size_2024 = random.randint(200, 500) * 1e6
    cagr = round(random.uniform(4.0, 12.0), 1)
    competitors = random.randint(5, 25)
    return {
        "therapy_area": therapy_area,
        "market_size_2024_usd": size_2024,
        "cagr_percent": cagr,
        "num_competitors": competitors,
    }


def get_molecule_market(molecule: str) -> Dict[str, Any]:
    random.seed(molecule)
    size_2024 = random.randint(50, 300) * 1e6
    cagr = round(random.uniform(2.0, 10.0), 1)
    share_top3 = round(random.uniform(35, 75), 1)
    return {
        "molecule": molecule,
        "market_size_2024_usd": size_2024,
        "cagr_percent": cagr,
        "share_top3_percent": share_top3,
    }
