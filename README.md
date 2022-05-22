## shopify-challenge

I have created basic APIs for tracking inventory. Below are the CRUD operations. I have also created APIs for shipment and assigned inventory to the shipment.

To run the app on Replit, the folder structure is brindap1210/shopify-structure. The app is located under this directory. So, change the directory to inventory-tracking and run the application. Below are the cURL's for the APIs with JSON body through which the APIs can be tested. I have used SQLAlchemy as an Object Relational mapping (ORM) to map the models with database in Python. And I have used Flask for building APIs in Python.

# Create item:

Request:

curl --location --request POST 'http://127.0.0.1:5000/createitem' \
--header 'Content-Type: application/json' \
--data-raw '{
    "item_id": 2,
    "item_name": "Laptop",
    "item_price": 1000,
    "item_category": "Gadgets",
    "item_quantity": 6
}'

Response:

{
  "message": "Item added to inventory"
}

# Retrieve items:

Request:

curl --location --request GET 'http://127.0.0.1:5000/list'

Response:

curl --request GET "http://127.0.0.1:5000/list"
[
  {
    "item_category": "Gadgets", 
    "item_id": 2, 
    "item_name": "Laptop", 
    "item_price": 1000.0, 
    "item_quantity": 6
  }
]

# Update item: 

Request: 

curl --location --request PATCH 'http://127.0.0.1:5000/updateitem/2' \
--header 'Content-Type: application/json' \
--data-raw '{
    "item_id": 2,
    "item_name": "Headphones",
    "item_price": 1000,
    "item_category": "Gadget"
}'

Response:

{
  "message": "Item updated in inventory"
}

# Delete item:

Request: 

curl --location --request DELETE 'http://127.0.0.1:5000/deleteitem/1'

Response:

{
    "message" : "Item deleted from inventory"
}

# Create Shipment:

Request: 

curl --location --request POST 'http://127.0.0.1:5000/createshipment' \
--header 'Content-Type: application/json' \
--data-raw '{
     "shipment_id" : 10,
    "item" : {
        "item_category": "Gadgets",
        "item_id": 5,
        "item_name": "Mobile",
        "item_price": 500.0,
        "item_quantity": 5
    }
}'

Response:

{
    "message" : "Shipment created"
}

# Get Shipments:

Request: 

curl --location --request GET 'http://127.0.0.1:5000/listshipment'

Response:

{
    "shipment_id" : 1,
    "shipment_item_id" : 2
}


