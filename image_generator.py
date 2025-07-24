from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import random

def generate_username_image(username: str, price: str) -> BytesIO:
    width, height = 1280, 768
    background_color = (10, 10, 10)

    # Create base image
    img = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(img)

    # Generate dreamy blurred gradient on right side
    gradient = Image.new("RGB", (width, height), color=0)
    grad_draw = ImageDraw.Draw(gradient)

    colors = random.choice([
        [(255, 92, 92), (255, 171, 157), (255, 212, 165)],
        [(155, 0, 255), (90, 0, 220), (50, 10, 100)],
        [(0, 199, 255), (0, 133, 255), (90, 30, 255)],
        [(255, 94, 247), (255, 196, 251), (255, 120, 221)],
        [(255, 157, 0), (255, 105, 0), (255, 200, 112)],
    ])
    for i, color in enumerate(colors):
        radius = 300 + i * 50
        x = width - 300 + random.randint(-40, 40)
        y = 200 + i * 100
        grad_draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)

    gradient = gradient.filter(ImageFilter.GaussianBlur(180))
    img = Image.blend(img, gradient, alpha=0.7)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        username_font = ImageFont.truetype("arialbd.ttf", 110)
        price_font = ImageFont.truetype("arialbd.ttf", 60)
        desc_font = ImageFont.truetype("arial.ttf", 40)
    except:
        username_font = ImageFont.load_default()
        price_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()

    # Text content
    username_text = f"@{username.lower()}"
    price_text = f"{price}"
    desc_text = "estimated username value"

    # Draw username (left-aligned)
    draw.text((80, 230), username_text, font=username_font, fill="white")
    draw.text((80, 380), price_text, font=price_font, fill="white")
    draw.text((80, 460), desc_text, font=desc_font, fill="#BBBBBB")

    # Output to memory
    output = BytesIO()
    img.save(output, format="PNG")
    output.seek(0)
    return output
