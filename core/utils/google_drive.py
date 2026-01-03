import traceback

from loguru import logger

from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io

from config import conf


class GDrive():
    def __init__(self):
        # Подсоединение к Google Таблицам
        scope = [
            "https://www.googleapis.com/auth/drive"
        ]

        credentials = service_account.Credentials.from_service_account_file("core/source/creds.json", scopes=scope)
        self.service = build('drive', 'v3', credentials=credentials)


    def find_photo_id(self, order_id: str) -> str | None:
        '''Возвращает id и имя первого файла в формате {'id': 'asdfaf', 'name': 'asd;flk'}, если есть, если нет - None'''
        try:
            return self.service.files().list(
                fields="files(id, name)",
                q=f"'{conf.folder_id()}' in parents and (name = '{order_id}.png' or name = '{order_id}.jpg')"
            ).execute()['files'][0]
        except Exception as e:
            text = f'Ошибка {e} при поиске фотографии по заказу {order_id}\nСтек:\n'
            text += traceback.format_exc()
            logger.error(text)


    def download_file(self, file_id: str, file_name: str) -> None:
        '''Скачивает файл с айдишником'''
        request = self.service.files().get_media(fileId=file_id)
        filename = 'core/source/drive_photos/' + file_name
        fh = io.FileIO(filename, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            logger.info(f"Download {file_name} %d%%." % int(status.progress() * 100))


gd = GDrive()
