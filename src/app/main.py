import uvicorn

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.api.api import api_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router)

@app.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url='/docs')

if __name__ == '__main__':
    # only debug
    uvicorn.run(app, host="0.0.0.0", port=8080)
