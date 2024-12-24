from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

class Task(Base) :
    __tablename__ = 'tasks'
    __table_args__ ={'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority  = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer , ForeignKey('users.id'), index=True, nullable=False)
    slug = Column(String, unique=True, index=True)
    user = relationship('User', back_populates='tasks')



