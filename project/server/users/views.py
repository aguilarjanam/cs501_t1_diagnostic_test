# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User
from project.server.auth.views import *
import json

userlist_blueprint = Blueprint('users', __name__)


class UserListAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):
    	responseObject = {
    		'status': 'success',
    		'message': 'Request successful but please send an HTTP POST request to register the user.'
    	}
    	return make_response(jsonify(responseObject)), 201
        
    def post(self):
        post_data = request.get_json(); print(request)
        users = User.query.all()
        d = []
        for u in users: 
            d.append(u.email)
        return make_response(jsonify(d))


# define the API resources
userlist_view = UserListAPI.as_view('userlist_api')
