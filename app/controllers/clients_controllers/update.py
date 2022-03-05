from http import HTTPStatus
from flask import current_app, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from sqlalchemy.orm import Session

from app.errors import JSONNotFound
from app.models import Client
from app.services.get_data_with_images import get_data_with_images, get_files
from app.services.payload_eval import payload_eval


@jwt_required()
def update():
    try:
        session: Session = current_app.db.session
        client_jwt = get_jwt_identity()
        id = client_jwt['id']

        client: Client = Client.query.get(id)

        data = get_data_with_images(exception=False)
        if(data):
            optional_fields = ["name", "email", "password", "phone", "general_information",
                               "street", "number", "city", "image_name", "image_bin", "image_mimetype"]
            field_types = {
                'name': str,
                'email': str,
                'phone': str,
                'password': str,
                'street': str,
                'number': int,
                'city': str
            }
            data = payload_eval(data, optional_fields, **field_types)
            for key, value in data.items():
                setattr(client, key, value)

        files = get_files()
        if files:
            for file in files:
                client.image_bin = file.file_bin
                client.image_name = file.filename
                client.image_mimetype = file.mimetype
        if not data and files:
            raise JSONNotFound

        # session.add(client)
        # session.commit()
        print("")
        print("CLient -> ", data)
        print("")
        print("CLient -> ", client)
        print("")

        return jsonify(client), HTTPStatus.OK
    except JSONNotFound as e:
        return {"error": f"{e.describe}"}, e.status_code
