from fastapi import APIRouter
from services.healthcheck_services import HealthCheckServices
from models.healthcheck_models import HealthStatus

router = APIRouter(prefix="/health", tags=["Health"])
service = HealthCheckServices()

@router.get("/healthcheck", response_model=HealthStatus)
async def healthcheck():
    return service.get_health()