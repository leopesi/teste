from flask import Flask, jsonify
from .genius import get_popularity_songs
import uuid
import redis

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.add_url_rule("/artist/<name>", 'artist', artist)
    db = redis.Redis('localhost')
    return app

def artist(name):
    dados = get_popularity_songs(name, max_songs=10)
    id = {"id": uuid.uuid4(), "artista": name}

    content = [
        {
            "title": dado.title,
        }
        for dado in dados
    ]
    return jsonify(id, content)

