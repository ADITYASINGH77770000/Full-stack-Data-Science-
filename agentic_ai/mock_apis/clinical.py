from __future__ import annotations
from typing import Dict, Any, List
import random

SPONSORS = ["NIH", "AstraZeneca", "Novartis", "J&J", "Roche"]
INDICATIONS = ["COPD", "Asthma", "Diabetes", "Hypertension", "GERD"]


def fetch_trials(molecule: str | None = None, indication: str | None = None) -> Dict[str, Any]:
    random.seed(f"ct-{molecule}-{indication}")
    trials: List[Dict[str, Any]] = []
    for i in range(random.randint(3, 10)):
        trials.append({
            "nct_id": f"NCT{random.randint(10000000, 99999999)}",
            "title": f"Study {i+1} of {molecule or 'Candidate'} in {indication or random.choice(INDICATIONS)}",
            "phase": random.choice(["I", "II", "III", "IV"]),
            "sponsor": random.choice(SPONSORS),
            "status": random.choice(["Recruiting", "Completed", "Active, not recruiting"]),
        })
    return {"molecule": molecule, "indication": indication, "trials": trials}
