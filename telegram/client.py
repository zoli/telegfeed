from telethon import TelegramClient
from . import config

client = TelegramClient('telegfeed',
    config.TELEGRAM['app_id'], config.TELEGRAM['api_hash'])
client.start()
