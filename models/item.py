from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(256),default='No info')
    price = db.Column(db.Float(precision=2),default=0.0)

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price,store_id,description=None):
        self.name = name
        self.price = price
        self.store_id = store_id
        self.description= description
    def json(self):
        return {
            'name': self.name,
            'description':self.description, 
            'price': self.price,
            'store_id': self.store_id
            }

    @classmethod
    def find_by_name_and_store(cls, name,store_id):
        return cls.query.filter_by(name=name).filter_by(store_id=store_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
