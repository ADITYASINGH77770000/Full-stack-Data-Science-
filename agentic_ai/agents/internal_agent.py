from __future__ import annotations
from typing import Any
from .base import BaseAgent, AgentResponse
from agentic_ai.mock_apis import internal_docs

class InternalKnowledgeAgent(BaseAgent):
    name = "internal"

    def run(self, query: str, **kwargs: Any) -> AgentResponse:
        return AgentResponse(internal_docs.search_internal(query))
