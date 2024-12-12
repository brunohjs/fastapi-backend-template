import fastapi

import src.api.router as router
from src.config import logging
from src.config.manager import settings


# Configura o logging ao iniciar a aplicação
logging.setup_logging()


app = fastapi.FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    debug=settings.DEBUG,
    root_path=settings.API_PREFIX,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    description=settings.DESCRIPTION
)

# Inclui o roteador principal
app.include_router(router.api_router)


@app.get("/")
async def root():
    return {"message": "Bem-vindo à API!"}
