from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class Entry(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    content: str
    summary: str
    mood_tag: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "content": "Today was a productive day. I finished my project and felt accomplished.",
                "summary": "A productive day marked by project completion and feelings of accomplishment.",
                "mood_tag": "accomplished",
                "created_at": "2024-03-20T12:00:00Z"
            }
        } 