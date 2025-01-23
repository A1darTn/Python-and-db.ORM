import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import create_tables, Base, Publisher, Book, Shop, Stock, Sale



DSN = 'postgresql://postgres:aboba9752obama@localhost:5432/dbsqlalchemy'
engine = create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


# publ_1 = Publisher(1,'Пушкин')
# publ_2 = Publisher(2, 'Чехов')
# publ_3 = Publisher(3, 'Толстой')

# session.add_all([publ_1, publ_2, publ_3])
# session.commit()

# book_1 = Book(1, 'Капитанская дочь', 1)
# book_2 = Book(2, 'Руслан и Людмида', 1)
# book_3 = Book(3, 'Война и Мир', 3)
# book_4 = Book(4, 'Вишневый сад', 2)

# session.add_all([book_1, book_2, book_3, book_4])
# session.commit()

# shop_1 = Shop(1, 'Буквоед')
# shop_2 = Shop(2, 'Книги и Книжечки')
# session.add_all([shop_1, shop_2])
# session.commit()

# stock_1 = Stock(1, 1, 1, 1)
# stock_2 = Stock(2, 2, 1, 1)
# stock_3 = Stock(3, 3, 2, 1)
# stock_4 = Stock(4, 4, 2, 1)

# session.add_all([stock_1, stock_2, stock_3,stock_4])
# session.commit()

# sale_1 = Sale(1, 300, '11.09.2021', 1, 1)
# sale_2 = Sale(2, 200, '11.09.2021', 2, 1)
# sale_3 = Sale(3, 100, '11.09.2021', 3, 1)
# sale_4 = Sale(4, 150, '11.09.2021', 4, 1)

# session.add_all([sale_1, sale_2, sale_3, sale_4])
# session.commit()


def get_shop(publisher_identifier: str):
    if publisher_identifier.isdigit():
        publisher_id = int(publisher_identifier)
        publisher = session.query(Publisher).filter_by(id = publisher_id).first()
    else:
        publisher_name = publisher_identifier
        publisher = session.query(Publisher).filter_by(name = publisher_name).first()

    if publisher:
        results = session.query(
            Book.title,
            Shop.name,
            Sale.price,
            Sale.date_sale
        ).join(Stock, Stock.id_book == Book.id) \
        .join(Shop, Stock.id_shop == Shop.id)   \
        .join(Sale, Sale.id_stock == Stock.id)  \
        .filter(Book.id_publisher == publisher.id).all()
        
        for title, shop_name, price, date_sale in results:
            print(f"{title: <40} | {shop_name: <10} | {price: <8} | {date_sale}")
    else:
        print('Издатель не найден')
        
session.close()

if __name__ == "__main__":
    name_publisher = input()
    get_shop(name_publisher)