from src.services.healthcheck_services import HealthCheckServices

health_service = HealthCheckServices()


def get_health_service() -> HealthCheckServices:
    return health_service
