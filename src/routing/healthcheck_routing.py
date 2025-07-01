from fastapi import APIRouter
from src.services.healthcheck_services import healthstatus

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/healthcheck", response_model=healthstatus)
async def healthcheck():
    return {"status": True}
