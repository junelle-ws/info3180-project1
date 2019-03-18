from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"

app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://qyfqdbptrtjpak:e67a378c7cc188952475ac126515515a048458245a904f8abc82284d842a0828@ec2-75-101-133-29.compute-1.amazonaws.com:5432/d7o5rfvftlau80"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
