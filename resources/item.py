from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="Name cannot be blank"
    )
    parser.add_argument('description',
        type=str,
        required=False
    )
    parser.add_argument('price',
        type=float,
        required=False,
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store id."
    )

    @jwt_required()
    def get(self):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name_and_store(data['name'],data['store_id'])
        if item:
            return item.json()
        return {'message': f"{data['name']} not found in the store with id {data['store_id']}"}, 404

    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()
        if ItemModel.find_by_name_and_store(data['name'],data['store_id']):
            return {'message': f"{data['name']} already exists in the store with id {data['store_id']}"}, 400

        item = ItemModel(**data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name_and_store(data['name'],data['store_id'])
        if item:
            item.delete_from_db()
        return {'message': f"{data['name']} deleted from the store with id {data['store_id']}"}

    @jwt_required()
    def put(self):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name_and_store(data['name'],data['store_id'])

        if item is None:
            item = ItemModel(**data)
        else:
            item.price = data['price']
            item.description = data['description']
        try:
            item.save_to_db()
            return item.json()
        except Exception as e:
            return {"message":str(e)}
        


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}