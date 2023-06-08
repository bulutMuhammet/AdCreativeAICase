from PIL import Image

def add_background(foreground_image_path, background_image_path):
    foreground_image = Image.open(foreground_image_path).convert("RGBA")
    background_image = Image.open(background_image_path).convert("RGBA")


    resized_background = background_image.resize(foreground_image.size, Image.ANTIALIAS)

    merged_image = Image.new("RGBA", foreground_image.size)
    merged_image.paste(resized_background, (0, 0))
    merged_image.paste(foreground_image, (0, 0), mask=foreground_image)

    return merged_image

foreground_image_path = "input.png"
background_image_path = "bg.png"

result_image = add_background(foreground_image_path, background_image_path)
result_image.save("sonuc.png")
result_image.show()
