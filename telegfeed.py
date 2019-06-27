from flask import Flask, url_for, render_template
from telegram.channel import Channel
from werkzeug.contrib.atom import AtomFeed

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/<name>')
# def channel(name):
#     channel = Channel(name)

#     posts = channel.get_posts()

#     return render_template('channel.html', posts=posts)

@app.route('/<name>/feed')
def channel_feed(name):
    channel = Channel(name)

    feed = AtomFeed('نوشته‌های اخیر '+channel.title, title_type='html',
        url='https://t.me/'+channel.name, id=channel.id, updated=channel.date,
        feed_url=url_for('channel_feed', name=channel.name),
        subtitle=channel.about, subtitle_type='html',
        generator=('telegfeed', None, '1.0.0'))

    posts = channel.get_posts()
    for post in posts:
        if not post.edit_date:
            post.edit_date = post.date

        feed.add(post.message[0:75], title_type='html', id=post.id,
            url='https://t.me/'+channel.name+'/'+str(post.id),
            content=post.message, content_type='html',
            updated=post.edit_date, published=post.date)

    return feed.get_response()
