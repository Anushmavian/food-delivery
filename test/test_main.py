from flaskr.main import main
import json


def test_create_id():
    payload = {
        "orderNumber": "12",
        "itemName": "pizza",
        "phoneNumber": "9876543210",
        "address": "abc"
    }
    response = main.test_client().post('/place_order', data=json.dumps(payload), content_type="application/json")
    assert response.status_code == 200
    assert json.loads(response.data.decode()) == {"success": True}


def test_create_id_no_data():
    payload = {}
    response = main.test_client().post('/place_order', data=json.dumps(payload), content_type="application/json")
    assert response.status_code == 400
    assert json.loads(response.data.decode()) == {"Error": "data not found"}


def test_create_id_invalid_item():
    payload = {
        "phoneNumber": "9876543210",
        "orderNumber": "12",
        "address": "abc",
        "itemName": "noodles"
    }
    response = main.test_client().post('/place_order', data=json.dumps(payload), content_type="application/json")
    assert response.status_code == 401
    assert json.loads(response.data.decode()) == {"message": "invalid input"}
