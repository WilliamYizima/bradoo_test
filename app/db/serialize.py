from flask_marshmallow import Marshmallow
from db.models import Vendor, Product, Errors

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class VendorSchema(ma.ModelSchema):
    class Meta:
        model = Vendor


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
        include_fk = True

class ErrorsSchema(ma.ModelSchema):
    class Meta:
        model = Errors
