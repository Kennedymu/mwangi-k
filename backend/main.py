from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.mwangi_k import router


# ENGINE
app = FastAPI(title="Mwangi K API")


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# CONNECT ROUTER
app.include_router(router)


# ENGINE TEST
@app.get("/")
def home():
    return {
        "status": "Mwangi K API running"
    }