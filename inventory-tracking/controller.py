import sqlalchemy as db
from flask import jsonify
from sqlalchemy.orm import declarative_base
from model import Item, Shipment
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update, delete

Base = declarative_base()
engine = db.create_engine('sqlite:///shopify.sqlite', echo=True)
connection = engine.connect()
metadata = db.MetaData()


def list_items():
    Session = sessionmaker(bind=engine)
    session = Session()
    items = session.query(Item).all()
    print(items)
    json_list = []
    for item in items:
        json_object = {}
        json_object['item_id'] = item.item_id
        json_object['item_name'] = item.item_name
        json_object['item_category'] = item.item_category
        json_object['item_price'] = item.item_price
        json_object['item_quantity'] = item.item_quantity
        json_list.append(json_object)
        print(json_object)
    return jsonify(json_list)


def create_item(json_obj):
    Session = sessionmaker(bind=engine)
    session = Session()
    item = Item(item_id=json_obj['item_id'], item_name=json_obj['item_name'], item_category=json_obj['item_category'],
                item_price=json_obj['item_price'], item_quantity=json_obj['item_quantity'])
    session.add(item)
    session.commit()
    session.close()
    return {"message": "Item added to inventory"}, 201


def update_item(param, json_obj):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = update(Item).where(Item.item_id == param).values(item_name=json_obj['item_name'],
                                                             item_category=json_obj['item_category'],
                                                             item_price=json_obj['item_price']).execution_options(
        synchronize_session="fetch")
    result = session.execute(query)
    row_count = result.rowcount
    print(row_count)
    session.commit()
    session.close()
    if row_count == 0:
        return {"message": "Failed to update item"}, 500
    return {"message": "Item updated in inventory"}, 200


def delete_item(param):
    Session = sessionmaker(bind=engine)
    session = Session()

    query = delete(Item).where(Item.item_id == param).execution_options(synchronize_session="fetch")
    result = session.execute(query)
    row_count = result
    session.commit()
    session.close()

    if row_count == 0:
        return {"message": "Failed to update item"}, 500
    return {"message": "Item deleted from inventory"}, 200


def create_shipment(json_obj):
    Session = sessionmaker(bind=engine)
    session = Session()
    exists = session.query(Item).filter_by(item_id=json_obj['item']['item_id']).first() is not None
    if not exists:
        return {"message": "No such item in inventory"}
    query = update(Item).where(Item.item_id == json_obj['item']['item_id']). \
        values(item_quantity=json_obj['item']['item_quantity'] - 1).execution_options(
        synchronize_session="fetch")
    result = session.execute(query)

    session.commit()
    session.close()

    Session = sessionmaker(bind=engine)
    session = Session()
    shipment = Shipment(shipment_id=json_obj['shipment_id'], shipment_item_id=json_obj['item']['item_id'])
    session.add(shipment)
    session.commit()
    session.close()

    return {"message": "Item added to shipment and inventory updated"}, 201

def list_shipments():
    Session = sessionmaker(bind=engine)
    session = Session()
    shipments = session.query(Shipment).all()

    json_list = []
    for shipment in shipments:
        json_object = {}
        json_object['shipment_id'] = shipment.shipment_id
        json_object['shipment_item_id'] = shipment.shipment_item_id

        json_list.append(json_object)
        print(json_object)
    return jsonify(json_list)