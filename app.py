import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ckejcbyhkyyelb:6805a7775c75e1003280cea9bf91b647055dd3872fb2913c3f123b504337fd26@ec2-3-225-213-67.compute-1.amazonaws.com:5432/d75j4qgk9h4rh9' #'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'kallibek'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store')
api.add_resource(Item, '/item')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')



if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)