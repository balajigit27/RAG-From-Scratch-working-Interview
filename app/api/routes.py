from fastapi import APIRouter
from fastapi import FastAPI

app = FastAPI()
router = APIRouter()

@router.post("/chat")
def chat(query: str):

    return {
        "response": "Hello"
    }

app.include_router(router, prefix="/api")