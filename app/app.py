import os
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Vendor

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/register')
def register():
    #TODO validar o cnpj
    #TODO id no BD
    #TODO CNPJ unique
    return render_template('vendor_form.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)