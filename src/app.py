from fastapi import FastAPI

from src.routing.healthcheck_routing import router

if __name__ == "__main__":
  app = FastAPI(openai_url="/core/openai.json", docs_url="/core/docs")

  app.include_router(router)
