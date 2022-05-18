from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = "inventory"

    item_id = Column('item_id', Integer, primary_key=True, index=True)
    item_name = Column('item_name', String)
    item_category = Column('item_category', String)
    item_price = Column('item_price', Float)
    item_quantity = Column('item_quantity', Integer)

    def __repr__(self):
        return "<Item(item_id='%s', item_name='%s', item_category='%s', item_price=%s, item_quantity=%s)>" % (
            self.item_id, self.item_name, self.item_category, self.item_price, self.item_quantity)

class Shipment(Base):
    __tablename__ = "shipment"

    shipment_id = Column('shipment_id', Integer, primary_key=True, index=True)
    shipment_item_id = Column('shipment_item_id', Integer, ForeignKey('inventory.item_id'), index=True)

    def __repr__(self):
        return "<Shipment(shipment_id='%s', shipment_item_id='%s')>" % (self.shipment_id, self.shipment_item_id)

import sqlalchemy as db
engine = db.create_engine('sqlite:///shopify.sqlite', echo=True)
# Item.__table__.drop(engine)
Base.metadata.create_all(bind=engine)