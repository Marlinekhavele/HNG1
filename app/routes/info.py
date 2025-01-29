from fastapi import APIRouter, HTTPException
from datetime import datetime
import pytz
from ..models import InfoResponse
from ..core.settings import get_settings

router = APIRouter()

@router.get("/", response_model=InfoResponse)
async def get_info():
    """
    Get basic information including email, current datetime, and GitHub URL
    Returns:
        JSON: Information payload
    """
    try:
        settings = get_settings()
        current_time = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        return {
            "email": settings.email,
            "current_datetime": current_time,
            "github_url": settings.github_url
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))