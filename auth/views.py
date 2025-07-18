from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note  is too short', category='error')
        else:
            new_user = Note(data='note', user_id=current_user.id)
            db.session.add(new_user)
            db.session.commit()
            flash("Note added!", category='success')



    return render_template("home.html")