from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import os


def generate_username_image(username: str, price: str, tone: str) -> BytesIO:

    # Image dimensions (wide format)
    width, height = 1280, 768
    
    # Create base image
    image = Image.new("RGB", (width, height), color=(10, 10, 10))
    draw = ImageDraw.Draw(image)

    # Define gradients based on username tone
    def get_gradient_colors(name):
        name = name.lower()
        if any(word in name for word in ["hopeless", "scopeless", "lifeless"]):
            return [(30, 30, 30), (80, 20, 60)]  # muted purple/grey
        elif any(word in name for word in ["hit", "kill", "dark"]):
            return [(40, 0, 0), (120, 0, 0)]  # dark reds
        elif any(word in name for word in ["love", "dream", "soul"]):
            return [(90, 40, 150), (255, 100, 180)]  # dreamy pinks/purples
        else:
            return [(0, 90, 150), (90, 0, 160)]  # default cool gradient

    # Apply gradient background
    def apply_gradient(image, start_color, end_color):
        base = Image.new('RGB', image.size, start_color)
        top = Image.new('RGB', image.size, end_color)
        mask = Image.linear_gradient('L').resize(image.size)
        blended = Image.composite(top, base, mask)
        image.paste(blended, (0, 0))

    gradient_start, gradient_end = get_gradient_colors(username)
    apply_gradient(image, gradient_start, gradient_end)

    # Fonts
    font_path_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font_large = ImageFont.truetype(font_path_bold, 140)
    font_small = ImageFont.truetype(font_path_bold, 48)

    # Text positions
    username_text = f"@{username.lower()}"
    price_text = f"${price}"
    desc_text = "clean ai-evaluated telegram handle"

    # Calculate center positions
    text_x = 80
    draw.text((text_x, 200), username_text, font=font_large, fill=(255, 255, 255))
    draw.text((text_x, 380), price_text, font=font_large, fill=(255, 255, 255))
    draw.text((text_x, 540), desc_text, font=font_small, fill=(255, 255, 255, 180))

    # Export to BytesIO
    output = BytesIO()
    image.save(output, format='PNG')
    output.seek(0)
    return output
