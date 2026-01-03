from datetime import datetime
from typing import List

from sqlalchemy import Column, String, BigInteger, DateTime, Boolean

from core.database.base_db_parametrs import Base, Session

from config import conf


class UsersTable():
    Session = Session


    class Users(Base):
        __tablename__ = "users"

        id = Column(BigInteger(), primary_key=True)
        topic_id = Column(BigInteger(), unique=True)
        lang = Column(String(), default='ru')
        first_name = Column(String())
        last_name = Column(String())
        username = Column(String())
        banned_bot = Column(Boolean(), default=False)
        last_active_date = Column(DateTime(), default=datetime.now)


        def readable_info(self) -> str:
            '''Читабельная инфа о пользователе'''
            return (
                f'Пользователь {self.id}\n'
                f'{self.first_name} {self.last_name} @{self.username}\n'
                f'Последняя активность: {self.last_active_date.strftime(conf.datetime_format())}\n'
                f'Забанил бота' if self.banned_bot else 'Не забанил бота'
            )


    # -------------------------
    # ---------- add ----------
    # -------------------------


    def add_user(
            self,
            id: int,
            first_name: str,
            last_name: str,
            username: str,
            topic_id: int,
            lang: str = 'ru'
    ) -> None:
        '''
        Добавляет топик

        :param id: id пользователя
        :param first_name: имя пользователя в тг
        :param last_name: фамилия пользователя в тг
        :param username: юзернейм пользователя
        :param topic_id: айди топика с пользователем
        :param lang: язык пользователя
        '''

        with self.Session() as s:
            topic = self.Users(
                id=id,
                first_name=first_name,
                last_name=last_name,
                username=username,
                topic_id=topic_id,
                lang=lang,
            )
            s.add(topic)
            s.commit()


    # -------------------------
    # ---------- edit ---------
    # -------------------------


    def edit_user_topic(self, user_id: int, topic_id: int) -> None:
        '''
        Изменение топика пользователя

        :param user_id: айди пользователя
        :param topic_id: новый айди топика
        '''
        with self.Session() as session:
            session.query(self.Users).filter(
                self.Users.id == int(user_id)
            ).update({
                self.Users.topic_id: topic_id
            })
            session.commit()


    def edit_user_banned(self, user_id: int, banned: bool = True) -> None:
        '''
        Изменение статуса пользователя забанил бота или нет

        :param user_id: айди пользователя
        :param banned: забанил пользователь ли бота
        '''
        with self.Session() as session:
            session.query(self.Users).filter(
                self.Users.id == user_id
            ).update({
                self.Users.banned_bot: banned
            })
            session.commit()


    def edit_user_language(self, user_id: int, lang: str = 'ru') -> None:
        '''
        Изменение языка пользователя

        :param user_id: айди пользователя
        :param lang: новый язык
        '''
        with self.Session() as session:
            session.query(self.Users).filter(
                self.Users.id == user_id
            ).update({
                self.Users.lang: lang
            })
            session.commit()


    # -------------------------
    # ---------- get ----------
    # -------------------------


    def get_user(
            self,
            id: int
    ) -> Users | None:
        '''
        Возвращает запись о пользователе из бд, либо нон

        :param id: id пользователя в тг
        '''

        with self.Session() as s:
            return s.query(self.Users).filter(
                self.Users.id == id
            ).first()


    def get_user_by_topic_id(
            self,
            topic_id: str
    ) -> Users | None:
        '''
        Возвращает запись о пользователе из бд, либо нон

        :param topic_id: id пользователя в тг
        '''

        with self.Session() as s:
            return s.query(self.Users).filter(
                self.Users.topic_id == topic_id,
                self.Users.topic_id != None
            ).first()


    def get_all_users(self) -> List[Users]:
        '''Данные всех пользователей'''
        with self.Session() as session:
            return session.query(self.Users).all()


    def get_users_for_mail(self) -> List[Users]:
        '''Список пользователей для рассылки'''
        with self.Session() as session:
            return session.query(self.Users).filter(
                self.Users.banned_bot == False
            ).all()


    # -------------------------
    # ---------- get ----------
    # -------------------------


    def delete_user(self, user_id: int) -> None:
        '''Удаление пользователя из бд'''
        with self.Session() as session:
            session.query(self.Users).filter(
                self.Users.id == user_id
            ).delete()
            session.commit()
