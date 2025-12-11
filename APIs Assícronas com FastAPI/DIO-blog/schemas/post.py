from datetime import datetime, UTC
from pydantic import BaseModel, Field

class PostIn(BaseModel):
    title: str
    date: datetime = Field(default_factory=lambda: datetime.now(UTC))
    published: bool = False
    author: str