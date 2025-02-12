from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String())
    date = db.Column("Date",db.DateTime, default=datetime.datetime.now)
    desc = db.Column("Description", db.Text)
    skills = db.Column("Skills", db.Text)
    github = db.Column("Github", db.Text)

def __repr__(self):
    return f'''<Project (Title: {self.title}
    Date: {self.date}
    Description: {self.desc}
    Skills: {self.skills}
    Github: {self.github})>'''