from PIL import Image, ImageDraw, ImageFont
import random
import os

WIDTH, HEIGHT = 1280, 768

FONTS_DIR = "assets/fonts"
GRADIENTS_DIR = "assets/gradients"
FONT_BOLD = os.path.join(FONTS_DIR, "GeneralSans-Bold.otf")
FONT_REGULAR = os.path.join(FONTS_DIR, "GeneralSans-Regular.otf")

def pick_gradient(username: str):
    # Match tone: red for aggressive, blue for aesthetic, etc.
    if any(word in username for word in ["hit", "kill", "blast", "rage", "slay"]):
        theme = "red"
    elif any(word in username for word in ["hopeless", "scopeless", "void", "less"]):
        theme = "blue"
    elif any(word in username for word in ["grace", "flow", "fade", "calm"]):
        theme = "purple"
    else:
        theme = "default"

    files = os.listdir(GRADIENTS_DIR)
    candidates = [f for f in files if theme in f] or files
    return os.path.join(GRADIENTS_DIR, random.choice(candidates))

def generate_image(username: str, est_price: int, category: str, notes: str = ""):
    uname = username.lower().strip("@")
    price_str = f"${est_price:,}"

    gradient_path = pick_gradient(uname)
    bg = Image.open(gradient_path).convert("RGBA").resize((WIDTH, HEIGHT))

    draw = ImageDraw.Draw(bg)

    font_username = ImageFont.truetype(FONT_BOLD, 120)
    font_price = ImageFont.truetype(FONT_BOLD, 80)
    font_info = ImageFont.truetype(FONT_REGULAR, 36)

    draw.text((60, 200), f"@{uname}", font=font_username, fill="white")
    draw.text((60, 350), price_str, font=font_price, fill="white")
    draw.text((60, 480), f"Category: {category}", font=font_info, fill="white")
    draw.text((60, 540), notes, font=font_info, fill="white")

    output_path = f"output/{uname}_rate.png"
    os.makedirs("output", exist_ok=True)
    bg.save(output_path)

    return output_path
