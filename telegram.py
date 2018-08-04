from telethon import TelegramClient
import config

client = TelegramClient('telegfeed',
	config.TELEGRAM['app_id'], config.TELEGRAM['api_hash']).start()

def get_posts(channel_id, limit=10):
    channel = client.get_input_entity(channel_id)

    posts = []
    for post in client.iter_messages(channel, limit=limit):
        posts.append(post)

    return posts
