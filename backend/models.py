from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    store = Column(Integer)
    dept = Column(Integer)
    message = Column(String)
    risk_score = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
