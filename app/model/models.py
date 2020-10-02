from app import db
from datetime import datetime


class Users(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(6))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    product = db.relationship('Products', backref='user_product', lazy='dynamic')
    image = db.relationship('Images', backref='user_image', lazy='dynamic') 

    def __repr__(self):
        return f'<User {self.name}>'


class Products(db.Model):
    id_barang = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    stock = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Product {self.name}>'
    

class Images(db.Model):
    id_img = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)

    def __repr__(self):
        return f'<Image {self.id_img}>'
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id_user')) ## users.id merujuk pada class User > id

    def __repr__(self):
        return f'<Post {self.body}>'
