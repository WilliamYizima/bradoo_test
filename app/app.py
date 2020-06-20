import os

from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap
from models import configure as config_db
from serialize import configure as config_ma
from flask_migrate import Migrate, MigrateCommand
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# Bootstrap(app)

# app.config.from_object(os.environ['APP_SETTINGS'])
#TODO retirar abaixo
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://will:123456@localhost:5432/bradoo_test"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://will:123456@localhost:5432/bradoo_test"
    
    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from routes import vendor,page
    app.register_blueprint(page.page)
    app.register_blueprint(vendor.vendor,url_prefix='/vendor')

    return app


# # @app.route('/register')
# # def register():
# #     
# #     #TODO id no BD
# #     
# #     return render_template('vendor_form.html')
# #TODO melhorar o sistema de rotas

# @app.route("/registerproduct",methods=['POST'])
# def add_product():
#     if request.method == 'POST':
#         name=request.form.get('name')
#         cnpj=request.form.get('code')
#         city=request.form.get('price')
#         try:
#             product=Product(
#                 name=name,
#                 cnpj=code,
#                 city=price
#             )
#             db.session.add(product)
#             db.session.commit()
#             return redirect(url_for('list'))
#         except Exception as e:
#             return(str(e))
#     return render_template("list.html")

# 





# 

# @app.route('/get_cnj/<string:cnpj>')
# def get_cnpj(cnpj):
    # try:
    #     vendor_cnpj = {'cnpj':'CNPJ not found'}
    #     cnpj = cnpj_without_mask(cnpj)
    #     vendor=Vendor.query.filter_by(cnpj=cnpj).first()
    #     if(vendor):
    #         vendor_cnpj =(vendor.serialize())
    #     return vendor_cnpj 
    # except Exception as e:
    #     error=Errors(
    #         end_point='/get_cnj/<cnpj>',
    #         error=str(e)
    #     )
    #     db.session.add(error)
    #     db.session.commit()
    #     return 'I have A Problem'

    
if __name__ == "__main__":
    app.run(port=5000, debug=True)