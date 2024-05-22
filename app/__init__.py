from flask import Flask
from routes import bp
from config import load_config, connect, select
import os

app = Flask(__name__)

app.register_blueprint(bp)

if __name__ == '__main__':

    config = load_config()
    connect(config)
    select(config)
    print(config)

    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
