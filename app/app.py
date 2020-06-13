import os
from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

app.config.from_object(os.environ['APP_SETTINGS'])
#TODO retirar abaixo
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://will:123456@localhost:5432/bradoo_test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from models import Vendor,Product

@app.route('/list')
def list():
    #TODO alterar nome das variaǘeis
    obj = [{
            "id": 123, 
            "First": "leo",
            "Last": "Avelino",
            "Handle": "@fat"
        },
        {
            "id": 132131, 
            "First": "asfsafsf",
            "Last": "Avelino",
            "Handle": "@fat"
        },]

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
#     #TODO validar o cnpj
#     #TODO id no BD
#     #TODO CNPJ unique
      #TODO Tratamento para mascara CNPJ
#     return render_template('vendor_form.html')
#TODO melhorar o sistema de rotas
@app.route("/registervendor",methods=['POST'])
def add_vendor():
    name=request.form.get('name')
    cnpj=request.form.get('cnpj')
    city=request.form.get('city')
    try:
        vendor=Vendor(
            name=name,
            cnpj=cnpj,
            city=city
        )
        db.session.add(vendor)
        db.session.commit()
        return redirect(url_for('list'))
    except Exception as e:
        return(str(e))
    return render_template("list.html")

@app.route("/registerproduct",methods=['GET', 'POST'])
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
            return "Vendor added. book id={}".format(product.id)
        except Exception as e:
            return(str(e))
    return render_template("product_form.html")


@app.route('/get/<id_>')
def get_id(id_):
    try:
        product=Product.query.filter_by(id=id_).first()
        product_id =(product.serialize())
        

        return render_template('detail.html',
                                product = product_id)
    except Exception as e:
        return (str(e))


if __name__ == "__main__":
    app.run(port=5000, debug=True)