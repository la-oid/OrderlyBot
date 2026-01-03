from typing import List
from datetime import datetime
from sqlalchemy import Column, BigInteger, DateTime, String, Integer, Boolean, desc

from core.database.base_db_parametrs import Base, Session


class OrdersTable():
    Session = Session


    class Orders(Base):
        __tablename__ = "orders"

        order_id = Column(String(), primary_key=True)
        user_id = Column(BigInteger())
        last_update_date = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
        sended = Column(Boolean())
        rate = Column(Integer(), default=None)
        mark_asked = Column(Boolean(), default=False)


        def __str__(self) -> str:
            return (
                'Order('
                f'order_id={self.order_id}, '
                f'user_id={self.user_id}, '
                f'last_update_date={self.last_update_date}, '
                f'sended={self.sended}, '
                f'rate={self.rate})'
            )


    # -------------------------
    # ---------- add ----------
    # -------------------------


    def add_order(
            self,
            order_id: str,
            user_id: int,
            sended: bool = False,
            rate: int = None,
    ) -> None:
        '''
        Добавляет заказ

        :param order_id: id заказа
        :param user_id: id пользователя
        :param sended: Отправлено ли сообщению пользователю, о том, что заказ готов
        :param rate: Оценка заказа
        '''

        with self.Session() as s:
            order = self.Orders(
                order_id=order_id,
                user_id=user_id,
                sended=sended,
                rate=rate,
            )
            s.add(order)
            s.commit()


    # -------------------------
    # ---------- edit ---------
    # -------------------------


    def edit_order_user_id(self, order_id: str, user_id: int, sended: bool = False, rate: int = None, mark_asked: bool = False) -> None:
        '''
        Изменение владельца заказа

        :param order_id: айди заказа
        :param user_id: айди нового владельца
        '''
        with self.Session() as session:
            session.query(self.Orders).filter(
                self.Orders.order_id == order_id
            ).update({
                self.Orders.user_id: user_id,
                self.Orders.sended: sended,
                self.Orders.rate: rate,
                self.Orders.mark_asked: mark_asked
            })
            session.commit()


    def edit_order_sended(self, order_id: str, sended: bool = True) -> None:
        '''
        Изменение статуса отправки сообщения о том, что заказ готов

        :param order_id: айди заказа
        :param sended: отправлено или нет
        '''
        with self.Session() as session:
            session.query(self.Orders).filter(
                self.Orders.order_id == order_id
            ).update({
                self.Orders.sended: sended
            })
            session.commit()


    def edit_order_rate_asked(self, order_id: str, asked: bool = True) -> None:
        '''
        Изменение статуса отправки сообщения о том, что оценка запрошена

        :param order_id: айди заказа
        :param asked: отправлено или нет
        '''
        with self.Session() as session:
            session.query(self.Orders).filter(
                self.Orders.order_id == order_id
            ).update({
                self.Orders.mark_asked: asked
            })
            session.commit()


    def edit_order_rate(self, order_id: str, rate: int) -> None:
        '''
        Изменение оценки заказа

        :param order_id: айди заказа
        :param rate: оценка заказа
        '''
        with self.Session() as session:
            session.query(self.Orders).filter(
                self.Orders.order_id == order_id
            ).update({
                self.Orders.rate: rate
            })
            session.commit()


    # -------------------------
    # ---------- get ----------
    # -------------------------


    def get_order(
            self,
            order_id: str
    ) -> Orders | None:
        '''
        Возвращает запись о заказе из бд, либо нон

        :param order_id: id заказа
        '''

        with self.Session() as s:
            return s.query(self.Orders).filter(
                self.Orders.order_id == order_id
            ).first()


    def get_user_orders(
            self,
            user_id: int
    ) -> List[Orders]:
        '''
        Возвращает все заказы из бд в порядке убывания даты обновления(самый первый - самый новый)

        :param user_id: id пользователя
        '''

        with self.Session() as s:
            return s.query(self.Orders).filter(
                self.Orders.user_id == user_id
            ).order_by(
                desc(self.Orders.last_update_date)
            ).all()
