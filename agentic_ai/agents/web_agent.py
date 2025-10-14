from __future__ import annotations
from typing import Any
from .base import BaseAgent, AgentResponse
from agentic_ai.mock_apis import web_search

class WebIntelligenceAgent(BaseAgent):
    name = "web"

    def run(self, query: str, **kwargs: Any) -> AgentResponse:
        return AgentResponse(web_search.web_search(query))
