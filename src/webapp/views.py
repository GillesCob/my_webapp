from flask import render_template, Blueprint
from flask_login import current_user, login_required
from webapp.models import User

views = Blueprint("views", __name__)


@views.route('/')
def home_page():
    return render_template('home.html',user=current_user)

# ------------- CV ------------- #
@views.route('/cv-1')
def cv_1():
    return render_template('cv_1.html',user=current_user)

@views.route('/cv-2')
#@login_required
def cv_2():
    return render_template('cv_2.html',user=current_user)


# ------------- CSS ------------- #

@views.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html',user=current_user)

@views.route('/bootstrap_1')
def bootstrap_1():
    return render_template('bootstrap_1.html',user=current_user)

@views.route('/carousel')
def carousel():
    return render_template('carousel.html',user=current_user)

@views.route('/bootstrap_2')
def bootstrap_2():
    return render_template('bootstrap_2.html',user=current_user)




@views.route('/flexbox')
def flexbox():
    return render_template('flexbox.html',user=current_user)


# ------------- GITHUB ------------- #

@views.route('/github')
def github():
    return render_template('github.html',user=current_user)


# ------------- OUTILS ------------- #

@views.route('/outils_design')
def outils_design():
    return render_template('outils_design.html',user=current_user)

@views.route('/outils_api')
def outils_api():
    return render_template('outils_api.html',user=current_user)

@views.route('/outils_deploiement')
def outils_deploiement():
    return render_template('outils_deploiement.html',user=current_user)

@views.route('/outils_documentaire')
def outils_documentaire():
    return render_template('outils_documentaire.html',user=current_user)


# ------------- IDENTIFICATION ------------- #

@views.route('/login')
def login():
    return render_template('login.html',user=current_user)

@views.route('/sign-up')
def sign_up():
    return render_template('sign_up.html',user=current_user)

@views.route('/log-out')
def log_out():
    return render_template('log_out.html',user=current_user)