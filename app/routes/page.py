from flask import Blueprint, request, render_template, redirect, url_for, jsonify, current_app
from db.models import Vendor, Product, db
from db.models import Product
from db.serialize import ProductSchema
import json

page = Blueprint('page', __name__)


@page.route('/')
def list():
    try:
        vendor = Vendor.query.all()
        all_vendor = [e.serialize() for e in vendor]

        return render_template('list.html',
                               obj=all_vendor)
    except Exception as e:
        return(str(e))
    return render_template('list.html')


@page.route('/<int:id_>')
def get_id(id_):
    try:

        vendor = Vendor.query.filter_by(id=id_).first()
        vendor_id = vendor.serialize()

        product = Product.query.filter_by(vendor_id=id_)
        all_product = [e.serialize() for e in product]

        return render_template('list.html',
                               vendor_id=vendor_id,
                               product=all_product)
    except Exception as e:
        return (str(e))


@page.route('/del/combo', methods=['POST'])
def delete_combo():
    try:
        vendor_list = request.get_json()
        for vendor_id in vendor_list['vendor_list']:
            Vendor.query.filter_by(id=vendor_id).delete()
            db.session.commit()
        return {'delete':'succes'}, 200

    except Exception as e:

        error = Errors(
            end_point='/del/combo',
            error=e
        )
        db.session.add(error)
        db.session.commit()
        return jsonify({'delete':'I have a problem'}), 500



