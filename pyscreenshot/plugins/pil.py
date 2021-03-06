from PIL import Image


class PilWrapper(object):

    """windows only."""

    home_url = 'http://www.pythonware.com/products/pil/'
    ubuntu_package = 'python-imaging'
    name = 'pil'
    childprocess = False

    def __init__(self):
        import ImageGrab  # windows only
        self.ImageGrab = ImageGrab

    def grab(self, bbox=None):
        return self.ImageGrab.grab(bbox)

    def grab_to_file(self, filename):
        im = self.grab()
        im.save(filename)

    def backend_version(self):
        return Image.VERSION
