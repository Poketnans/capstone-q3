from http import HTTPStatus

from app.models import Storage


class UnavaliableItemQuantityError(Exception):
    code = HTTPStatus.CONFLICT
    description = {
        "msg": "unavaliable item quantity",
        "item": {}
    }

    def __init__(self, item: Storage):
        self.description['item'] = {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "remaining_quantity": item.quantity
        }
