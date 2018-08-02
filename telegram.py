from telethon import TelegramClient, sync
import json
import config, utils

client = TelegramClient('telegfeed',
	config.TELEGRAM['app_id'], config.TELEGRAM['api_hash']).start()

def generate_channel_feed(channel_id, limit=10):
    channel = client.get_input_entity(channel_id)

    msgs = []
    for msg in client.iter_messages(channel, limit=10):
        msgs.append(msg.to_dict())

    return msgs
