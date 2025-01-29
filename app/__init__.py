from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import info
from .core.settings import get_settings

def create_app() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title="HNG Stage 1",
        description="An API that returns basic user information",
        version="1.0.0"
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(info.router)

    return app