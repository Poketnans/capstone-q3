from re import match
from functools import wraps
from flask import request
import datetime
from app.services import get_files


def validator(
    user_name: str = None,
    date: str = None,
    phone: str = None,
    cpf: str = None,
    zip_code: str = None,
    email=None,
    password=None,
    birthdate: str = None,
):
    '''
            Decorator valida os campos do request pelo tipo de campo requerido.
            Tipos:

                -> Todos os formatos de data são `DD/MM/YYYY`
                - `date`: Verifica se o formato da data é valido e se essa data ainda não passou.
                - `birthdate`: Verifica se o formato da data é valido.
                - `zip_code`: Verifica se o formato CEP é valido. O CEP aceita somente nesse formato `60000-000`.
                - `cpf`: Verifica se o formato da CPF é valido. O CPF aceita somente números `12345678901` ou números separados por ponto `123.456.789.01`.
                - `email`: Verifica se o formato da email é valido.
                - `password`: Verifica se o formato do password é valido. O password aceita somente uma letra Maiuscula , uma minuscula um numero e um caracter especial.
                - `name`: Verifica se o formato de USER_NAME é valido. O USER_NAME aceita somente letras e sem espaço.


            Exceções:
                `É lançada excesão personalidazada para cada validação`
    '''
    def received_function(function):
        @wraps(function)
        def wrapper(id: int = 0):

            regex_bithdate = (
                "^(0[1-9]|[12][0-9]|3[01])[\/\-](0[1-9]|1[012])[\/\-]\d{4}$"
            )
            regex_phone = "^\([1-9]{2}\)(?:[2-8]|9[0-9])[0-9]{3}\-[0-9]{4}$"
            regex_cep = "^[0-9]{5}-[0-9]{3}$"
            regex_cpf = "^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?[0-9]{2}$"
            regex_email = "^[\w\.]+@([\w-]+\.)+[\w-]{2,4}$"

            # nome usuario somente letras sem espaço e sem numero.
            regex_name = "^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$"

            # uma letra Maiuscula , uma minuscula um numero e um caracter especial
            regex_password = "^((?=.*[!@#$%^&*()\-_=+{};:,<.>]){1})(?=.*\d)((?=.*[a-z]){1})((?=.*[A-Z]){1}).*$"

            request_json: dict = get_files()

            if request_json.get(date):
                date_now = datetime.date.today()
                date_passed = request_json[date]

                if not date_now >= date_passed:
                    return {"error": "that date has passed"}, 400

            if request_json.get(birthdate):
                if not match(regex_bithdate, request_json[birthdate]):
                    return {"error": "birthdate in format incorrect"}, 400

            if request_json.get(phone):
                if not match(regex_phone, request_json[phone]):
                    return {"error": "phone in format incorrect"}, 400

            if request_json.get(cpf):
                if not match(regex_cpf, request_json[cpf]):
                    return {"error": "cpf in format incorrect"}, 400

            if request_json.get(zip_code):
                if not match(regex_cep, request_json[zip_code]):
                    return {"error": "cep in format incorrect"}, 400

            if request_json.get(email):
                if not match(regex_email, request_json[email]):
                    return {"error": "email in format incorrect"}, 400

            if request_json.get(password):
                if not match(regex_password, request_json[password]):
                    return {
                        "error": "password in format incorrect",
                        "should be": "Password must contain at least one letter uppercase, one lowercase, one number and one special character",
                    }, 400

            if request_json.get(user_name):
                if not match(regex_name, request_json[user_name]):
                    return {"error": "name in format incorrect"}, 400

            if id:
                return function(id)
            return function()

        return wrapper

    return received_function
