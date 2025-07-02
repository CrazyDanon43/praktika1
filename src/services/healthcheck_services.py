from models.healthcheck_models import HealthStatus

class HealthCheckServices:
    def get_health(self) -> HealthStatus:
        return HealthStatus(status=True)