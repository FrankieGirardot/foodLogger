from flask import Blueprint, render_template, request
from app.pages.insertFood import insertfoodpost, insertfoodget
from app.pages.seeFood import seeFoodGet

# Create a Blueprint object
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/add_food', methods=['GET', 'POST'])
def add_food():
    if request.method == 'POST':
        return insertfoodpost(request)
    elif request.method == 'GET':
        return insertfoodget()


@bp.route('/see_food')
def see_food():
    return seeFoodGet()


@bp.route('/about')
def about():
    return render_template('about.html')
