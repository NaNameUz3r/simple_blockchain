from fastapi import FastAPI
from api.routes.main import router


def init() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application


app = init()
