# Bradoo - Python Developer

- Validate:
- [x]  functionality
- [x]  deployment
- [ ]  documentation
- [ ]  testing

- Requirements:

- [ ]  Instructions needed to run the project into the repository
- [x]  Deploy Heroku

- Application 01:

    - [ ]  Front end application that will allow listing, editing, creating and removal of vendors and products.
    ##### VENDOR
    - [x]  The vendor record need:
        - id(self generated, surrogate key)
        - name(required)
        - CNPJ(required, this value is unique )
        - City
    - List
        - [x] Listing of vendor records, should allow searching of the records by any of the fields or a combination of them all
        - [x] Button to allow removal of a single or group of vendor records
        - [x] Button to create a new vendor 
        - [x] Button to edit a vendor 
    - Edit
        - [x] Edit/create selection must include the required fields
        - [x] There must be a button to remove the record, if already existent 
        - [x] There must be a button to create/save the record
        - [x] The create/save button must validate if the required fields are filled.Upon successful create/save of record the user must be redirected to the vendor listing
        - [x] Upon successful create/save of record the user must be redirected to the vendor listing CNPJ value needs be a valid number according to the BR rules
    
    ##### Products
    - [x] From within the vendors record, yout should provide a list and record creation method and input form for the products of the vendor
    - [x] The product record need:
        - id(self generated, surrogate key) 
        - Name(required)
        - Code(required)
        - Price
    - [x] Validate fields
    - [x] The products records should only be changed/create/deleted upon the vendor create/save button (to exclude a vendor it is necessary to exclude a product)

- Application 02:
    - [ ]  REST API for the vendor model
    - [ ]  Endpoint needs to return a paginated list with the vendor's data.
    - [ ]  Optionally the vendors can be searched by name, CNPJ, ID or a combination of these fields
    - [ ] Need to implement these actions in your API:
        - Create a vendor
        - Read vendor's data
        - Update vendor's data
        - Delete vendor's data
    - [ ] Example:
        ```json
        {
        "name": // Name of the vendor,
        "CNPJ": // CNPJ number,
        "city": // City of the vendor,
        "products": [ {
        “Name”: //product name,
        “Code” : //product code,
        “Price” : //product price,
        }]
        }
        ```
    - [ ] Use the appropriated HTTP verbs for the CRUD action, example , POST, GET
    - [ ] When no data is found, you should return HTTP CODE 204 - No Content

- USE:
    - Python Flask or Django
    - ORM to interface with the database
    - Use Python >=3.5
    - PEP-8
    - Every text or code must be in English
    - Documentation:
        - [ ] Description
        - Installing setup and testing instructions
        - Docker solution for setup
        - Brief description of the work environment used to run this project
    - Provide API documentation (in English)
    - Variables, code and strings must be all in English
    - Relational database
    - Deploy and deliver your code
