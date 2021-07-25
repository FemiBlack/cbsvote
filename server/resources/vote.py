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
            vote.save()

            nominee = Nominee.objects.get(id=request.args['nominee_id'],category__names=request.args['category'])
            nominee.update(inc__category__S__vote=1)
            nominee.save()

            user = User.objects.get(id=user_id)
            user.update(push__voted_for=request.args['category'])
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
    def get(self, type):
        try:
            users = Nominee.objects.get(category=type).to_json()
            return Response(users, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception:
            raise InternalServerError

class GetLeadsApi(Resource):
    def get(self):
        # get largest per category
        cats = ['freshman',"poppy"]
        leads = []
        for cat in cats:
            nominee = Nominee.objects(category__name=cat).order_by('category_S_votes').first()         
            leads.append(nominee)
        return Response(leads, mimetype="application/json", status=200)
