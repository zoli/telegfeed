from flask import Flask, jsonify
from telegram import generate_channel_feed

app = Flask(__name__)

@app.route('/channel/<channel_id>')
def channel_feed(channel_id):
    return jsonify(generate_channel_feed(channel_id))
