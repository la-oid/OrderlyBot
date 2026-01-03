from core.database import (
    orders,
    users
)
from core.database.base_db_parametrs import Base, engine


class DataBase(
    users.UsersTable,
    orders.OrdersTable
):
    '''
    Класс для работы с базой данных
    '''
    Base.metadata.create_all(engine, checkfirst=True)


db = DataBase()
