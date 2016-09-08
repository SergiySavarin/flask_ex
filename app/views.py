#!.venv/bin/python
# import ipdb

from flask import render_template
from flask import request
from flask import jsonify

from app import app
from app import db
from forms import LoginForm
from models import User
import ipdb

@app.route('/', methods=['GET', 'POST'])
def index():
    user = {'username': 'Sasha'}
    form = LoginForm()
    if request.method == 'POST':
        req_user = User(username=request.form['username'],
                        password=request.form['password'])
        db.session.add(req_user)
        db.session.commit()
    # ipdb.set_trace()
    if request.is_xhr:
        return jsonify({'message': 'Request received!'})
    return render_template('index.html', user=user,
                            title='Secret', form=form)
