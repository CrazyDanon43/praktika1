from fastapi import APIRouter

from src.models.healthcheck_models import HealthStatus
from src.services.healthcheck_services import HealthCheckServices

router = APIRouter(prefix="/health", tags=["Health"])
service = HealthCheckServices()


@router.get("/healthcheck", response_model=HealthStatus)
async def healthcheck() -> HealthStatus:
    return service.get_health()
