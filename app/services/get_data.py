from json import loads

from flask import request

from app.errors import JSONNotFound


def get_data(exception: bool = True, key_form: str = "data") -> "dict or None":
    ''' Função captura os dados de uma rota.
        A captura é feita caso a rota seja com `JSON` ou `Multipart-form` caso contrario lança um  exceção.
        As imagens são capturadas na função `get_files`.
        `exception` campo boleano opcional que define se é levantado exceções. O valor por padrão é True.

        Exceções:
            `from app.errors.JSONNotFound` - Body vazio.
    '''

    data = {}
    if(request.get_json()):
        data: dict = request.get_json()
    elif request.form.get(key_form):
        data: dict = loads(request.form.get(key_form))
        if data.get("file"):
            data.pop("file")

    return data
