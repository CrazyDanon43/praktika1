from fastapi import FastAPI

from routing import router

app = FastAPI(openai_url="/core/openai.json", docs_url="/core/docs")

app.include_router(router)