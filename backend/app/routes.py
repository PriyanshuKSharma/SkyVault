from flask import Blueprint, request, jsonify, send_from_directory
from app.models import db, File, User
from flask import current_app as app
import hashlib
import os

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'Authorization' not in request.headers:
        return jsonify({'message': 'Authorization required'}), 401

    auth_token = request.headers['Authorization']
    if not validate_token(auth_token):
        return jsonify({'message': 'Invalid token'}), 401

    file = request.files['file']
    file_hash = hashlib.sha256(file.read()).hexdigest()
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    new_file = File(name=file.filename, hash=file_hash)
    db.session.add(new_file)
    db.session.commit()
    return jsonify({'message': 'File uploaded successfully', 'hash': file_hash})

@main.route('/files', methods=['GET'])
def get_files():
    if 'Authorization' not in request.headers:
        return jsonify({'message': 'Authorization required'}), 401

    auth_token = request.headers['Authorization']
    if not validate_token(auth_token):
        return jsonify({'message': 'Invalid token'}), 401

    files = File.query.all()
    return jsonify([{'id': file.id, 'name': file.name} for file in files])

@main.route('/files/<int:id>', methods=['GET'])
def download_file(id):
    if 'Authorization' not in request.headers:
        return jsonify({'message': 'Authorization required'}), 401

    auth_token = request.headers['Authorization']
    if not validate_token(auth_token):
        return jsonify({'message': 'Invalid token'}), 401

    file = File.query.get_or_404(id)
    return send_from_directory(app.config['UPLOAD_FOLDER'], file.name)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400
    
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login(): 
    data = request.get_json() 
    username = data['username'] 
    password = data['password'] 
    
    user = User.query.filter_by(username=username).first() 
    if not user or not user.check_password(password): 
        return jsonify({'message': 'Invalid credentials'}), 401 
    
    expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=1) 
    token = jwt.encode({'user_id': user.id, 'exp': expiry}, app.config['SECRET_KEY'], algorithm='HS256') 
    
    return jsonify({'token': token}), 200

def generate_token(user_id):
    from datetime import datetime, timedelta
    import jwt
    expiry = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode({'user_id': user_id, 'exp': expiry}, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def validate_token(token):
    import jwt
    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return User.query.get(decoded['user_id']) is not None
    except:
        return False
