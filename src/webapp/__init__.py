from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path


#Je créé l'objet 'db", instance de la classe SQLAlchemy
db = SQLAlchemy()
DB_NAME = "database.db"


#1 - Je créé l'app, lignes de codes non modifiables-----------------------------------------------------------
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    

#2 - Je m'occupe des Blueprint--------------------------------------------------------------------------------
    #depuis la feuille "views" j'importe la variable views (qui contient le blueprint)
    from .views import views
    #Idem avec auth
    from .auth import auth
    #J'enregistre ces Blueprint dans mon app
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    
    
#3 - Création de la base de données en appelant la fonction "create_database"
    from .models import User
    create_database(app)
    
#4 - On implémente l'identification des utilisateurs (login)
    login_manager = LoginManager()
    #Ci-dessous la route vers laquelle sont renvoyés les utilisateurs non identifiés
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    #fonction appelée quand j'utilise "login_user"
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
#J'ai créé l'app, j'ai déclaré les blueprint, j'ai créé la BDD, j'ai implémenté la gestion de login (pas encore).
# Je peux donc faire un return app afin de pouvoir appeler mon objet app
    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created database!")