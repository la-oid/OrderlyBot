from typing import List

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from core.utils.models import UserOrderStatusesRow, ServerOrderStatusesRow


class GTables():
    def __init__(self):
        # Подсоединение к Google Таблицам
        scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive"
        ]

        credentials = ServiceAccountCredentials.from_json_keyfile_name("core/source/creds.json", scopes=scope)
        client = gspread.authorize(credentials)

        self.user_order_statuses = client.open_by_url(
            'https://docs.google.com/spreadsheets/d/1VRyB8EgNHG3BBTHyOsVLf2rRhjtHpRDDb5dVtU1c_ok/edit'
        ).worksheet('Лист1')

        self.server_order_statuses = client.open_by_url(
            'https://docs.google.com/spreadsheets/d/1sjCkNySGA5_oKC2YtnZbF4D0Qrl_mc3ExWftLHPal2c/edit'
        ).worksheet('Лист1')


    def get_user_order(self, id: str) -> UserOrderStatusesRow:
        '''Получение статуса заказа по запросу пользователя'''
        cell = self.user_order_statuses.find(id)
        if cell is None:
            return
        return UserOrderStatusesRow(*self.user_order_statuses.row_values(cell.row))


    def get_server_order(self, id: str) -> ServerOrderStatusesRow:
        '''Получение статуса заказа по запросу пользователя'''
        cell = self.server_order_statuses.find(id)
        if cell is None:
            return
        return ServerOrderStatusesRow(*self.server_order_statuses.row_values(cell.row))


    def get_server_orders(self) -> List[ServerOrderStatusesRow]:
        '''Получение всех заказов'''
        rows = self.server_order_statuses.get_all_values()
        orders = []
        for row in rows:
            orders.append(ServerOrderStatusesRow(*row))
        return orders



gt = GTables()
