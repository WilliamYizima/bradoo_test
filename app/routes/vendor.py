from flask import Blueprint, request, jsonify, current_app
from db.models import Vendor
from db.serialize import VendorSchema
from helper.helper import cnpj_mask


vendor = Blueprint('vendor', __name__)


@vendor.route("/register", methods=['POST'])
def add_vendor():
    vs = VendorSchema()
    vendor = vs.load(request.json)
    try:
        current_app.db.session.add(vendor)
        current_app.db.session.commit()
        return vs.jsonify(vendor), 200
    except Exception as e:
        print(str(e))
        return jsonify(content=e), 500

@vendor.route('/<int:id_>', methods=['DELETE'])
def delete_vendor(id_):
    try:
        Vendor.query.filter(Vendor.id == id_).delete()
        current_app.db.session.commit()
        return jsonify(f'Deletado {id_}'), 200

    except Exception as e:
        return {'error': e}, 500

@vendor.route("/edit/<int:id_>", methods=['PUT'])
def edit_vendor(id_):

    try:
        vs = VendorSchema()
        query = Vendor.query.filter(Vendor.id == id_)
        query.update(request.json)
        current_app.db.session.commit()
        return vs.jsonify(query.first())

    except Exception as e:

        return(str(e))

@vendor.route('/get_cnj/<string:cnpj>')
def get_cnpj(cnpj):
    try:
        vendor_cnpj = {'cnpj':'CNPJ not found'}
        cnpj = cnpj_mask(cnpj)
        print(cnpj)
        vendor = Vendor.query.filter_by(cnpj=cnpj).first()
        if(vendor):
            vendor_cnpj =(vendor.serialize())
        return vendor_cnpj 
    except Exception as e:
        print(e)
        return 'I have A Problem'