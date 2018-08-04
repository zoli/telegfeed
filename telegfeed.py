from flask import Flask, url_for
from telegram.channel import Channel
from werkzeug.contrib.atom import AtomFeed

app = Flask(__name__)

@app.route('/channel/<username>')
def channel_feed(username):
    channel = Channel(username)

    feed = AtomFeed('نوشته‌های اخیر '+channel.title, title_type='html',
        url='https://t.me/'+channel.username, id=channel.id, updated=channel.date,
        feed_url=url_for('channel_feed', username=channel.username),
        subtitle=channel.about, subtitle_type='html',
        generator=('telegfeed', None, '1.0.0'))

    posts = channel.get_posts()
    for post in posts:
        if not post.edit_date:
            post.edit_date = post.date

        feed.add(post.message[0:75], title_type='html', id=post.id,
            url='https://t.me/'+channel.username+'/'+str(post.id),
            content=post.message, content_type='html',
            updated=post.edit_date, published=post.date)

    return feed.get_response()
