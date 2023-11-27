from flask import Blueprint, request, flash, redirect, render_template, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, current_user, logout_user


#Je créé un objet "auth" accessible dans le module "__name__" et tout ça est stocké dans une variable "auth"
auth = Blueprint("auth", __name__)

#Page dédiée à l'inscription--------------------------------------------------------------------------------------------------------------------------------------------
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email") #Création de tous mes encadrés à remplir
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first() #l'email existe déjà ?
        username_exists = User.query.filter_by(username=username).first() #Le nom d'utilisateur existe déjà ?

        if email_exists: #Je rajoute toute une série de vérifications
            flash('Email is already in use.', category='danger')
        elif username_exists:
            flash('Username is already in use.', category='danger')     
        elif password1 != password2:
            flash('Password don\'t match!', category='danger')
        elif len(username) < 2:
            flash('Username is too short.', category='danger')
        elif len(password1) < 1:
            flash('Password is too short.', category='danger')
        elif len(email) < 4:
            flash("Email is invalid.", category='danger')
        
        else: #Je rajoute un nouvel utilisateur si tout est bon jusque là
            new_user = User(email=email, username=username, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit() #sauvegarde dans la BDD
            login_user(new_user, remember=True) #Je connecte mon nouvel utilisateur
            flash('User created!', category='success')
            return redirect(url_for('views.home_page'))
    return render_template("sign_up.html", user=current_user)



#Page dédiée à la connexion--------------------------------------------------------------------------------------------------------------------------------------------
@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first() #Je regarde ici si le mail existe, si oui il devient la variable "user"
        if user:
            if check_password_hash(user.password, password): #Je vérifie le hash du mdp
                flash("Logged in!", category='success')
                login_user(user, remember=True) #Création de la session persistante (True) pour mon user
                return redirect(url_for('views.home_page')) #si mdp ok, redirection vers home page
            else:
                flash('Password is incorrect.', category='danger')
        else:
            flash('Email does not exist.', category='danger')
    return render_template("login.html", user=current_user)


#Page dédiée à la déconnexion--------------------------------------------------------------------------------------------------------------------------------------------
@auth.route("/logout")
def logout():
    logout_user()
    flash("Logout successfull", category='success')
    return redirect(url_for("auth.login"))