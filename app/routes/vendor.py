from flask import Blueprint, request, jsonify,render_template,current_app
from models import Vendor
from helper import cnpj_without_mask
from serialize import VendorSchema
import json

vendor = Blueprint('vendor', __name__)


@vendor.route('/')
def list():
    try:
        

        vendor = Vendor.query.all()
        all_vendor = [e.serialize() for e in vendor]
        
        
        return render_template('list.html',
                                obj=all_vendor)
    except Exception as e:
        return(str(e))
    return render_template('list.html',obj = obj)

@vendor.route("/registervendor",methods=['POST'])

def add_vendor():
    vs = VendorSchema()
    vendor = vs.load(request.json)
    try:
        current_app.db.session.add(vendor)
        current_app.db.session.commit()
        return vs.jsonify(vendor), 200
    except Exception as e:
        print(str(e))
        return jsonify(content =  e), 500
    return render_template("list.html")
