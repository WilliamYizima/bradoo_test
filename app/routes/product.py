#TODO IMPLANTAR

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