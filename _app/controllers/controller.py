from _app.models.model import Item
from _app import db

def get_all():
    return Item.query.all()

def add(name):
    item = Item(name=name)
    db.session.add(item)
    db.session.commit()

def delete(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()

def update(name, item_id):
    item = Item.query.get(item_id)
    if item:
        item.name = name
        db.session.commit()
