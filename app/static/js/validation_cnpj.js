var b = document.querySelector("#createVendor");

function somenteNumeros(e) {
    var charCode = e.charCode ? e.charCode : e.keyCode;
    if (charCode != 8 && charCode != 9) {
        if (charCode < 48 || charCode > 57) {
            return false;
        }
    }
}
//Validate CNPJ
function cnpj(s) {
    let cnpj = s.replace(/[^\d]+/g, '')

    // Valida a quantidade de caracteres
    if (cnpj.length !== 14)
        return false

    // Elimina inválidos com todos os caracteres iguais
    if (/^(\d)\1+$/.test(cnpj))
        return false

    // Cáculo de validação
    let t = cnpj.length - 2,
        d = cnpj.substring(t),
        d1 = parseInt(d.charAt(0)),
        d2 = parseInt(d.charAt(1)),
        calc = x => {
            let n = cnpj.substring(0, x),
                y = x - 7,
                s = 0,
                r = 0

            for (let i = x; i >= 1; i--) {
                s += n.charAt(x - i) * y--;
                if (y < 2)
                    y = 9
            }

            r = 11 - s % 11
            return r > 9 ? 0 : r
        }

    return calc(t) === d1 && calc(t + 1) === d2
}

function maskCNPJ(n) {
    nMask = n.replace(/\D/g, '')
        .replace(/^(\d{2})(\d{3})?(\d{3})?(\d{4})?(\d{2})?/, "$1.$2.$3/$4-$5")
    return nMask
}

function validate_cnpj_bd(e) {

    var cnj_capturado = document.getElementById(e).value
    document.getElementById(e).value = maskCNPJ(cnj_capturado)
    var id_ = document.querySelector("#id-Vendor").value;

    if (cnpj(cnj_capturado) == false) {
        document.getElementById("validateCNJ").innerHTML = "Invalid CNPJ"
        b.setAttribute("disabled", "disabled");

    }
    else {
        n = cnj_capturado.replace('.', '').replace('-', '').replace('/', '').replace('.', '');

        fetch("/vendor/get_cnj/" + n)
            .then(response => response.json().then(data => {

                console.log(data)
                if (data['cnpj'] != 'CNPJ not found') {
                    document.getElementById("validateCNJ").innerHTML = "CNPJ already exists"
                    if (id_ == "") {
                        b.setAttribute("disabled", "disabled");
                    } else { b.removeAttribute("disabled"); }
                } else {
                    document.getElementById("validateCNJ").innerHTML = "CNPJ Accepted"
                    b.removeAttribute("disabled");

                }
            }
            )
            )
            .catch(function (err) {
                console.error('Failed retrieving information', err);
            });
    }
    }