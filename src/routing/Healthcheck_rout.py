from typing import List
from fastapi import APIRouter, Depends, HTTPException
from src.depends import get_health_service
from src.models.Healthcheck_mod import HealthStatus
from src.services.Healthcheck_serv import HealthHealth

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/healthcheck", response_model=HealthStatus)
async def healthcheck():
    return {"status": True}

@router.get(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=List[HealthStatus],
    description="Получение листинга всех статусов здоровья"
)
async def get_all_health(
    health_service: HealthHealth = Depends(get_health_service)
) -> List[HealthStatus]:
    health = health_service.get_health()
    return health

@router.post(
    "",
    responses={400: {"description": "Bad request"}},
    response_model=HealthStatus,
    description="Создание статуса здоровья"
)
async def create_health(
    health_service: HealthHealth = Depends(get_health_service)
) -> HealthStatus:
    health = health_service.create_health()
    return health