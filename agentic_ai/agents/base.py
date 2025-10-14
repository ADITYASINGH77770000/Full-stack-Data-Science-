from __future__ import annotations
from typing import Any, Dict

class AgentResponse(Dict[str, Any]):
    pass

class BaseAgent:
    name: str = "base"

    def run(self, **kwargs) -> AgentResponse:
        raise NotImplementedError
