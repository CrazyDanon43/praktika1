import pytest
from src.models.healthcheck_models import HealthStatus
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_healthcheck(async_client: AsyncClient):
    response = await async_client.get("/health/healthcheck")
    assert response.status_code == 200
    health_status = HealthStatus(**response.json())
    assert health_status.status is True
    assert response.json() == {"status": True}
