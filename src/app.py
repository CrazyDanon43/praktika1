from fastapi import FastAPI

from src.routing.Healthcheck_rout import router

app = FastAPI(openai_url="/core/openai.json", docs_url="/core/docs")

app.include_router(router)