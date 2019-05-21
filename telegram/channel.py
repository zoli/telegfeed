from .client import client
from telethon.tl.types import PeerChannel
from telethon.tl.functions.channels import GetFullChannelRequest

class Channel:
    def __init__(self, name):
        self.name = name
        self.channel = client.get_input_entity(self.name)
        self.full_channel = client(GetFullChannelRequest(self.channel))

        self.id = self.full_channel.full_chat.id
        self.about = self.full_channel.full_chat.about
        self.title = self.full_channel.chats[0].title
        self.date = self.full_channel.chats[0].date

    def get_posts(self, limit=10):
        posts = []
        for post in client.iter_messages(self.channel, limit=limit):
            posts.append(post)

        return posts
