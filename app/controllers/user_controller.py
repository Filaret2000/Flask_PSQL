from flask import Blueprint, request, jsonify
from services.user_service import UserService
from repositories.user_repository import UserRepository

user_blueprint = Blueprint('user_blueprint', __name__)

# Inject dependencies manually
user_repository = UserRepository()
user_service = UserService(user_repository)

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: User found
        schema:
          id: User
          properties:
            id:
              type: integer
            username:
              type: string
            email:
              type: string
      404:
        description: User not found
    """
    try:
        user = user_service.get_user(user_id)
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: CreateUser
          required:
            - username
            - email
          properties:
            username:
              type: string
            email:
              type: string
    responses:
      201:
        description: User created
      400:
        description: Missing fields
    """
    try:
        data = request.json
        user = user_service.create_user(data)
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
