import base64
import io
from PIL import Image

def get_pic_str(path):
    with open(path, "rb") as image:
        b64string = base64.b64encode(image.read())
    # print(b64string)
    return b64string

def save_pic(str_input, path):
    f = io.BytesIO(base64.b64decode(str_input))
    pil_image = Image.open(f)
    pil_image.save(path, "JPEG")


