from flask import Flask
from config import Config
from .site.routes import site
from.authentication.routes import auth
from .models import db as root_db, login_manager, ma, User
from flask_migrate import Migrate
from flask_login import LoginManager
#flask CORS import - CROSS ORIGIN RESOURCE SHARING-FUTURE PROOFING
#our react app so it can make api calls to this flask app

from flask_cors import CORS
app=Flask(__name__)
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)
root_db.init_app(app)
migrate = Migrate(app,root_db)
ma.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'


CORS(app)












# @app.route("/")
# def hello_world():
#     return "<p>hello,world!</p>"
