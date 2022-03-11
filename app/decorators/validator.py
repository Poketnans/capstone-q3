from http import HTTPStatus
from re import match
from functools import wraps
from flask import request
import datetime
from app.errors.json_not_found import JSONNotFound
from app.services import get_data
from datetime import datetime, timedelta, timezone


def validator(
    user_name: str = None,
    date: str = None,
    date_schedule: dict = None,
    phone: str = None,
    cpf: str = None,
    zip_code: str = None,
    email=None,
    password=None,
    birthdate: str = None,
    interval_date: dict = None
):
    '''
            Decorator valida os campos do request pelo tipo de campo requerido.
            Tipos:

                -> Todos os formatos de data são `DD/MM/YYYY`
                - `date_schedule`: recebe um objeto dois datetime com data e hora uma de inicio e fim. `date_schedule` Verifica se o formato datetime é valido e se o intervalo da data esta correto.
                - `date`: Verifica se o formato da data é valido e se essa data ainda não passou.
                - `birthdate`: Verifica se o formato da data é valido.
                - `zip_code`: Verifica se o formato CEP é valido. O CEP aceita somente nesse formato `60000-000`.
                - `cpf`: Verifica se o formato da CPF é valido. O CPF aceita somente números `12345678901` ou números separados por ponto `123.456.789.01`.
                - `email`: Verifica se o formato da email é valido.
                - `password`: Verifica se o formato do password é valido. O password aceita somente uma letra Maiuscula , uma minuscula, um número e um caracter especial.
                - `phone`: Verifica se o formato do phone é valido. O phone aceita somente números. Lembrando que só são aceitos números de telefones fixos e móveis válidos no Brasil.
                - `verify_two`: Verifica se a data atual esta entre este intervalo

            Exceções:
                `É lançada excesão personalida para cada validação`
    '''
    def received_function(function):
        @wraps(function)
        def wrapper(id: int = 0):
            try:
                regex_bithdate = (
                    "^(0[1-9]|[12][0-9]|3[01])[\/\-](0[1-9]|1[012])[\/\-]\d{4}$"
                )
                regex_phone = "^[1-9]{2}(?:[2-8]|9[0-9])[0-9]{3}[0-9]{4}$"
                regex_cep = "^[0-9]{5}-[0-9]{3}$"
                regex_cpf = "^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?[0-9]{2}$"
                regex_email = "^[\w\.]+@([\w-]+\.)+[\w-]{2,4}$"
                regex_password = "^((?=.*[!@#$%^&*()\-_=+{};:,<.>]){1})(?=.*\d)((?=.*[a-z]){1})((?=.*[A-Z]){1}).*$"

                request_json: dict = get_data()

                if request_json.get(date):
                    date_now = datetime.now()
                    pattern = "%d/%m/%Y"

                    try:
                        date_passed = datetime.strptime(
                            request_json[date], pattern)

                    except ValueError as err:
                        resp = {
                            'msg': 'Invalid date format. It must be in the format DD/MM/YYYY'
                        }
                        return resp, HTTPStatus.BAD_REQUEST

                    if date_now >= date_passed:
                        return {"error": "that date has passed"}, 400

                if request_json.get(date_schedule):
                    pattern = "%d/%m/%Y %H:%M:%S"
                    tattoo_schedule = request_json.get(date_schedule)
                    try:
                        date_now = datetime.utcnow()
                        start = tattoo_schedule.get("start")
                        end = tattoo_schedule.get("end")

                        start = datetime.strptime(
                            start, pattern)
                        end = datetime.strptime(end, pattern)
                        rest_time = end - start

                        if start.date() != end.date():
                            return {"error": "the dates are not the same day"}, 400
                        if(start >= end):
                            return {"error": "date and hour start smaller date and hour end"}, 400
                        if rest_time < timedelta(hours=1):
                            return {"error": "Minimum time of 1 hour per tattoo"}, 400

                    except ValueError:
                        return {"error": "datetime in the wrong format. It must be in the format DD/MM/YYYY H:M:S"}, 400

                if request_json.get(birthdate):
                    if not match(regex_bithdate, request_json[birthdate]):
                        return {"error": "birthdate in format incorrect. It must be in the format DD/MM/YYYY"}, 400

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

            except JSONNotFound as err:
                return {"msg": f"{err.describe}"}, err.status_code

            if id:
                return function(id)
            return function()

        return wrapper

    return received_function
