from . import db

class User(db.Model):
    __tablename__ = 'user_profiles'
    
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.Text)
    date = db.Column(db.String(12))
    photo = db.Column(db.String(100))
    
    
    
    def __init__(self,firstname,lastname,gender,email,location,biography,date,photo):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.date = date
        self.photo = photo
        
    def __repr__(self):
        return '<User %r>' % (self.username)
    