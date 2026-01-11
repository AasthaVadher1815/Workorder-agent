from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/process")
async def process_excel(file: UploadFile = File(...)):
    return {"status": "not_implemented"}
