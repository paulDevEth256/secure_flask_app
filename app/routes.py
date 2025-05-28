from flask import Blueprint, request, jsonify
from .models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .extensions import limiter

bp = Blueprint('api', __name__)

@bp.route('/register', methods=['POST'])
@limiter.limit("5/minute")
def register():
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return jsonify({"msg": "Missing username or password"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "User already exists"}), 400

    user = User(
        username=data['username'],
        password_hash=User.hash_password(data['password'])
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User registered"}), 201

@bp.route('/login', methods=['POST'])
@limiter.limit("5/minute")
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    if not user or not user.check_password(data.get('password')):
        return jsonify({"msg": "Bad credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)

@bp.route('/user', methods=['GET'])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(id=user.id, username=user.username)
