import sqlalchemy
from sqlalchemy import ForeignKey, Column, String, Integer, Date, DECIMAL
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Publisher(Base):
    __tablename__ = "publisher"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(length=40), unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Book(Base):
    __tablename__ = "book"

    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(length=40), nullable=False)
    id_publisher = Column("id_publisher", Integer, ForeignKey("publisher.id"))

    def __init__(self, id, title, id_publisher):
        self.id = id
        self.name = title 
        self.id_publisher = id_publisher


class Shop(Base):
    __tablename__ = "shop"
    
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(length=40), unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Stock(Base):
    __tablename__ = "stock"

    id = Column("id", Integer, primary_key=True)
    id_book = Column("id_book", Integer, ForeignKey("book.id"), nullable=False)
    id_shop = Column("id_shop", Integer, ForeignKey("shop.id"), nullable=False)
    count = Column("count", Integer, nullable=False)

    def __init__(self, id, id_book, id_shop, count):
        self.id = id
        self.id_book = id_book
        self.id_shop = id_shop
        self.count = count


class Sale(Base):
    __tablename__ = "sale"

    id = Column("id", Integer, primary_key=True)
    price = Column("price", DECIMAL, nullable=False)
    date_sale = Column("date_sale", Date, nullable=False)
    id_stock = Column("id_stock", Integer, ForeignKey("stock.id"), nullable=False)
    count = Column("count", Integer, nullable=False)

    def __init__(self, id, price, date_sale, id_stock, count):
        self.id = id
        self.price = price
        self.date_sale = date_sale
        self.id_stock = id_stock
        self.count = count


def create_tables(engine):
    Base.metadata.create_all(engine)

