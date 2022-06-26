from flask import current_app
from datetime import datetime
from flaskFile import db, loginManager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@loginManager.user_loader
def loadUser(userId):
    return User.query.get(int(userId))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def getResetToken(self, expiresSec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expiresSec)
        return s.dumps({'userId': self.id}).decode('utf-8')

    @staticmethod
    def verifyToken(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            userId = s.loads(token)['userId']
        except:
            return None
        return User.query.get(userId)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    sku_code = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(20), nullable=False)
    mrp = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    shipping_cost = db.Column(db.Integer, nullable=False)
    bulk_pricing = db.Column(db.Integer, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_1 = db.Column(db.String(40), nullable=False)
    image_2 = db.Column(db.String(40), nullable=False)
    image_3 = db.Column(db.String(40), nullable=False)
    image_4 = db.Column(db.String(40), nullable=False)

    
    def __repr__(self):
        return f"UserRide('{self.userId}','{self.name}', '{self.id}')"
