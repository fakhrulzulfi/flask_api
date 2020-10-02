from flask import request

from app import app, response

from app.controller import userController, productController, imageController

import os

import io


@app.route('/users/', methods=['GET'])
def show_users():
    return userController.users_all()


@app.route('/users/profile/', methods=['GET'])
def filter_user():
    return userController.profile()


@app.route('/users/', methods=['POST'])
def add_user():
    data = request.get_json()
    
    try:
        name = data['username']
        email = data['email']
        pwd = data['password']
        

    except Exception as e:
        return response.gagal('user gagal ditambah', f'Error : {type(e).__name__} in {e.args[0]}', 400)

    return userController.add_user(name, email, pwd)


@app.route('/users/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):
    return userController.del_user(id_user)


@app.route('/users/profile/settings/', methods=['PUT'])
def update_user():
    try:
        data = request.get_json()

        username = data['username']
        password = data['password']
        email = data['email']

    except Exception as e:
        return response.gagal('user gagal diupdate', f'Error : {type(e).__name__} in {e.args[0]}', 404)
        
    return userController.upd_user(username, password, email)


@app.route('/login/')
def login():
    try:
        data = request.get_json()
        
        username = data['username']
        password = data['password']

    except Exception as e:
        return response.gagal('login gagal', f'Error : {type(e).__name__} in {e.args[0]}', 404)

    return userController.login(username, password)


@app.route('/products/', methods=['GET'])
def show_all_product():
    return productController.show_all_product()


@app.route('/products/<int:id_user>/', methods=['POST'])
def create_product(id_user):
    try:
        data = request.get_json()
        
        name= data['name']
        description= data['description']
        price= data['price']
        stock= data['stock']
        category= data['category']

    except Exception as e:
        return response.gagal('produk gagal ditambahkan', f'Error : {type(e).__name__} in {e.args[0]}', 404)

    return productController.create_product(name, description, price, category, stock, id_user) 


@app.route('/products/<int:id_user>/', methods=['GET'])
def show_product(id_user):
    product_id = request.args.get('p')

    if product_id is None:
        return productController.show_product(id_user, product_id)
    
    else:
        return productController.show_product(id_user, int(product_id))


@app.route('/uploads/<int:id_user>/', methods=['POST'])
def upload_file(id_user):

    if 'file' not in request.files:
        return 'file not found'
    
    files = request.files['file']
    
    return imageController.add_image(id_user, files)


@app.route('/show-images/')
def show_image():
    return imageController.show_images()


@app.route('/protected')
def protected():
    user_id = request.args.get('id')
    return userController.protected(user_id)