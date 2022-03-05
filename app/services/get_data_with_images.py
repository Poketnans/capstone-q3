from json import loads

from flask import request
from werkzeug.utils import secure_filename

from app.errors import JSONNotFound


class ImageFile():
    def __init__(self, **kargs) -> None:
        self.file_bin = kargs['file_bin']
        self.filename = kargs['filename']
        self.mimetype = kargs['mimetype']


def get_data_with_images(exception: bool = True, key_form: str = "data") -> "dict or None":
    ''' Função captura os dados de uma rota.
        A captura é feita caso a rota seja com `JSON` ou `Multipart-form` caso contrario lança um  exceção.
        As imagens são capturadas na função `get_files`.
        `exception` campo boleano opcional que define se é levantado exceções. O valor por padrão é True.

        Exceções:
            `from app.errors.JSONNotFound` - Body vazio.
    '''

    data = None
    if(request.get_json()):
        data: dict = request.get_json()
    elif request.form.get(key_form):
        data: dict = loads(request.form.get(key_form))
        if data.get("file"):
            data.pop("file")
    elif exception:
        raise JSONNotFound
    return data


"""def get_files() -> ImageFile:
    ''' Função captura os arquivos de uma rota.
        A captura é feita caso a rota seja com `Multipart-form` caso contrario retorna none.

    '''

    if request.files:
        file = request.files["file"]
        file_bin = file.read()
        filename = secure_filename(file.filename)
        mimetype = file.mimetype
        image = ImageFile(**{
            "file_bin": file_bin,
            "filename": filename,
            "mimetype": mimetype
        })
        return image
    return None"""


def get_files(limite=None) -> "list[ImageFile] or None":
    ''' Função captura os arquivos de uma rota.
        A captura é feita caso a rota seja com `Multipart-form` caso contrario retorna none.
        `limite` é opicional e referente a quantidade de imagens.
    '''
    list_files = []
    if request.files:
        count = 0
        for key, value in request.files.items():
            if(limite == count):
                break
            file = value
            file_bin = file.read()
            filename = secure_filename(file.filename)
            mimetype = file.mimetype
            image = ImageFile(**{
                "file_bin": file_bin,
                "filename": filename,
                "mimetype": mimetype
            })
            count += 1
        list_files.append(image)
        return list_files
    return None
