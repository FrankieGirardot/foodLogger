from tkinter.tix import Form
from flask import Blueprint, render_template, send_from_directory, request

# Create a Blueprint object
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')
