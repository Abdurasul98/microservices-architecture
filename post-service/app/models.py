from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    content = Column(String(1000))
    user_id = Column(Integer)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))