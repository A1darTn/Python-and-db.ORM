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


name_publisher = input()

result = session.query(Book, Shop, Sale).filter(Publisher.name == name_publisher).filter(Publisher.id == Book.id_publisher).filter(Book.id == Stock.id_book).filter(Shop.id == Stock.id_shop).filter(Stock.id == Sale.id_stock)
for i in result:
    print(f'{i[0]} | {i[1]} | {i[2]}')
else:
    print(f'Список окончен или данные были введены непраивльно')
session.close()