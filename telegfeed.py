from flask import Flask, jsonify
from telegram import generate_channel_feed

app = Flask(__name__, static_url_path='./')

@app.route('/channel/<channel_id>')
def channel_feed(channel_id):
    return jsonify(generate_channel_feed(channel_id))
