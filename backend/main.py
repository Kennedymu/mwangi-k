from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

from backend.mwangi_k import router


app = FastAPI(title="Mwangi K API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(router)


BASE_DIR = Path(__file__).resolve().parent.parent
HTML_FILE = BASE_DIR / "mwangi-k.html"


# PUBLIC WEB DISPLAY
@app.get("/", include_in_schema=False)
def home():
    return FileResponse(HTML_FILE)


# API STATUS
@app.get("/status")
def status():
    return {
        "status": "Mwangi K API running"
    }