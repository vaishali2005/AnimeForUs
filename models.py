#Install Packages
from flask import Flask,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager
from datetime import datetime

#create the object of SQLAlchemy
db = SQLAlchemy()

#create the object of login manager to manage the login
login = LoginManager()

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique = True,nullable = False)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(250))
    profile_pic = db.Column(db.String(100),default='default.jpg')
    join_date = db.Column(db.DateTime,default=datetime.utcnow)
    
    # convert password into hashing
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
        
    #check password when user log's in
    def check_password(self,password): 
        c= check_password_hash(self.password_hash,password)
        print(c)
        return c
    
#find user it call back for reloading a user from session
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

    

class  WatchHistory(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    anime_id = db.Column(db.Integer,nullable=False,unique=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)  
    anime_name = db.Column(db.String(200),nullable=False)
    img_url = db.Column(db.String(500),nullable=False)
    anime_type = db.Column(db.String(50),nullable=False)
    # FOREIGN KEY (user_id) REFERENCES users(id)
    episode = db.Column(db.Integer,default = 1)
    watch_time = db.Column(db.Integer,default=0)
    
class FollowingAnime(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    anime_id = db.Column(db.Integer,nullable=False,unique=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    anime_name = db.Column(db.String(200),nullable=False)
    img_url = db.Column(db.String(500),nullable=False)
    episode = db.Column(db.Integer,default=1)
    
class AnimeComments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    anime_id = db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    username = db.Column(db.String(50),nullable=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    comment = db.Column(db.String(500))
    img_url = db.Column(db.String(500),nullable=False)
    