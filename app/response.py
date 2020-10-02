from flask import jsonify, make_response

def sukses(message, data):
    resp = {
        'success': True,
        'message': message,
        'data': data 
    }
    return make_response(jsonify(resp)), 200

def gagal(message, data, error_code):
    resp = {
        'success': False,
        'message': message,
        'error_code': error_code,
        'data': data
    }
    return make_response(jsonify(resp)), 400