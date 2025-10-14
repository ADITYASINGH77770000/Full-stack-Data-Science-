from __future__ import annotations
from typing import Any
from .base import BaseAgent, AgentResponse
from agentic_ai.mock_apis import iqvia

class IQVIAInsightsAgent(BaseAgent):
    name = "iqvia"

    def run(self, molecule: str | None = None, therapy_area: str | None = None, **kwargs: Any) -> AgentResponse:
        if molecule:
            return AgentResponse(iqvia.get_molecule_market(molecule))
        if therapy_area:
            return AgentResponse(iqvia.get_market_overview(therapy_area))
        raise ValueError("Either molecule or therapy_area must be provided")
