from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_URI

engine = create_engine(DB_URI)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    brand = Column(String(100))
    price = Column(Float)
    image = Column(String(255))
    description = Column(String(500))


def init_db():
    Base.metadata.create_all(bind=engine)