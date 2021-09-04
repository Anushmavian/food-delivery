import json
from unittest import mock
from flaskr.publish import publish_text
from pika.exceptions import AMQPChannelError, AMQPConnectionError


@mock.patch("flaskr.publish.pika.BlockingConnection")
def test_publish_with_AMQPConnectionError(mock_error):
    # given
    details = json.dumps({"orderNumber": 12, "itemName": "pizza", "phoneNumber": "9876543210", "address": "abc"})
    mock_error.side_effect = [AMQPConnectionError()]
    try:
        publish_text(details)

        assert False
    except AMQPConnectionError:
        assert True


