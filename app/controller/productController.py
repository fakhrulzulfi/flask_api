from app.model.models import Users, Products

from app import app, db, response

from flask_jwt_extended import jwt_required


## POSTS
@jwt_required
def create_product(name, desc, price, category, stock, user_id):
    try:
        user_select = Users.query.get(user_id)
        product = Products(name=name, description=desc, 
                            price=price, category=category, 
                            stock=stock, user_product=user_select)
    
        db.session.add(product)
        db.session.commit()

        return response.sukses('product created', '')
    
    except Exception as e:
        db.session.rollback()
        return response.gagal(f'failed to add product!', f'Error : {type(e).__name__}, {e.args[0]}', '400')


def transform_product(products):
    arr = []
    
    for product in products:
        arr.append({
            'id_barang': product.id_barang,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'stock': product.stock,
            'id_user': product.user_id,
            'username': product.user_product.name,
            'posted_at': product.created_at
        })
    
    return arr


def show_all_product():
    try:
        products = Products.query.all()
        data = transform_product(products)

        return response.sukses('products loaded!', data)
        

    except Exception as e:
        return response.gagal('can\'t load products!', f'Error : {type(e).__name__}, {e.args[0]}', '400')
        Error : {type(e).__name__}

    
def show_product(id_user, p):
    user = Users.query.get(id_user)
    try:
        products = user.product.all()
    except Exception as e:
        return response.gagal('product is empty!', f'Error : {type(e).__name__}, {e.args[0]}', '400')
    data = transform_product(products)
    arr = []
    
    for product in data:
        arr.append(product)


    if p is None:
        return response.sukses('products reloaded!', data)
    
    else:
        try:
            return response.sukses('product reloaded!', arr[p-1])
        except Exception as e:
            return response.gagal('product not found!', f'Error : {type(e).__name__}, {e.args[0]}', '400')