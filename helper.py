from aiogram import Bot, Dispatcher
from config import Config
from apscheduler.schedulers.asyncio import AsyncIOScheduler


conf = Config()
bot = Bot(token=conf.get_token())
dp = Dispatcher()
scheduler = AsyncIOScheduler()
