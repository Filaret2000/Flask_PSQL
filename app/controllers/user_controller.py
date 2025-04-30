from flask import Blueprint, request, jsonify
from dependency_injector.wiring import inject, Provide
from services.abstract.user_service_interface import UserServiceInterface
from containers import Container

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix="/users")

@user_blueprint.route('/', methods=['GET'])
@inject
def get_all_users(user_service: UserServiceInterface = Provide[Container.user_service]):
    """
    Get all users
    ---
    responses:
      200:
        description: List of all users
        schema:
          type: array
          items:
            $ref: '#/definitions/User'
      500:
        description: Server error
    """
    try:
        users = user_service.get_all_users()
        return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_blueprint.route('/<int:user_id>', methods=['GET'])
@inject
def get_user(user_id: int, user_service: UserServiceInterface = Provide[Container.user_service]):
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
        
@user_blueprint.route('/<int:user_id>', methods=['PUT'])
@inject
def update_user(user_id: int, user_service: UserServiceInterface = Provide[Container.user_service]):
    """
    Update a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          id: UpdateUser
          required:
            - username
            - email
          properties:
            username:
              type: string
            email:
              type: string
    responses:
      200:
        description: User updated
      400:
        description: Missing fields
      404:
        description: User not found
    """
    try:
        data = request.json
        user = user_service.update_user(user_id, data)
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 404
        
@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
@inject
def delete_user(user_id: int, user_service: UserServiceInterface = Provide[Container.user_service]):
    """
    Delete a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: User deleted
      404:
        description: User not found
    """
    try:
        user_service.delete_user(user_id)
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@user_blueprint.route('/', methods=['POST'])
@inject
def create_user(user_service: UserServiceInterface = Provide[Container.user_service]):
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
