from .vote import VotingApi, GetCategoryApi, GetLeadsApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(VotingApi, '/api/vote')
    api.add_resource(GetCategoryApi, '/api/category/<type>')
    api.add_resource(GetLeadsApi, '/api/leads')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')