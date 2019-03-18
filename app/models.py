from . import db

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(255))
    location = db.Column(db.String(255))
    description = db.Column(db.String(255))
    gender =db.Column(db.String(255))
    photo = db.Column(db.String(255))
    date = db.Column(db.String(255))

    def __init__(self, first_name, last_name, email, location, description, gender, photo,  date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.description= description
        self.gender = gender
        self.photo = photo 
        self.date = date

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.email)