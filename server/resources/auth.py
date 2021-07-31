from flask import request, jsonify
from flask_jwt_extended import create_access_token
from database.models import User, Nominee
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from .mail import send_token_email
import datetime

from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
    InternalServerError, MovieAlreadyExistsError

class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.password=send_token_email(user)
            print(user.password)
            # user.password='password'
            user.hash_password()
            user.save()
            id = user.id
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                return {'error': 'Username or password invalid'}, 401

            role = str(user.role)
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=str(user.id), additional_claims={'role':int(role)}, expires_delta=expires)
            return {'token': access_token, 'role': role, 'id':str(user.id)}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError

class AddNomineeApi(Resource):
    @jwt_required()
    def post(self):
        claims = get_jwt()
        if int(claims['role']) == 2:
            try:
                body = request.get_json()
                nominee = Nominee(**body)
                nominee.save()
                id = nominee.id
                return {'id':str(id)}, 200
            except (FieldDoesNotExist, ValidationError):
                raise SchemaValidationError
            except NotUniqueError:
                raise MovieAlreadyExistsError
            except Exception as e:
                raise InternalServerError
        else:
            return jsonify(message='Administrator Priviledge required')
