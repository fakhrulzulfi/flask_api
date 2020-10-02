from app.model.models import Users

from app import response, app, db, bcrypt

from flask import request

from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, jwt_manager

import os

import datetime


def transform(user):
    arr = []

    arr.append({
        'id': user.id_user,
        'name': user.name,
        'email': user.email,
        'created_at':user.created_at,
        'role':user.role
    })

    return arr


def users_all():
    arr = []

    try:
        users = Users.query.all()

        for user in users:
            arr.append({
                'id': user.id_user,
                'name': user.name,
                'email': user.email,
                'created_at':user.created_at,
                'role':user.role
            })
        
        return response.sukses('', arr)
    
    except Exception as e:
        return response.gagal('user gagal ditampilkan!', f'Error : {type(e).__name__}, {e.args[0]}', 404)


def add_user(user, email, pwd, role='member'):
    hashedPw = bcrypt.generate_password_hash(pwd).decode('utf-8')
    
    try:
        addUser = Users(name=user, email=email, password=hashedPw, role=role)

        db.session.add(addUser)
        db.session.commit()

        return response.sukses('user berhasil ditambahkan', '')

    except Exception as e:
        db.session.rollback()

        return response.gagal('user gagal ditambahkan!', f'Error : {type(e).__name__}, {e.args[0]}', 400)


def del_user(id_user):
    try:
        delUser = Users.query.filter_by(id_user=id_user).first()
        
        db.session.delete(delUser)
        db.session.commit()

        return response.sukses('user berhasil dihapus', '')
    
    except Exception as e:
        return response.gagal('user gagal dihapus', f'Error : {type(e).__name__}, {e.args[0]}', 400)

@jwt_required
def upd_user(uname, pwd, email):
    token = get_jwt_identity()

    try:
        user = Users.query.filter_by(id_user=token['id']).first()
        hashedPw = bcrypt.generate_password_hash(pwd).decode('utf-8')
        user.password = hashedPw
        user.name = uname
        user.email = email

        db.session.commit()
        
        return response.sukses('user berhasil diupdate', '')
    
    except Exception as e:
        return response.gagal('user gagal diupdate', f'Error : {type(e).__name__}, {e.args[0]}', 404 )


@jwt_required
def protected(user_id):
    user_select = Users.query.filter_by(id_user=user_id).first()
    print(user_select.role)

    if user_select.role != 'admin':
        return '[!] admin only!'
    else:
        return 'halo admin!'

    return 'user not found'


def login(username, passwd):

    user_select = Users.query.filter_by(name=username).first()
    
    if user_select:
        if bcrypt.check_password_hash(user_select.password, passwd):
            
            expires = datetime.timedelta(days=1)
            expires_refresh = datetime.timedelta(days=1)

            access_token = create_access_token({'id':user_select.id_user, 'expires':datetime.datetime.utcnow()+expires}, fresh=True, expires_delta=expires) 
            refresh_token = create_refresh_token({'id':user_select.id_user, 'expires':datetime.datetime.utcnow()+expires_refresh}, expires_delta=expires_refresh)

            token = {
                'token': access_token,
                'refresh_token': refresh_token
            }

            return response.sukses('login berhasil!', token)
            
        else: 
            return response.gagal('password salah!', '', 401)
    else:
        return response.gagal(f'user tidak terdaftar', '', 404)


@jwt_required
def profile():
    token = get_jwt_identity()
    print(request.headers)
    try:
        users = Users.query.filter_by(id_user=token['id']).first()        
        data = transform(users) 

    except AttributeError as err_attr:
        return response.gagal(f'user dengan id={user_id} tidak ada!', f'Error : {type(err_attr).__name__}, {err_attr.args[0]}', 404)

    return response.sukses('user ditampilkan', data)
