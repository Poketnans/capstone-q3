from PIL import Image
from environs import os

from flask import request
from werkzeug.utils import secure_filename
import werkzeug.exceptions

allowed_formats = ["image/jpeg", "image/png"]


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
    path = "tmp"
    if request.files:
        count = 0
        for key, value in request.files.items():
            if(limite == count):
                break

            with Image.open(value) as open_image:
                (width, height) = (open_image.width//2, open_image.height//2)
                image_resized = open_image.resize((width, height))
                image_resized.save(os.path.join(
                    path, secure_filename(value.filename)), quality=60)
                path_file = f"{path}/{value.filename}"

            with open(path_file, "rb") as file:
                file_bin = file.read()
                filename = secure_filename(value.filename)
                mimetype = value.mimetype
            if mimetype not in allowed_formats:
                raise werkzeug.exceptions.UnsupportedMediaType(
                    description={"msg": f"unsuported media type, allowed formats: {allowed_formats}"})
            image = ImageFile(**{
                "file_bin": file_bin,
                "filename": filename,
                "mimetype": mimetype
            })
            os.remove(path_file)
            count += 1
            list_files.append(image)
        return list_files
    return None
