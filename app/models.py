from datetime import datetime

from app import db
from helper import cnpj_mask

class Vendor(db.Model):
    

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(),nullable = False, unique = False)
    cnpj = db.Column(db.String(),nullable = False, unique = True)
    city = db.Column(db.String(),nullable = True, unique = False)
    product = db.relationship('Product',backref = 'vendor',lazy=True)

    def __init__(self, name,cnpj,city=''):
        self.name = name
        self.cnpj = cnpj
        self.city = city

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'cnpj': cnpj_mask(self.cnpj),
            'city': self.city
        }

class Product(db.Model):
    

    id = db.Column(db.Integer,primary_key = True)
    code = db.Column(db.String,nullable = False, unique = True)
    name = db.Column(db.String(),nullable = False, unique = False)
    price = db.Column(db.Float(), nullable = False, unique = False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'),nullable=False)

    def __init__(self, code,name,vendor_id,price=0.00):
        self.name = name
        self.code = cnpj
        self.price = city
        self.vendor_id = city

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return{
            'id': self.id,
            'code': self.code,
            'name':self.name,
            'price': 'R${:20,.2f}'.format(self.price),
            'vendor_id': self.city
        }
class Errors(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    end_point = db.Column(db.String(),nullable = False, unique = False)
    error = db.Column(db.String(),nullable = False, unique = False)
    updated_at = db.Column(db.Date(), onupdate=datetime.now(),nullable=False)

    def __init__(self, end_point,error):
        self.end_point = end_point
        self.error = error
        self.updated_at = datetime.now()
    
    def serialize(self):
        return{
            'id': self.id,
            'end_point': self.end_point,
            'error':self.error,
            'updated_at':self.updated_at
        }
        