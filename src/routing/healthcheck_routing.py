from fastapi import APIRouter
from src.services.healthcheck_services import HealthCheckServices
from src.models.healthcheck_models import HealthStatus

router = APIRouter(prefix="/health", tags=["Health"])
service = HealthCheckServices()

@router.get("/healthcheck", response_model=HealthStatus)
async def healthcheck():
    return service.get_health()