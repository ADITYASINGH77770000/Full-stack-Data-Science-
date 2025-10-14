from __future__ import annotations
from typing import Dict, Any, List

MOCK_DOCS: List[Dict[str, Any]] = [
    {"id": "DOC-001", "title": "Respiratory Strategy 2024", "highlights": [
        "Shift towards fixed-dose combinations",
        "Opportunity in pediatric formulations",
        "Need for device innovation to improve adherence",
    ]},
    {"id": "DOC-002", "title": "Field Insights India Q3", "highlights": [
        "High patient burden in tier-2 cities",
        "Limited access to biologics",
        "Price sensitivity drives generic switches",
    ]},
]


def search_internal(query: str) -> Dict[str, Any]:
    hits = [d for d in MOCK_DOCS if query.lower() in d["title"].lower()]
    return {"query": query, "results": hits}
