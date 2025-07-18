from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def filmua():
    return render_template("filmua.html")