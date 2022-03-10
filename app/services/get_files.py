from json import loads

from flask import request
from werkzeug.utils import secure_filename


class ImageFile():
    def __init__(self, **kargs) -> None:
        self.file_bin = kargs['file_bin']
        self.filename = kargs['filename']
        self.mimetype = kargs['mimetype']


def get_files(limite=None) -> "list[ImageFile] or None":
    ''' Função captura os arquivos de uma rota
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
