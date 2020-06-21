from flask import Blueprint, request, render_template,redirect
from models import Vendor


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


@page.route('/get/<int:id_>')
def get_id(id_):
    try:

        vendor = Vendor.query.filter_by(id=id_).first()
        vendor_id = vendor.serialize()
        return render_template('list.html',
                               vendor_id=vendor_id)
    except Exception as e:
        return (str(e))


@page.route('/del/combo', methods=['POST'])
def delete_combo():   
    try:
        vendor_list = request.get_json()
        for vendor_id in vendor_list['vendor_list']:
            vendor = Vendor.query.filter_by(id=vendor_id).delete()
            db.session.commit()
        return redirect(url_for('list'))

    except Exception as e:
        
        error=Errors(
            end_point='/del/combo',
            error=e
        )
        db.session.add(vendor)
        db.session.commit()
        return redirect(url_for('list'))