from fastapi import FastAPI

from routing.healthcheck_routing import router

app = FastAPI(openapi_url="/core/openai.json",
              docs_url="/core/docs")

app.include_router(router)

