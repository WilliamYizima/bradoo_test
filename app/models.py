from app import db


class Vendor(db.Model):
    __tablename__ = 'tb_vendor'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String())
    cnpj = db.Column(db.String())
    city = db.Column(db.String())

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