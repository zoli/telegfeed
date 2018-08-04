from flask import Flask, jsonify
from telegram import get_posts
from werkzeug.contrib.atom import AtomFeed

app = Flask(__name__)

@app.route('/channel/<channel_id>')
def channel_feed(channel_id):
    feed = AtomFeed('۱۰ نوشته آخر کانال فلان', id='1')

    posts = get_posts(channel_id)
    for post in posts:
        if not post.edit_date:
            post.edit_date = post.date

        feed.add('test', content=post.message, id=post.id,
            updated=post.edit_date, published=post.date)

    return feed.get_response()
