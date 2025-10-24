from slqlalchemy import Column, Integer, String
from sqlalchemy.orm import realationship

from ..database import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key = True, index=True)
    name = Column(String, uniqie=True, nullable = False, index = True)
    slug = Column(String, uniqie=True, nullable = False, index = True)

    products = realationship('Product', back_populates='category')

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
