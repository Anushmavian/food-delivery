from src.id_creator import create_id


def test_id_creator():
    # given
    frame = {"orderNumber": 12, "itemName": "pizza", "phoneNumber": "9876543210", "address": "abc"}
    try:
        # when
        create_id(frame)
        # then
        assert True
    except TypeError:
        assert False





