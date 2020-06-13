from app import db


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
            'cnpj': self.cnpj,
            'city': self.city
        }

class Product(db.Model):
    

    id = db.Column(db.Integer,primary_key = True)
    code = db.Column(db.Integer,autoincrement=True,nullable = False, unique = False)
    name = db.Column(db.String(),nullable = False, unique = False)
    price = db.Column(db.Float(), nullable = False, unique = False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'),nullable=False)