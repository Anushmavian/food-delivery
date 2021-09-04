import json
import logging
from flaskr.publish import publish_text
from flask import Flask, request, jsonify, abort

main = Flask(__name__)

item = ["biriyani", "burger", "pizza", "sandwich", "kebab"]

@main.route("/place_order", methods=["POST"])
def place_order():
    body = request.json
    if not body:
        return jsonify({"Error": "data not found"}), 400
    if body["itemName"] not in item:
        return jsonify({"message": "invalid input"}), 401
    queue_message = json.dumps(
            {"orderNumber": body["orderNumber"], "itemName": body["itemName"], "phoneNumber": body["phoneNumber"],
             "address": body["address"]})
    publish_text(queue_message)


    logging.info(f"creating id for {body['orderNumber']}")
    return jsonify({"success": True})
        
    


if __name__ == "__main__":
    main.run(host="0.0.0.0")
