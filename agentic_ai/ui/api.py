from __future__ import annotations
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import os
from agentic_ai.orchestrator.master import MasterAgent

app = FastAPI(title="Agentic AI Prototype")
master = MasterAgent()

class Query(BaseModel):
    molecule: str
    indication: str

@app.post("/generate")
async def generate(query: Query):
    result = master.generate_ppt(query.molecule, query.indication)
    return JSONResponse(result)

@app.get("/download")
async def download(path: str):
    if not os.path.exists(path):
        return JSONResponse({"error": "file not found"}, status_code=404)
    return FileResponse(path, filename=os.path.basename(path))

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    # In a real system, we would parse and index the PDF. Here we mock success.
    return {"filename": file.filename, "status": "uploaded"}
