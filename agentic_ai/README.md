# Agentic AI Prototype for Pharmaceutical Innovation

This prototype demonstrates an Agentic AI system that orchestrates multiple worker agents over mock data sources to accelerate literature and market research for pharmaceutical product innovation.

## Components
- Master Agent (LangGraph): task decomposition, orchestration, synthesis.
- Worker Agents (mock integrations): IQVIA, EXIM, Patent, ClinicalTrials, Internal Knowledge, Web Intelligence, Report Generator.
- UI: Minimal FastAPI endpoints for querying and downloading reports.
- Report: 5-slide PPT story from molecule search to innovative product concept.

## Quickstart
1. Create venv and install deps
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r agentic_ai/requirements.txt
```
2. Run API
```bash
uvicorn agentic_ai.ui.api:app --reload
```
3. Generate a sample PPT directly
```bash
python agentic_ai/scripts/generate_ppt.py --molecule "Budesonide" --indication "COPD"
```

Artifacts are saved under `agentic_ai/reports/archive`.
