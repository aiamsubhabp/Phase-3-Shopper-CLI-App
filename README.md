# Shopper CLI App
## CLI Description 
- This project features a command line interface (CLI), which is an interactive script that prompts the user and performs operations based on the user input.
- This project includes two models, the Manufacturer model and the Product model.  
    - There exists a one to many relationship between the two models; the manufacturer is the one, and the products are the many. In other words one manufacturer can produce many products, but each product can only be associated with one manufacturer. For instance, Apple produces many products such as iPhones, Airpods, etc.; however, iPhones and Airpods can only be produced by Apple. 
- Through this app, users are able to:
    - list all manufacturers and products
    - find manufacturers/products in the database,
    - create new manufacturers/products
    - update existing manufacturers/products
    - delete manufacturers/products
    - list all products made by a user specified manufacturer
    
## Installation
- To install, user must have Python 3 and pip installed.
    1. Clone this repository to your local machine and navigate to its directory.
    2. Run `pipenv install`. 
    3. After install, run `pipenv shell` to enter the local environment.
    4. Navigate to the `/lib` directory and run `python seed.py` to populate database with mock data.
    5. Finally inside of the `/lib` directory, run `python cli.py` to start using the app.

## Manufacturer Model
- Manufacturer class has the following attribues: id, name, and industry, with name and industry being properties
- The methods inside of the Manufacturer class are described below:
    - `create_table()`: Creates a new table to persist the attributes of Manufacturer instances.
    - `drop_table()`: Drops (deletes) the table taht persists the Manufacturer instances.
    - `save()`: Inserts a new row with the name and industry values of the current Manufacturer instance. Updates object id attribute using the primary key (PK) value of the new row. Saves the object in the local dictionary using table row's PK as the dictionary key.
    - `create()`: Initializes a new Manufacturer instance and saves the object to the database.
    - `update()`: Updates the table row corresponding to the current Manufacturer instance.
    - `delete()`: Deletes the table row corresponding to the current Manufacturer instance. Deletes the dictionary entry, and reassigns the id attribute.
    - `instance_from_db()`: Returns a Manufacturer object having the attribute values from the table row.
    - `get_all()`: Returns a list containing a Manufacturer object per row in the table.
    - `find_by_id()`: Returns a Manufacturer object corresponding to the table row matching the specified PK.
    - `find_by_name()`: Returns a Manufacturer object corresponding to the first table row matching the specified name. 
    - `products()`: Returns a list of products associated with the current manufacturer.

## Product Model
- The Product class has the following attributes: name, product_type, manufacturer_id, and id, with the name, product_type, and manufacturer_id being properties.
- The methods included in this class are the same as described above, just this time pertaining to the creation, deletion, and editing of Products.

## Roadmap
- add MSRPs to each product so that shoppers can compare prices
- add option for user to go back a step if needed
- update to have more visual appeal

## References
- PyFiglet: A library for rendering ASCII art fonts.