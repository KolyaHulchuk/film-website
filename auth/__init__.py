from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Kolya:Kolya6_333@localhost/mydb" # Шлях до бази даних
    db.init_app(app) # Ініціалізуємо SQLAlchemy з нашим додатком

    from .views import views
    from .auth import auth
    
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    from .models import User, Note # Імпортуємо моделі бази даних 

    create_database(app)

    login_manager = LoginManager() # відповідає за менеджмент авторизації:Перевіряє, чи користувач залогінений.
    login_manager.login_view = 'auth.login' #  куди перенаправляти користувача, якщо він неавторизований.
    login_manager.init_app(app)  # Цей рядок підключає LoginManager до Flask-додатку.

    @login_manager.user_loader # Це функція, яку Flask-Login буде викликати, щоб завантажити користувача по його id, коли сесія активна
    def load_user(id):
        return User.query.get(int(id)) # завантажуватиме користувача по айді
    

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print("Created Tables in PostgreSQL")
