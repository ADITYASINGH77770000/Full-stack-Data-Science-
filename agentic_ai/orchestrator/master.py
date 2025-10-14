from __future__ import annotations
from typing import Any, Dict, List

from agentic_ai.agents.iqvia_agent import IQVIAInsightsAgent
from agentic_ai.agents.exim_agent import EXIMTrendsAgent
from agentic_ai.agents.patent_agent import PatentLandscapeAgent
from agentic_ai.agents.clinical_agent import ClinicalTrialsAgent
from agentic_ai.agents.internal_agent import InternalKnowledgeAgent
from agentic_ai.agents.web_agent import WebIntelligenceAgent
from agentic_ai.agents.report_agent import ReportGeneratorAgent

class MasterAgent:
    def __init__(self) -> None:
        self.iqvia = IQVIAInsightsAgent()
        self.exim = EXIMTrendsAgent()
        self.patent = PatentLandscapeAgent()
        self.clinical = ClinicalTrialsAgent()
        self.internal = InternalKnowledgeAgent()
        self.web = WebIntelligenceAgent()
        self.report = ReportGeneratorAgent()

    def build_story(self, molecule: str, indication: str) -> Dict[str, Any]:
        # Decompose into tasks and aggregate
        market = self.iqvia.run(molecule=molecule)
        trade = self.exim.run(molecule=molecule)
        patents = self.patent.run(molecule=molecule)
        trials = self.clinical.run(molecule=molecule, indication=indication)
        internal_hits = self.internal.run(query=indication)
        web_hits = self.web.run(query=f"{molecule} {indication} unmet needs")

        unmet_needs: List[str] = []
        for d in internal_hits.get("results", []):
            for h in d.get("highlights", []):
                unmet_needs.append(h)
        for r in web_hits.get("results", []):
            unmet_needs.append(f"{r['title']}: {r['snippet']}")

        hypotheses = [
            f"Assess alternative dosage forms of {molecule} for pediatrics",
            f"Explore {molecule} use in related inflammatory diseases",
            "Investigate device or delivery innovation to reduce exacerbations",
        ]

        story: Dict[str, Any] = {
            "molecule": molecule,
            "indication": indication,
            "market": market,
            "trade": trade,
            "patents": patents.get("patents", []),
            "clinical_trials": trials.get("trials", []),
            "unmet_needs": unmet_needs[:6],
            "repurposing_hypotheses": hypotheses,
            "references": [r.get("url") for r in web_hits.get("results", [])],
        }
        return story

    def generate_ppt(self, molecule: str, indication: str) -> Dict[str, Any]:
        story = self.build_story(molecule, indication)
        return self.report.run(story=story)
