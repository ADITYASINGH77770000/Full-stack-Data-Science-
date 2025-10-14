from __future__ import annotations
from typing import Any
from .base import BaseAgent, AgentResponse
from agentic_ai.mock_apis import clinical

class ClinicalTrialsAgent(BaseAgent):
    name = "clinical"

    def run(self, molecule: str | None = None, indication: str | None = None, **kwargs: Any) -> AgentResponse:
        return AgentResponse(clinical.fetch_trials(molecule=molecule, indication=indication))
