from typing import List

from src.repositories.Healthcheck_rep import HealthRepository
from src.models.Healthcheck_mod import healthchecker

class HealthHealth:
    def __init__(self, repository: HealthRepository) -> None:
        self.repository = repository

    def get_health(self) -> List[healthchecker]:
        result = self.repository.get_health()
        return result

    def create_health(self) -> healthchecker:
        result = self.repository.create_health()
        return result