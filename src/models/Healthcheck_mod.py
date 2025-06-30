from pydantic import BaseModel

class healthchecker(BaseModel):
    def __call__(self) -> bool:
        return True or False

class health(BaseModel):
    status: healthchecker