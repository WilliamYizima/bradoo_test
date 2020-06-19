var b = document.querySelector("#createVendor");

function register_vendor(id,name,cnpj,city) {
    var req_json = JSON.stringify({
      "name": name,
      "cnpj": cnpj,
      "city": city,
      "id_vendor":id
    });
    if (id == '') {
        console.log('novo registro')
      var xmlhttp = new XMLHttpRequest();
      xmlhttp.open("POST", "/registervendor");
      xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
      xmlhttp.send(req_json);
    } else {
        req_json.id_vendor = id;
      var xmlhttp = new XMLHttpRequest();
      xmlhttp.open("POST", "/editvendor");
      xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
      xmlhttp.send(req_json);
    }

    new_vendor();
    $('#vendorModal').modal('hide');
    window.location.reload();
  }

  function validation_form() {
    var name = document.querySelector('#new-nameVendor').value;
    var cnpj = document.querySelector('#new-cnpjVendor').value;
    var city = document.querySelector('#new-cityVendor').value;
    var id = document.querySelector('#id-Vendor').value;
    if(name != ''  && cnpj != '' ){
        register_vendor(id,name,cnpj,city);
    }else{
        document.getElementById("invalid-name").innerHTML = "Invalid name";
        b.setAttribute("disabled", "disabled");
    }

  }

  function input_name_validation(){
    document.getElementById("invalid-name").innerHTML = "";
    b.removeAttribute("disabled");
  }

  function new_vendor() {
    document.getElementById('new-nameVendor').value = '';
    document.getElementById('new-cnpjVendor').value = '';
    document.getElementById('new-cityVendor').value = '';
    document.getElementById('id-Vendor').value = '';
  }

  function editar(objeto) {
    document.getElementById('new-nameVendor').value = objeto.name;
    document.getElementById('new-cnpjVendor').value = objeto.cnpj;
    document.getElementById('new-cityVendor').value = objeto.city;
    document.getElementById('id-Vendor').value = objeto.id;
    b.removeAttribute("disabled");
  }

  async function excluir(id) {

    myElement = document.querySelector(`tr[data-id="${id}"]`)
    myElement.remove()

    let response = await fetch(`http://127.0.0.1:5000/del/${id}`, {
      method: 'DELETE',
    });
  }

  function checkbox_delete() {

    var textinputs = document.querySelectorAll('input[type=checkbox]');
    var vendor_checked = [].filter.call(textinputs, function (el) { return el.checked });
    var vendor_list = [];
    for (i = 0; i < vendor_checked.length; i++) { vendor_list.push(vendor_checked[i].attributes.value.textContent) };
    var req_json = JSON.stringify({ "vendor_list": vendor_list });
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/del/combo");
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.send(req_json);
    location.reload();
  }