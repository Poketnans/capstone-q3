
class ImageFile():
    ''' Ultilizada para possibilitar o intelisense '''

    def __init__(self, **kargs) -> None:
        self.file_bin = kargs['file_bin']
        self.filename = kargs['filename']
        self.mimetype = kargs['mimetype']
