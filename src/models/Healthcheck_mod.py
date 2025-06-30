from pydantic import BaseModel
from typing import Optional

class HealthStatus(BaseModel):
    status: bool

class HealthChecker:
    def __call__(self) -> bool:
        return True