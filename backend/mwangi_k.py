from fastapi import APIRouter
import json
from pathlib import Path


# ==========================================
# ROUTER
# ==========================================

router = APIRouter()


# ==========================================
# MWANGI K JSON FILE
# ==========================================

JSON_FILE = Path(__file__).resolve().parent.parent / "mwangi-k.json"


# ==========================================
# LOAD MWANGI K
# ==========================================

def load_mwangi_k():
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


mwangi_k = load_mwangi_k()


# ==========================================
# SAVE MWANGI K
# ==========================================

def save_mwangi_k():
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(
            mwangi_k,
            file,
            indent=4,
            ensure_ascii=False
        )


# ==========================================
# GET MWANGI K
# ==========================================

@router.get("/cv")
def get_mwangi_k():
    return mwangi_k


# ==========================================
# POST MWANGI K
# ==========================================

@router.post("/cv")
def post_mwangi_k(data: dict):

    mwangi_k.clear()
    mwangi_k.update(data)

    save_mwangi_k()

    return {
        "message": "Mwangi K posted",
        "mwangi_k": mwangi_k
    }


# ==========================================
# PUT / EDIT MWANGI K
# ==========================================

@router.put("/cv")
def put_mwangi_k(data: dict):

    mwangi_k.update(data)

    save_mwangi_k()

    return {
        "message": "Mwangi K updated",
        "mwangi_k": mwangi_k
    }


# ==========================================
# DELETE MWANGI K
# ==========================================

@router.delete("/cv")
def delete_mwangi_k():

    mwangi_k.clear()

    save_mwangi_k()

    return {
        "message": "Mwangi K deleted"
    }