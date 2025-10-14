from __future__ import annotations
from typing import Any
from .base import BaseAgent, AgentResponse
from agentic_ai.mock_apis import patent

class PatentLandscapeAgent(BaseAgent):
    name = "patent"

    def run(self, molecule: str, **kwargs: Any) -> AgentResponse:
        return AgentResponse(patent.search_patents(molecule))
