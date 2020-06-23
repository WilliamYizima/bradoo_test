async function delete_product(id) {

    myElement = document.querySelector(`tr[data-id="${id}"]`)
    myElement.remove()

    let response = await fetch(`product/${id}`, {
      method: 'DELETE',
    });
  }

  function editar_product(objeto) {
    var b = document.querySelector("#createProduct");
    document.getElementById("editProduct").action = "/product/edit/"+objeto.id;
    document.getElementById('new-nameProduct').value = objeto.name;
    document.getElementById('new-codeProduct').value = objeto.code;
    document.getElementById('new-priceProduct').value = objeto.price;
    document.getElementById('idProduct').value = objeto.id;
    document.getElementById('idProductVendor').value = objeto.vendor_id;
    b.removeAttribute("disabled");
  }
