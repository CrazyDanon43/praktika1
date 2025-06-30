from fastapi import FastAPI

from src.models.Healthcheck_mod import healthchecker
from src.routing import Healthcheck_rout

app = FastAPI(openai_url="/core/openai.json", docs_url="/core/docs")

app.include_router(Healthcheck_rout)