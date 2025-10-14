from __future__ import annotations
from typing import Any
from .base import BaseAgent, AgentResponse
from agentic_ai.mock_apis import exim

class EXIMTrendsAgent(BaseAgent):
    name = "exim"

    def run(self, molecule: str, **kwargs: Any) -> AgentResponse:
        return AgentResponse(exim.get_trade_trends(molecule))
