from fastapi import FastAPI

from routing.healthcheck_routing import router

app = FastAPI()

app.include_router(router)
