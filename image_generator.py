# image_generator.py

from PIL import Image, ImageDraw, ImageFont
import random
import os

# Dimensions (1280x768)
WIDTH, HEIGHT = 1280, 768
PADDING = 60

# Fonts (update paths if needed)
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Define gradient themes
GRADIENTS = {
    "default": ["#0f0c29", "#302b63", "#24243e"],
    "danger": ["#2c001e", "#78002e", "#e7005c"],
    "cool": ["#000428", "#004e92"],
    "sunset": ["#ff512f", "#dd2476"],
    "calm": ["#2193b0", "#6dd5ed"],
    "mint": ["#76b852", "#8DC26F"],
    "midnight": ["#232526", "#414345"],
    "dream": ["#c33764", "#1d2671"]
}

# Match tone to theme
def choose_gradient(username: str) -> list:
    uname = username.lower()
    if any(x in uname for x in ["kill", "hit", "dead", "rage", "hunt"]):
        return GRADIENTS["danger"]
    if any(x in uname for x in ["calm", "soft", "float", "cloud"]):
        return GRADIENTS["calm"]
    if any(x in uname for x in ["dream", "hopeless", "less"]):
        return GRADIENTS["dream"]
    return random.choice(list(GRADIENTS.values()))

# Create vertical gradient background
def draw_gradient_background(colors: list) -> Image:
    base = Image.new("RGB", (WIDTH, HEIGHT), colors[0])
    top = Image.new("RGB", (WIDTH, HEIGHT), colors[-1])
    mask = Image.linear_gradient("L").resize((WIDTH, HEIGHT))
    blended = Image.composite(top, base, mask)
    return blended

# Clean bullet point list formatting
def format_bullets(lines: list, draw, font, start_y, color) -> int:
    y = start_y
    for line in lines:
        draw.text((PADDING, y), f"• {line}", font=font, fill=color)
        y += font.size + 10
    return y

# Main image generation
def generate_image(username: str, price_str: str, pros: list, cons: list, save_path: str = "output.png") -> str:
    bg = draw_gradient_background(choose_gradient(username))
    draw = ImageDraw.Draw(bg)

    # Fonts
    font_title = ImageFont.truetype(FONT_BOLD, 96)
    font_sub = ImageFont.truetype(FONT_REGULAR, 36)
    font_text = ImageFont.truetype(FONT_REGULAR, 32)

    # Username + Price
    draw.text((PADDING, PADDING), username.lower(), font=font_title, fill="white")
    draw.text((PADDING, PADDING + 110), f"Estimated value: {price_str}", font=font_sub, fill="white")

    # Pros
    pros_y = PADDING + 190
    draw.text((PADDING, pros_y), "Pros", font=font_sub, fill="#9effc4")
    pros_y += 50
    pros_y = format_bullets(pros, draw, font_text, pros_y, "#e6ffe4")

    # Cons
    cons_y = pros_y + 40
    draw.text((PADDING, cons_y), "Cons", font=font_sub, fill="#ffbaba")
    cons_y += 50
    format_bullets(cons, draw, font_text, cons_y, "#ffeaea")

    bg.save(save_path)
    return save_path
