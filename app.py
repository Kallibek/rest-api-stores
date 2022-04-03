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

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://emveicbdqgpuhb:471dc3d3eb6bf0fe4a75579d76e411a90403c679cf89a28df173b2f90c102fef@ec2-18-214-134-226.compute-1.amazonaws.com:5432/d2a0ku8vsbv2dm' #'sqlite:///data.db'
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