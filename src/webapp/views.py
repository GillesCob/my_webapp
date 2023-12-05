from flask import render_template, Blueprint
from flask_login import current_user, login_required
from webapp.models import User

views = Blueprint("views", __name__)


@views.route('/')
def home_page():
    return render_template('home.html',user=current_user)

@views.route('/cv-1')
def cv_1():
    return render_template('cv_1.html',user=current_user)

@views.route('/cv-2')
#@login_required
def cv_2():
    return render_template('cv_2.html',user=current_user)

@views.route('/flexbox')
def flexbox():
    return render_template('flexbox.html',user=current_user)

@views.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html',user=current_user)

@views.route('/login')
def login():
    return render_template('login.html',user=current_user)

@views.route('/sign-up')
def sign_up():
    return render_template('sign_up.html',user=current_user)

@views.route('/log-out')
def log_out():
    return render_template('log_out.html',user=current_user)