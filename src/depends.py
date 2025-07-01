from services.healthcheck_services import healthchecker
from src.services.healthcheck_services import healthstatus

health_service = healthstatus(healthchecker)

def get_health_service() -> healthchecker:
   return health_service
