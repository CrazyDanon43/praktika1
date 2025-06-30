from src.repositories.Healthcheck_rep import HealthRepository
from src.services.Healthcheck_serv import HealthHealth

health_repository = HealthRepository()

health_service = HealthHealth(HealthRepository)

def get_health_service() -> HealthHealth:
   return health_service