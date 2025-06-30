from typing import List
from fastapi import APIRouter, Depends

from src.depends import get_health_service
from src.models import Healthcheck_mod
from src.services import Healthcheck_serv

router = APIRouter(prefix="/HEALTH", tags=["HEALTH"])

@router.get(
    "",
    responses={400:{"desvription":"Bad request"}},
    response_model=List[Healthcheck_mod],
    description="Получение листинга всех статусов здоровья",
)
async def get_all_health(
        health_service: Healthcheck_serv = Depends(get_health_service),
) -> List[Healthcheck_mod]:
    health = health_service.get_health()
    return

@router.post(
    "",
    responses={400:{"description":"Bad request"}},
    response_model=Healthcheck_mod,
    description="Создание статуса здоровья"
)
async def get_all_health(
    health_service: Healthcheck_serv = Depends(get_health_service),
) -> Healthcheck_mod:
    health = health_service.create_health()
    return health