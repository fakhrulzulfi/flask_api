from app.model.models import Users, Images

from app import db, response, app

import os

import random

import string


def chgName(nameFile):

    get_ext = nameFile.split('.')

    numchar = string.ascii_letters + string.digits
    changeName = []

    for i in range(1,20):
        temp = random.choice(numchar)
        changeName.append(temp)

    values = ''.join(str(x) for x in changeName) +'.'+ get_ext[1]
    return values

def valid_ext(nameFile):
    get_ext = nameFile.split('.')[::-1]

    if ('.'+get_ext[0]) not in app.config['UPLOAD_EXTENSIONS']:
        return False
    else: 
        return True


def add_image(user_id, files):
    file_name = files.filename
    if file_name == '':
        return response.gagal('failed', 'null file', 404)

    else:
        
        try:
            user_select = Users.query.get(user_id)
        
            path = os.path.join(app.config['UPLOAD_FOLDER'], chgName(files.filename))
            
            if valid_ext(path) is True:
                image = Images(image=path, user_image=user_select)

                files.save(path)

                db.session.add(image)     # add to database

                db.session.commit()
                return response.sukses('berhasil upload', '')

            else:
                return response.gagal('ekstensi harus .jpg .jpeg .png', '', 400)
        
        except Exception as e:
            return response.gagal('failed', f'Error : {type(e).__name__}, {e.args[0]}', '400')

    

def transform(images):
    arr = []

    for img in images:
        arr.append({
            'id_image':img.id_img,
            'path':img.image,
            'username':img.user_image.name
        })

    return arr

def show_images():
        images = Images.query.all()
        data = transform(images)
        
        return response.sukses('success', data)