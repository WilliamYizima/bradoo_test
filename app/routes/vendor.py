from flask import Blueprint, request, jsonify, render_template, current_app
from models import Vendor
from serialize import VendorSchema


vendor = Blueprint('vendor', __name__)

@vendor.route("/register",methods=['POST'])
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

@vendor.route('/<int:id_>',methods=['DELETE'])
def delete_vendor(id_):
    try:
            #TODO ddelete products before vendor
        Vendor.query.filter(Vendor.id == id_).delete()
        current_app.db.session.commit()
        return jsonify(f'Deletado {id_}'),200
    except Exception as e:
        return {'error':e},500

@vendor.route("/edit/<int:id_>",methods=['PUT'])
def edit_vendor(id_):
   
    try:
        vs = VendorSchema()
        query = Vendor.query.filter(Vendor.id == id_)
        query.update(request.json)
        current_app.db.session.commit()
        return vs.jsonify(query.first())

    except Exception as e:
        
        return(str(e))

