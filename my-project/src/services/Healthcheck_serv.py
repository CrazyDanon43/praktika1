from typing import List

from src.repositories import Healthcheck_rep
from src.models import Healthcheck_mod

class HealthHealth:
    def __init__(self, repository: Healthcheck_rep) -> None:
        self.repository = repository

    def get_health(self) -> List[Healthcheck_mod]:
        result = self.repository.get_health()
        return result

    def create_health(self) -> Healthcheck_mod:
        result = self.repository.create_health()
        return result