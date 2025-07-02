from services.healthcheck_services import HealthCheckServices
from models.healthcheck_models import HealthStatus

health_service = HealthCheckServices()

def get_health_service() -> HealthCheckServices:
    return health_service