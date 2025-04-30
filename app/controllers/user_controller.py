from flask import Blueprint, request, jsonify
from flasgger import swag_from
from dependency_injector.wiring import inject, Provide
from services.abstract.user_service_interface import UserServiceInterface
from containers import Container
from models.DTOs import UserDTO

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix="/users")

@user_blueprint.route('/', methods=['GET'])
@inject
def get_all_users(user_service: UserServiceInterface = Provide[Container.user_service]):
    """
    Get all users
    ---
    tags:
      - Users
    summary: Get all users
    description: Retrieve a list of all users
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
        users_dto = user_service.get_all_users()
        return jsonify([UserDTO.to_dict(user_dto) for user_dto in users_dto]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_blueprint.route('/<int:user_id>', methods=['GET'])
@inject
def get_user(user_id: int, user_service: UserServiceInterface = Provide[Container.user_service]):
    """
    Get a user by ID
    ---
    tags:
      - Users
    summary: Get a user by ID
    description: Retrieve a specific user by their ID
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user to retrieve
    responses:
      200:
        description: User found
        schema:
          $ref: '#/definitions/User'
      404:
        description: User not found
    """
    try:
        user_dto = user_service.get_user(user_id)
        return jsonify(UserDTO.to_dict(user_dto)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@user_blueprint.route('/', methods=['POST'])
@inject
def create_user(user_service: UserServiceInterface = Provide[Container.user_service]):
    """
    Create a new user
    ---
    tags:
      - Users
    summary: Create a new user
    description: Add a new user to the system
    parameters:
      - name: body
        in: body
        required: true
        description: User information
        schema:
          $ref: '#/definitions/CreateUser'
    responses:
      201:
        description: User created
        schema:
          $ref: '#/definitions/User'
      400:
        description: Missing fields
      500:
        description: Server error
    """
    try:
        data = request.json
        user_dto = user_service.create_user(data)
        return jsonify(UserDTO.to_dict(user_dto)), 201
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_blueprint.route('/<int:user_id>', methods=['PUT'])
@inject
def update_user(user_id: int, user_service: UserServiceInterface = Provide[Container.user_service]):
    """
    Update a user
    ---
    tags:
      - Users
    summary: Update a user
    description: Update an existing user's information
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user to update
      - name: body
        in: body
        required: true
        description: Updated user information
        schema:
          $ref: '#/definitions/UpdateUser'
    responses:
      200:
        description: User updated
        schema:
          $ref: '#/definitions/User'
      400:
        description: Missing fields
      404:
        description: User not found
    """
    try:
        data = request.json
        user_dto = user_service.update_user(user_id, data)
        return jsonify(UserDTO.to_dict(user_dto)), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 404
        
@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
@inject
def delete_user(user_id: int, user_service: UserServiceInterface = Provide[Container.user_service]):
    """
    Delete a user
    ---
    tags:
      - Users
    summary: Delete a user
    description: Remove a user from the system
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user to delete
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
