from PIL import Image


def is_transparent(image):
    image = Image.open(image).convert("RGBA")
    alpha_range = image.getextrema()[-1]
    if alpha_range == (255, 255):
        return False
    else:
        return True