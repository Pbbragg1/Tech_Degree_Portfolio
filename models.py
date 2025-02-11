from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String)
    date = db.Column("Date", db.DateTime, default=datetime.datetime.now)
    description = db.Column("Description", db.String)
    skills = db.Column("Skills", db.String)
    github = db.Column("Github", db.String)

def __repr__(self):
    return f'''<Project (Title: {self.title}
    Date: {self.date}
    Description: {self.description}
    Skills: {self.skills}
    Link: {self.link})'''