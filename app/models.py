from pydantic import BaseModel

class InfoResponse(BaseModel):
    email: str
    current_datetime: str
    github_url: str