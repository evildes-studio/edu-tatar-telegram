
from aiogram import Bot, Dispatcher
from configparser import ConfigParser
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from edu_tatar_bot.main.filters.is_edu_account import IsEduAccount

config = ConfigParser()
config.read('config/config.ini', encoding="utf8")

bot = Bot(token=config['bot']['token'], parse_mode='html')

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.filters_factory.bind(IsEduAccount)
