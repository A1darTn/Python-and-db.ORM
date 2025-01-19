import sqlalchemy as sq
# from sqlalchemy import ForeignKey, Column, String, Integer, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column("id", sq.Integer, primary_key=True)
    name = sq.Column("name", sq.String(length=40), unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Book(Base):
    __tabalename__ = "book"

    id = sq.Column("id", sq.Integer, primary_key=True)
    title = sq.Column("title", sq.String(length=40), nullable=False)
    id_publisher = sq.Column("id_publisher", sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    def __init__(self, id, title, id_publisher):
        self.id = id
        self.name = title 
        self.id_publisher = id_publisher


class Shop(Base):
    __tablename__ = "shop"
    
    id = sq.Column("id", sq.Integer, primary_key=True)
    name = sq.Column("name", sq.String(length=40), unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column("id", sq.Integer, primary_key=True)
    id_book = sq.Column("id_book", sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column("id_shop", sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column("count", sq.Integer, nullable=False)

    def __init__(self, id, id_book, id_shop, count):
        self.id = id
        self.id_book = id_book
        self.id_shop = id_shop
        self.count = count


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column("id", sq.Integer, primary_key=True)
    price = sq.Column("price", sq.Integer, nullable=False)
    date_sale = sq.Column("data_sale", sq.Date, nullable=False)
    id_stock = sq.Column("id_stock", sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column("count", sq.Integer, nullable=False)

    def __init__(self, id, price, data_sale, id_stock, count):
        self.id = id
        self.price = price
        self.date_sale = data_sale
        self.id_stock = id_stock
        self.count = count


def create_tables(engine):
    Base.metadata.create_all(engine)

