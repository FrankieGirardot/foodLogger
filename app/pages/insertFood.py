from flask import render_template, request
from app.resources.configuration import load_config, connect, insert
from app.resources.queries import insert_query


def insertfoodget() -> str:
    return render_template('add_food.html')


def insertfoodpost(pagerequest: request) -> str:
    config = load_config()
    connect(config)

    food = pagerequest.form['food']
    servingSize = pagerequest.form['servingsize']
    calories = pagerequest.form['calories']

    insertQueryString = insert_query(food, servingSize, calories)

    insert(config, insertQueryString)

    return render_template('add_food.html')

