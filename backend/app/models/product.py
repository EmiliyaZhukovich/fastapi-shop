from slqlalchemy import Column, Integer, String, Text, Float, ForeighKey, DateTime
from sqlalchemy.orm import realationship
from datetime import datetime

from ..database import Base

class Product(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key = True, index=True)
    name = Column(String, nullable = False, index = True)
    description = Column(Text)
    price = Column(Float, nullable = False)
    category_id = Column(Integer, ForeighKey("categories.id"), nullable = False)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())

    category = realationship('Category', back_populates='products')

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price='{self.price}')>"
