from http import HTTPStatus
from json import JSONDecodeError
from typing import Callable
from flask import jsonify, Response
from functools import wraps

from app.errors import FieldMissingError, InvalidValueTypesError, JSONNotFound
from app.services.get_data_with_images import get_data_with_images
from app.services import payload_eval


def verify_payload(optional: list = [], **fields_and_types) -> Callable:
    ''' 
        Realiza a verificação de payload e trata os erros associados.

        `optional` - lista com os nomes dos campos opcionais.

        `kwargs` - campos possíveis para a requisição. Seus valores\n
            correspondem ao tipo de dado permitido para aquele campo.

        No final, este decorator passa, como argumento para o controller, um\n
            objeto chamado `payload` contendo os campos filtrados pela função\n
            `app.services.payload_eval`, bastando fazer com que o controller\n
            receba o parâmetro `payload` para recuperar os dados já filtrados.
    '''

    def decorated_controller(controller: Callable) -> Callable:
        @wraps(controller)
        def wrapper(*args, **kwargs) -> tuple[Response, int]:
            '''
                Realiza a captura das exceções relacionadas ao tratamento de\n
                payload e interrompe o fluxo da requisição retornando as\n
                devidas mensagens e códigos de erro.
            '''
            try:
                data = get_data_with_images()

                filtered_data = payload_eval(data, optional, **fields_and_types)

                return controller(*args, payload=filtered_data, **kwargs)

            except JSONDecodeError:
                msg = {"msg": "JSON in invalid format"}
                return jsonify(msg), HTTPStatus.BAD_REQUEST
            except InvalidValueTypesError as err:
                return jsonify(err.description), err.code
            except FieldMissingError as err:
                return jsonify(err.description), err.code
            except JSONNotFound as err:
                return {"msg": f"{err.describe}"}, err.status_code
        return wrapper
    return decorated_controller
