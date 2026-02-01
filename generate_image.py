
import os
from PIL import Image, ImageDraw, ImageFont

def generate_image(text, output_path):
    # Create a new image with a blue background
    img = Image.new('RGB', (1200, 630), color = (73, 109, 137))
    d = ImageDraw.Draw(img)

    # Add text to the image
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()
    
    d.text((10,10), text, fill=(255,255,0), font=font)

    # Save the image
    img.save(output_path)

if __name__ == "__main__":
    # Get the file name from the environment variable
    file_name = os.environ.get("IMAGE_NAME")
    if file_name:
        generate_image(file_name, f"static/images/{file_name}.png")
        print(f"Generated image for {file_name}")
    else:
        print("IMAGE_NAME environment variable not set")
