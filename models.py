from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(200), nullable=False)
    social_links = db.Column(db.String(200))
    projects = db.Column(db.String(200))

    def __repr__(self):
        return f'<Portfolio {self.name}>'
