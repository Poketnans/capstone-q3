from PIL import Image

from app.classes.image_file import ImageFile


def generate_image_default() -> ImageFile:
    '''
        Gera uma imagem automaticamente para a instancia da classe e retorna um objeto de `ImageFile` com image_mimetype,image_bin e image_filename.
    '''
    url_image = "./app/assets/image_default.png"
    image_mimetype: str = None
    image_bin = None
    image_filename = "filename"

    image = Image.open(url_image)
    image_mimetype = image.get_format_mimetype()

    with open(url_image, "rb") as file:
        image_bin: str = file.read()
    image = ImageFile(**{
        "filename": image_filename,
        "file_bin": image_bin,
        "mimetype": image_mimetype
    })
    return image
