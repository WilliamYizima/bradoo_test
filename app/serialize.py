from flask_marshmallow import Marshmallow
from models import Vendor, Product, Errors

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class VendorSchema(ma.ModelSchema):
    class Meta:
        model = Vendor


class ProductSchema(ma.Schema):
    class Meta:
        model = Product


class ErrorsSchema(ma.Schema):
    class Meta:
        model = Errors
