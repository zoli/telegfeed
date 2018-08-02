from telethon import TelegramClient, sync
import json, datetime
import config

def date_format(message):
	if type(message) is datetime:
		return message.strftime("%Y-%m-%d %H:%M:%S")

client = TelegramClient('telegfeed',
	config.TELEGRAM['app_id'], config.TELEGRAM['api_hash']).start()

channel = client.get_input_entity('mostafamalekian')

msgs = []
for msg in client.iter_messages(channel, limit=10):
	msgs.append(msg.to_dict())

print(json.dumps(msgs, default=date_format))
