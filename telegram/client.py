from telethon import TelegramClient
from . import config, util

if config.PROXY['addr']:
    client = TelegramClient('telegfeed', config.TELEGRAM['app_id'],
        config.TELEGRAM['api_hash'], proxy=util.get_proxy(config.PROXY))
else:
    client = TelegramClient('telegfeed', config.TELEGRAM['app_id'],
        config.TELEGRAM['api_hash'])

client.start()
