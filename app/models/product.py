from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    Numeric,
    ForeignKey
)
from sqlalchemy.orm import relationship

from app.db.database import Base


class Image(Base):
    __tablename__ = "images"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer,ForeignKey("products.id"),nullable=False)
    url = Column(String(length=250),nullable=False)
    
    product = relationship("Product", back_populates="images")
    


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=250),nullable=False)
    description = Column(Text)
    price = Column(Numeric,nullable=False)
    
    images = relationship("Image", back_populates="product")