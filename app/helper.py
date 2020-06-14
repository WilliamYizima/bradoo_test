def cnpj_without_mask(cnpj):
    cnpj = cnpj.replace('.','')
    cnpj = cnpj.replace('-','')
    cnpj = cnpj.replace('/','')
    return cnpj

def cnpj_mask(cnpj):
    return "%s.%s.%s/%s-%s" % ( cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14] )