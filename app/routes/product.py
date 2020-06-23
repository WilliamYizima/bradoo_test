# TODO IMPLANTAR
from flask import Blueprint, request, jsonify, current_app, render_template,redirect,url_for
from db.models import Product
from db.serialize import ProductSchema
import json

product = Blueprint('product',__name__)


@product.route('/<int:id_>', methods=['DELETE'])
def delete_product(id_):
    try:
        Product.query.filter(Product.id == id_).delete()
        current_app.db.session.commit()
        return jsonify(f'Deletado {id_}'), 200
    except Exception as e:
        return {'error': str(e)}, 500

@product.route("/edit/<int:id_>", methods=['POST'])
def edit_product(id_):

    try:    
        price = request.form.get('price').replace('R$','').strip()
        print(price)
        if (price==''):
            price = 0
        form_product = {'code':request.form.get('code'),
                        'name':request.form.get('name'),
                        'price':float(price),
                        'vendor_id':int(request.form.get('vendor_id'))
                        }
        print(form_product)
        ps = ProductSchema()
        query = Product.query.filter(Product.id == id_)
        query.update(form_product)
        current_app.db.session.commit()
        return redirect(url_for('page.get_id', id_=form_product['vendor_id']))

    except Exception as e:

        return(str(e))

@product.route('/register', methods=['POST'])
def add_product():
    
    vendor_id = int(request.form.get('vendor_id'))
    price = request.form.get('price')
    if (price==''):
        price = 0
    form_product = {'code':request.form.get('code'),
                    'name':request.form.get('name'),
                    'price':float(price),
                    'vendor_id':int(request.form.get('vendor_id'))
                    }
    ps = ProductSchema()
    print(form_product)
    product = ps.load(form_product)
    try:
        current_app.db.session.add(product)
        current_app.db.session.commit()
        return redirect(url_for('page.get_id', id_=vendor_id))
    except Exception as e:
        print(str(e))
        return redirect(url_for('page.get_id', id_=vendor_id))