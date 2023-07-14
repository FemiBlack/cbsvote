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
            user = User.objects.get(id=user_id)
            body = request.get_json()
            if body['category'] not in user.voted_for:
                vote = Vote(**body)
                vote.save()

                nominee = Nominee.objects(id=body['nominee_id'],category__name=body['category'])
                nominee.update_one(__raw__={'$inc': {'category.$.votes':1}},
                )

                user.update(push__voted_for=body['category'])
                user.save()
                id = vote.id
                return {'id':str(id)}, 200
                except (FieldDoesNotExist, ValidationError):
                    raise SchemaValidationError
                except NotUniqueError:
                    raise MovieAlreadyExistsError
                except Exception as e:
                    raise InternalServerError
            else:
                return { 'message':'Can\'t vote twice buddy!' }, 200

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
            'entrepreneurmale',
            'entrepreneurfemale',
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
