from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_login import LoginManager

app = Flask(__name__)


### Configuration για τα Secret Key, WTF CSRF Secret Key, SQLAlchemy Database URL, 
app.config["SECRET_KEY"] = '0ed1cfcfa3cdd1a4f6cb59036e6730c6'
app.config['WTF_CSRF_SECRET_KEY'] = 'c0b0d6a094a1a1ac9afef765e07f2c80'

## Το όνομα του αρχείου της βάσης δεδομένων θα πρέπει να είναι 'flask_movies_database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_movies_database.db"




app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


### Αρχικοποίηση της Βάσης, και άλλων εργαλείων ###
### Δώστε τις σωστές τιμές παρακάτω ###

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = "login_page"
login_manager.login_message_category = "warning"
login_manager.login_message = "Παρακαλώ κάντε login για να δείτε αυτή τη σελίδα."


from flaskMoviesApp import routes



