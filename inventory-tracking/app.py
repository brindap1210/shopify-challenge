from flask import Flask, request
from sqlalchemy.ext.declarative import declarative_base
import controller
import sqlalchemy as db

app = Flask(__name__)


@app.route('/list', methods=['GET'])
def list_items():
    return controller.list_items()


@app.route('/createitem', methods=['POST'])
def create_item():
    json_obj = request.get_json()
    return controller.create_item(json_obj)


@app.route('/updateitem/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    json_obj = request.get_json()
    return controller.update_item(item_id, json_obj)


@app.route('/deleteitem/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return controller.delete_item(item_id)

@app.route('/createshipment', methods=['POST'])
def create_shipment():
    json_obj = request.get_json()
    return controller.create_shipment(json_obj)

@app.route('/listshipment', methods=['GET'])
def list_shipments():
    return controller.list_shipments()

if __name__ == '__main__':
    app.run(debug=True)
