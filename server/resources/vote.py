from flask import Response, request, jsonify
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
            
            data = request.get_json()
            nominee = Nominee.objects(id=data['nominee_id'],category__name=data['category'])
            # print(nominee)
            # nominee.update(inc__category__S__votes=1)
            nominee.update_one(__raw__={'$inc': {'category.$.votes':1}},
            )
            # nominee.save()

            user = User.objects.get(id=user_id)
            user.update(push__voted_for=data['category'])
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
            users = Nominee.objects(category__name=type).to_json()
            return Response(users, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception:
            raise InternalServerError

class GetUserVoteApi(Resource):
    @jwt_required()
    def get(self, id):
        try:
            users = User.objects(id=id).to_json()
            return Response(users, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception:
            raise InternalServerError

class GetLeadsApi(Resource):
    def get(self):
        # nominee = Nominee.objects(category__name="facemale").to_json()
        # get largest per category
        cats = [
            'fashionablemale',
            'fashionablefemale',
            'nextgenmale',
            'nextgenfemale',
            'entreprenuermale',
            'entreprenuerfemale',
            'facemale',
            'facefemale',
            'sociablemale',
            'sociablefemale',
            'sportspersonmale',
            'sportspersonfemale',
            'innovativemale',
            'innovativefemale',
        ]
        leads = []
        for cat in cats:
            print(cat)
            try:
                nominee = Nominee.objects(category__name=cat).order_by('category__S__votes').first().to_json()
                # print(json.loads(nominee))
                leads.append(nominee)
                print(json.dumps(leads))
            except AttributeError:
                continue
        return Response(json.dumps(leads), mimetype="application/json", status=200)
        # return jsonify(leads=leads)
