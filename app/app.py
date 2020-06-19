import os
from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

app.config.from_object(os.environ['APP_SETTINGS'])
#TODO retirar abaixo
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://will:123456@localhost:5432/bradoo_test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from models import Vendor,Product,Errors
from helper import cnpj_without_mask

@app.route('/')
def list():
    #TODO alterar nome das variaǘeis

    try:
        vendor=Vendor.query.all()
        all_vendor = [e.serialize() for e in vendor]
        
        
        return render_template('list.html',
                                obj=all_vendor)
    except Exception as e:
        return(str(e))
    return render_template('list.html',obj = obj)

# @app.route('/register')
# def register():
#     
#     #TODO id no BD
#     
#     return render_template('vendor_form.html')
#TODO melhorar o sistema de rotas
@app.route("/registervendor",methods=['POST'])
def add_vendor():
    
    request_data = request.get_json()
    
    name = request_data['name']
    cnpj = request_data['cnpj']
    city = request_data['city']

    try:
        vendor=Vendor(
            name=name,
            cnpj=cnpj_without_mask(cnpj),
            city=city
        )
        db.session.add(vendor)
        db.session.commit()
        return redirect(url_for('list'))
    except Exception as e:
        return(str(e))
    return render_template("list.html")

@app.route("/registerproduct",methods=['POST'])
def add_product():
    if request.method == 'POST':
        name=request.form.get('name')
        cnpj=request.form.get('code')
        city=request.form.get('price')
        try:
            product=Product(
                name=name,
                cnpj=code,
                city=price
            )
            db.session.add(product)
            db.session.commit()
            return redirect(url_for('list'))
        except Exception as e:
            return(str(e))
    return render_template("list.html")

@app.route("/editvendor",methods=['POST'])
def edit_vendor():

    request_data = request.get_json()
    id_= request_data['id_vendor']
    name = request_data['name']
    cnpj = request_data['cnpj']
    city = request_data['city']
    
    try:
        vendor = Vendor.query.filter_by(id = id_).first()
        vendor.name = name
        vendor.cnpj = cnpj
        vendor.city = city
        
        db.session.commit()
        return redirect(url_for('list'))
    except Exception as e:
        
        return(str(e))
    return render_template("list.html")

@app.route('/get/<int:id_>')
def get_id(id_):
    try:
        vendor = Vendor.query.filter_by(id=id_).first()
        vendor_id =vendor.serialize()
        print(vendor_id)
        return render_template('list.html',
                                vendor_id = vendor_id)
    except Exception as e:
        return (str(e))

@app.route('/del/<int:id_>',methods=['DELETE'])
def delete_vendor(id_):
    try:
        #TODO ddelete products before vendor
        vendor=Vendor.query.filter_by(id=id_).delete()
        db.session.commit()
        return {'message':'deletado'}
    except Exception as e:
        return {'error':e}

@app.route('/del/combo',methods=['POST'])
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

@app.route('/get_cnj/<string:cnpj>')
def get_cnpj(cnpj):
    try:
        vendor_cnpj = {'cnpj':'CNPJ not found'}
        cnpj = cnpj_without_mask(cnpj)
        vendor=Vendor.query.filter_by(cnpj=cnpj).first()
        if(vendor):
            vendor_cnpj =(vendor.serialize())
        return vendor_cnpj 
    except Exception as e:
        error=Errors(
            end_point='/get_cnj/<cnpj>',
            error=str(e)
        )
        db.session.add(error)
        db.session.commit()
        return 'I have A Problem'

    
if __name__ == "__main__":
    app.run(port=5000, debug=True)