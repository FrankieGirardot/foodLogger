from flask import render_template
from app.resources.configuration import load_config, connect, select


def seeFoodGet():
    config = load_config()
    connect(config)
    select(config)
    print(config)

    return render_template('see_food.html')