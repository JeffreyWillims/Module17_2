from site import USER_BASE

from backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from models import __init__models, user_models


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('tasks.id'))
    rating = Column(Float)
    is_active = Column(Boolean, default=True)

from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))
print(CreateTable(User.__table__))