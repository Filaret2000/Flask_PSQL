import os
from flask import Flask
from config.db import db
from controllers.user_controller import user_blueprint
from flasgger import Swagger
from flask_migrate import Migrate
from containers import Container

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

swagger = Swagger(app, template={
    'swagger': '2.0',
    'info': {
        'title': 'User API',
        'version': '1.0'
    },
    'definitions': {
        'User': {
            'type': 'object',
            'properties': {
                'id': {'type': 'integer'},
                'username': {'type': 'string'},
                'email': {'type': 'string'}
            }
        },
        'CreateUser': {
            'type': 'object',
            'required': ['username', 'email'],
            'properties': {
                'username': {'type': 'string'},
                'email': {'type': 'string'}
            }
        },
        'UpdateUser': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string'},
                'email': {'type': 'string'}
            }
        }
    }
})

# Dependency Injection
container = Container()
container.wire(packages=["controllers"])
app.container = container  # so controllers can access it

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
