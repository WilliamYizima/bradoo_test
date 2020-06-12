from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

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