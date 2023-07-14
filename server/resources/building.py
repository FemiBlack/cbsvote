from flask import Response, request
from database.models import Vote, Nominee, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
import json

from mongoengine.errors import FieldDoesNotExist, \
    NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, MovieAlreadyExistsError, \
    InternalServerError, UpdatingMovieError, DeletingMovieError, MovieNotExistsError

class VotingApi(Resource):
    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            vote = Vote(**body)
            nominee = Nominee.objects.get(id=vote.nominee_id)
            index=int(vote.index)
            vote.save()
            nominee.update({f'inc__likes__{index}':1})
            nominee.save()
            user = User.objects.get(id=user_id)
            user.update(push__voted_for=index)
            user.save()
            id = vote.id
            return {'id':str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise MovieAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class GetCategoryApi(Resource):
    def get(self, id):
        try:
            users = Nominee.objects.get(category=id).to_json()
            return Response(users, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception:
            raise InternalServerError

class GetLeadsApi(Resource):
    def get(self):
        # get largest per category
        leads = []
        for i in range(14):
            x = User.objects().order_by(f'like[{i}]')
            x= x[0]
            leads.append(x)
        return Response(leads, mimetype="application/json", status=200)
