from typing import List

from src.repositories.Healthcheck_rep import HealthRepository
from src.models.Healthcheck_mod import HealthStatus

class HealthHealth:
    def __init__(self, repository: HealthRepository) -> None:
        self.repository = repository

    def get_health(self) -> List[HealthStatus]:
        result = self.repository.get_health()
        return result

    def create_health(self) -> HealthStatus:
        result = self.repository.create_health()
        return result