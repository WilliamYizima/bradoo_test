def cnpj_without_mask(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('/', '')
    return cnpj


def cnpj_mask(cnpj):
    cnpj_clear = cnpj_without_mask(cnpj)
    return "%s.%s.%s/%s-%s" % (cnpj_clear[0:2], cnpj_clear[2:5],
                               cnpj_clear[5:8], 
                               cnpj_clear[8:12], 
                               cnpj_clear[12:14])
