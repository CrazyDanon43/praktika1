from typing import List

from src.models import Healthcheck_mod

class HealthRepository:

  def get_health(self) -> List[Healthcheck_mod]:
      result = self.repository.get_health()
      return result

  def create_health(self) -> Healthcheck_mod:
      result = self.repository.create_health()
      return result