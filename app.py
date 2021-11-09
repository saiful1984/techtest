from flask import Flask
from flask_restful import Api, Resource, marshal_with, fields, reqparse, abort
import logging as logger
from flask_sqlalchemy import SQLAlchemy
logger.basicConfig(level="DEBUG")
flaskAppInstance = Flask(__name__)

flaskAppInstance.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
flaskAppInstance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flaskAppInstance.config['SQLALCHEMY_BINDS_ENGINE_OPTIONS'] = {
    'connect_args': {'pool_size': 20}
}

db = SQLAlchemy(flaskAppInstance)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    middleName = db.Column(db.String)
    lastName = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)


user_put_args = reqparse.RequestParser()
user_put_args.add_argument("firstName", type=str, help="First name is required", required=True)
user_put_args.add_argument("middleName", type=str, help="Middle name is not mandatory", required=False)
user_put_args.add_argument("lastName", type=str, help="Last name is required", required=True)
user_put_args.add_argument("age", type=int, help="Age of user is required", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("firstName", type=str, help="First name is required", required=False)
user_update_args.add_argument("middleName", type=str, help="Middle name is not mandatory", required=False)
user_update_args.add_argument("lastName", type=str, help="Last name is required", required=False)
user_update_args.add_argument("age", type=int, help="Age of user is required", required=False)


user_fields = {
    'id': fields.Integer,
    'firstName': fields.String,
    'middleName': fields.String,
    'lastName': fields.String,
    'age': fields.Integer
}


@flaskAppInstance.before_first_request
def create_tables():
    db.create_all()


class apiTasks(Resource):
    '''
    Contains functions that define the HTTP methods
    '''
    @marshal_with(user_fields)
    def get(self, id):
        '''
        Performs the READ function for CRUD operation
        '''
        logger.info("Inside get method")
        result = User.query.filter_by(id=id).first()
        if not result:
            abort(404, message="Could not find user with that id")
        return result

    @marshal_with(user_fields)
    def put(self, id):
        '''
        Performs the UPDATE function for CRUD operation
        '''
        logger.info("Inside put method")
        args = user_put_args.parse_args()
        result = User.query.filter_by(id=id).first()
        if result:
            abort(409, 'This id is already taken..')
        user_data = User(id=id,
                         firstName=args["firstName"],
                         middleName=args["middleName"],
                         lastName=args["lastName"],
                         age=args["age"]
                         )
        db.session.add(user_data)
        db.session.commit()
        return user_data, 200

    @marshal_with(user_fields)
    def patch(self, id):
        logger.info("Inside PATCH method")
        args = user_update_args.parse_args()
        result = User.query.filter_by(id=id).first()
        if not result:
            abort(404, message="user doesn't exist, cannot update")

        if args['firstName']:
            result.firstName = args['firstName']

        if args['middleName']:
            result.middleName = args['middleName']

        if args['lastName']:
            result.lastName = args['lastName']

        if args['age']:
            result.age = args['age']

        db.session.commit()
        return result

    def delete(self, id):
        '''
        Performs the DELETE function for rest api
        '''
        logger.info("Inside delete method")
        result = User.query.filter_by(id=id)
        if not result:
            abort(404, message="user doesn't exist, cannot delete")
        result.delete()
        db.session.commit()
        return "", 204


restServer = Api(flaskAppInstance)
restServer.add_resource(apiTasks, "/api/v1.0/apiTasks/<int:id>")

if __name__ == '__main__':
    logger.info("Starting the app")

    flaskAppInstance.run(
        host='localhost',
        port=8000,
        debug=True,
        use_reloader=True
    )
    # flaskAppInstance.run(debug=True)
