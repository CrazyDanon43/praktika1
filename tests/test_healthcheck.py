import pytest
from http import HTTPStatus
from httpx import AsyncClient
from models.healthcheck_models import HealthStatus


@pytest.mark.asyncio
async def test_healthcheck(async_client: AsyncClient):
    response = await async_client.get("/health/healthcheck")
    assert response.status_code == HTTPStatus.OK
    health_status = HealthStatus(status=response.json()["status"])
    assert health_status.status is True