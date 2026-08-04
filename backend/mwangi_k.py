from fastapi import APIRouter


# ==========================================
# ROUTER
# ==========================================

router = APIRouter()


# ==========================================
# MWANGI K CV OBJECT
# ==========================================

mwangi_k = {}


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

    return {
        "message": "Mwangi K deleted"
    }