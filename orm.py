import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import create_tables, Base, Publisher, Book, Shop, Stock, Sale



DSN = 'postgresql://postgres:aboba9752obama@localhost:5432/dbsqlalchemy'
engine = create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


with open('tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()





session.close()