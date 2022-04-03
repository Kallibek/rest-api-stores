from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=False,
        #help="id is optional"
    )
    parser.add_argument('name',
        type=str,
        required=False,
        #help="name is optional"
    )
    parser.add_argument('address',
        type=str,
        required=False,
        #help="address is optional"
    )
    def get(self):
        data = Store.parser.parse_args()
        if store:=StoreModel.find_by_id(data['id']):
            return store.json()
        elif store:=StoreModel.find_by_name(data['name']):
            return store.json()
        else:
            return {'message': 'Store not found'}, 404

    def post(self):
        data = Store.parser.parse_args()
        # check if name is valid
        if data['name'] is None:
            return {'message':'name field is missing'},400
        # check if in db
        if store:=StoreModel.find_by_id(data['id']):
            return {'message': f"A store with id {data['id']}'already exists.",
                    'store': store.json()}, 400
        elif store:=StoreModel.find_by_name(data['name']):
            return {'message': f"A store with name {data['name']} already exists.",
                    'store': store.json()}, 400
        else:
            # create in db
            store = StoreModel(**data)
            try:
                store.save_to_db()
                return store.json(), 201
            except Exception as e:
                return {"message": str(e)}, 500
            
            
    def put(self):
        data = Store.parser.parse_args()
        if store:=StoreModel.find_by_id(data['id']):
            if data['name']:
                store.name=data['name']
            store.address=data['address']
            
        elif store:=StoreModel.find_by_name(data['name']):
            if data['id']:
                store.id=data['id']
            store.address=data['address']
        else:
            # create in db
            store = StoreModel(**data)
        try:
            store.save_to_db()
            return store.json(), 201
        except Exception as e:
            return {"message": str(e)}, 500

def delete(self):
        data = Store.parser.parse_args()
        if store:=StoreModel.find_by_name(data['name']):
            store.delete_from_db()
        elif store:=StoreModel.find_by_id(data['id']):
            store.delete_from_db()
        else:
            return {'message': 'Store not found by id or name'}

        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
