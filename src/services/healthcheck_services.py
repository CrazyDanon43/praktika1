from pydantic import BaseModel


class healthstatus(BaseModel):
    status: bool

class healthchecker:
    def __call__(self) -> bool:
        return True
