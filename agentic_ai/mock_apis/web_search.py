from __future__ import annotations
from typing import Dict, Any, List

MOCK_RESULTS: List[Dict[str, Any]] = [
    {"url": "https://who.int/respiratory/copd-guidelines", "title": "WHO COPD guideline 2024", "snippet": "Updated recommendations on COPD management and inhaled corticosteroids."},
    {"url": "https://nejm.org/article/ics-copd", "title": "NEJM: ICS in COPD", "snippet": "Evidence on efficacy and risks of inhaled corticosteroids in COPD."},
    {"url": "https://clinicaltrials.gov/copd-ics", "title": "ClinicalTrials COPD ICS", "snippet": "Overview of ongoing ICS-related trials in COPD."}
]


def web_search(query: str) -> Dict[str, Any]:
    return {"query": query, "results": MOCK_RESULTS}
