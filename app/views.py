#!.venv/bin/python
from flask import render_template

from app import app
from forms import LoginForm


@app.route('/')
def index():
    user = {'username': 'Sasha'}
    form = LoginForm()
    return render_template('index.html', user=user,
                            title='Secret', form=form)
